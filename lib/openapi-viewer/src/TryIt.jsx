import { reactive } from "vue";
import { data } from "./OpenAPIViewer";
import "./TryIt.scss"
import { Code } from "./Code";

/** Vue component to render an interactive Try-it editor for an API endpoint */
export const TryIt = {
  props: ["endpoint"],
  setup(props) {
    const ui = reactive({ tab: "curl", busy: false })
    const payload = reactive({ "API Key": data.API_KEY })
    const params = gather_params(props.endpoint)
    const headerParams = params.filter(p => p.in === "header")
    const pathParams = params.filter(p => p.in === "path")
    const queryParams = params.filter(p => p.in === "query")
    const bodyParams = params.filter(p => p.in === "body")

    async function execute() {
      ui.busy = true;
      const [status, res] = await execute_endpoint(props.endpoint, payload)
      ui.status = status
      ui.res = res
      ui.busy = false;
    }

    function needRequired() {
      for (const p of params) {
        if (p.required && !payload[p.name]) return true
      }
      return false
    }

    return () => {
      return <div class="try-it">
        <div class="parameters">
          {headerParams?.length > 0 && <div class='params headers'><h3>Headers</h3>
            {headerParams.map(p => Field(p, payload))}
          </div>}
          {pathParams?.length > 0 && <div class='params path-params'><h3>Path parameters</h3>
            {pathParams.map(p => Field(p, payload))}
          </div>}
          {queryParams?.length > 0 && <div class='params query-params'><h3>Query parameters</h3>
            {queryParams.map(p => Field(p, payload))}
          </div>}
          {bodyParams?.length > 0 && <div class='params body-params'><h3>Body parameters</h3>
            {bodyParams.map(p => Field(p, payload))}
          </div>}
        </div>
        <footer>
          <button type="submit" disabled={ui.busy || needRequired()} onClick={execute}>Send</button>
        </footer>


        <div class='code-examples'>
          <h3>Code snippets</h3>
          <ul role="tablist">
            <li class="tab-success" class={{ selected: ui.tab === "curl" }} onClick={() => ui.tab = "curl"} role="tab" aria-selected="true" aria-disabled="false">cURL</li>
            <li class="tab-success" class={{ selected: ui.tab === "python" }} onClick={() => ui.tab = "python"} role="tab" aria-selected="false" aria-disabled="false">Python</li>
            <li class="tab-success" class={{ selected: ui.tab === "js" }} onClick={() => ui.tab = "js"} role="tab" aria-selected="false" aria-disabled="false">Javascript</li>
          </ul>

          <div>
            {ui.tab === "curl" && <Code lang="shell" src={generate_curl(props.endpoint, payload)} />}
            {ui.tab === "python" && <Code lang="python" src={generate_python(props.endpoint, payload)} />}
            {ui.tab === "js" && <Code lang="javascript" src={generate_js(props.endpoint, payload)} />}
          </div>

          {((ui.res && ui.status) || ui.busy) && <div class="results">
            <h3>Response</h3>
            {ui.res && ui.status && <Code lang="json" class={ui.status} src={ui.res} />}
            {ui.busy && <div class="ui-spinner" />}
          </div>}

        </div>
      </div>
    };
  },
};


export const Field = ({ name, required }, payload) => <div class="field">
  <label>{name} <span class="required">{!!required && "*"}</span></label>
  <input
    class={{ error: !payload[name] && required }}
    onInput={({ target }) => payload[name] = target.value}
    value={payload[name] || ""}
    placeholder={required ? "required" : ""}
    name={`sekoia-${name}`}
    type={name === "API Key" ? "password" : "text"}
  ></input>
</div>


function gather_params(endpoint) {
  const params = [];
  // Always prepend API Key field
  params.push({ name: "API Key", in: "header", required: true });
  // ... query params
  params.push(...(endpoint.parameters || []));

  // ... path params
  for (const pathParam of endpoint.path.matchAll(/\{([^:\}]+)(:([^:\}]+))?\}/g)) {
    if (!params.find((p) => p.name === pathParam[1] && p.in === "path")) {
      params.push({
        name: pathParam[1],
        in: "path",
        schema: { type: pathParam[3] || "any" },
      });
    }
  }

  // ... body params
  let bodySchema = endpoint.requestBody?.content?.["application/json"]?.schema;
  if (bodySchema?.["$ref"]) {
    bodySchema = bodySchema?.["$ref"]?.replace(/^#\/components\/schemas\//, "");
    const body = data.schema.components?.schemas?.[bodySchema]?.properties || {};
    for (const k in body) {
      params.push({ name: k, in: "body" });
    }
  } else {
    const body = bodySchema?.properties || {};
    for (const k in body) {
      params.push({ name: k, in: "body" });
    }
  }

  // Filter-out authentication fields
  return params.filter(
    (p) => !["authorization", "access_token_cookie"].includes(p.name)
  );
}

// Generate a try-it query from entered {params} for the given {method}+{endpoint}
function generate_query(
  endpoint,
  payload,
  { inline_query_params = true } = {}
) {
  data.API_KEY = payload["API Key"]
  const method = endpoint.method.toUpperCase();
  let url = (data.schema.servers[0]?.url || "") + endpoint.path;
  const params = gather_params(endpoint)
  for (const p of params) p.value = payload[p.name]

  const hasBodyParams = !!params?.find((p) => p.in === "body");
  const bodyParams = params?.filter(
    (p) => p.in === "body" && ![undefined, ""].includes(p.value)
  );
  let headers = { Authorization: "Bearer <YOUR_API_KEY>" };
  let body, query_params;

  // Interpolate path params
  url = url.replaceAll(
    /\{([^:\}]+)(:[^\}:]+)?\}/g,
    (m, placeholder) =>
      params.find((p) => p.in === "path" && p.name === placeholder)?.value || ""
  );

  // Interpolate query params
  if (method === "GET") {
    query_params = params
      .filter(
        (p) => p.in === "query" && p.value !== "" && p.value !== undefined
      )
      .map((p) => [p.name, p.value]);
    if (inline_query_params) {
      url += "?" + new URLSearchParams(Object.fromEntries(query_params));
    }
  }

  // Generate JSON body
  else if (hasBodyParams) {
    body = Object.fromEntries(bodyParams.map((p) => [p.name, p.value]));

    // Try to JSON parse each body param, in case it expects arrays or other composite values
    for (const k in body) {
      try {
        body[k] = JSON.parse(body[k]);
      } catch { }
    }
    headers["Content-Type"] = "application/json";
    body = JSON.stringify(body);
  }

  return { method, url, headers, body, query_params };
}

// Generate a CURL command line for an OpenAPI endpoint
function generate_curl(endpoint, payload) {
  let { url, headers, body } = generate_query(endpoint, payload);
  let out = `curl -X ${endpoint.method.toUpperCase()} ${url}`;
  Object.entries(headers).forEach(([h, v]) => (out += ` -H '${h}:${v}'`));
  if (body) out += ` --data-raw '${body}'`;
  return out
}

// Generate a Python example code for an OpenAPI endpoint
function generate_python(endpoint, payload) {
  let { url, headers, body, query_params } = generate_query(
    endpoint,
    payload,
    {
      inline_query_params: false,
    }
  );
  let out = `import requests
import json

result = requests.request(
    "${endpoint.method.toUpperCase()}",
    "${url}",
`;
  if (query_params) {
    out += `    params=${JSON.stringify(
      Object.fromEntries(query_params),
      null,
      4
    ).replaceAll("\n", "\n    ")},\n`;
  }
  if (body) {
    out += `    json=${JSON.stringify(JSON.parse(body), null, 4).replaceAll(
      "\n",
      "\n    "
    )},\n`;
  }
  if (headers) {
    out += `    headers=${JSON.stringify(headers, null, 4).replaceAll(
      "\n",
      "\n    "
    )},\n`;
  }
  out += `).json()
print(json.dumps(result, indent=4))
  `;
  return out
}

// Generate a Javascript example code for an OpenAPI endpoint
function generate_js(endpoint, payload) {
  let { url, headers, body } = generate_query(endpoint, payload);
  let out = `await fetch("${url}", {
    method: "${endpoint.method.toUpperCase()}",
`;
  if (body) {
    out += `    body: \`${JSON.stringify(JSON.parse(body), null, 4).replaceAll(
      "\n",
      "\n    "
    )}\`,\n`;
  }
  if (headers) {
    out += `    headers: ${JSON.stringify(headers, null, 4).replaceAll(
      "\n",
      "\n    "
    )},\n`;
  }

  out += `}).then(res=>res.json())
  `;
  return out
}

async function execute_endpoint(endpoint, payload) {
  let { url, headers, body } = generate_query(endpoint, payload);
  headers = {
    ...headers,
    accept: "application/json",
    Authorization: `Bearer ${payload['API Key']}`,
  };

  const [status, res] = await fetch(url, { method: endpoint.method, body, headers })
    .then(async (x) => {
      if (x.status >= 400) {
        return ["error", `Error ${x.status}\n${await x.text()}}`];
      }
      return ["success", JSON.stringify(await x.json(), null, 4)];
    })
    .catch((e) => {
      return ["error", `${e}`]
    });

  return [status, res]
}
