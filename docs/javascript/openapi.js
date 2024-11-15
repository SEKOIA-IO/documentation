// Declare officially documented regions
const REGIONS = ["FRA1", "FRA2", "MCO1", "UAE1"];

// Declare default tagGroups for mapping OpenAPI tags to left menu groups
const X_TAG_GROUPS = [
  {
    name: "User",
    tags: [
      "User Authentication",
      "me",
      "mfa", // TODO: split 'mfa' into administration and self
      "permissions",
    ],
  },
  {
    name: "Workspace",
    tags: [
      "customers", // TODO deprecated, get rid of it
      "communities",
      "api-keys",
      "licenses",
      "invitations",
      "plans",
      "sub-communities",
      "avatars",
      "users", // TODO set this tag on all user administration stuff
      "roles",
    ],
  },
  {
    name: "Intelligence",
    tags: [
      "Observables",
      "CTI Objects",
      "Bundles",
      "Collections",
      "Exports",
      "Outgoing Feeds",
      "Graphs",
      "MISP",
      "Objects",
      "Observable relationships",
      "Indicators",
      "Images",
      "support",
      "Labels",
      "Kill Chains",
    ],
  },
  {
    name: "Collect",
    tags: [
      "Intakes",
      "Assets",
      "Atoms",
      "Intakes by status",
      "Intakes errors and warnings",
      "Intakes lag and processing lag",
      "formats",
      "IOC Collections",
    ],
  },

  {
    name: "Detection rules",
    tags: [
      "Rules",
      "datasources",
      "generation-modes",
      "rules-catalog",
      "alert-filter", // TODO: to create, this tag doesn't exist yet
    ],
  },
  {
    name: "Alerts",
    tags: [
      "Alert",
      "Alert Entities",
      "Alert Rules",
      "Alert Sources and Targets",
      "Countermeasures",
      "Cyber Kill Chain",
      "Stats",
      "Alert Status",
      "Alert Type",
    ]
  },{
    name:"Cases",
    tags: [
      "Case",
      "Comments",
      "Statistics",
      "Enrichers",
      "Callbacks",
      "Services",
      "Tasks",
    ]
  },
  {
    name: "Playbooks",
    tags: [
      "Playbook actions telemetry",
      "modules",
      "Action Runs",
      "Actions",
      "Changes",
      "Connector Configurations",
      "Connectors",
      "Module Configurations",
      "Modules",
      "Node Runs",
      "Playbooks Runs",
      "Playbooks",
      "Trigger Configurations",
      "Triggers",
    ],
  },

  {
    name: "AI assistant", // TODO: Make that private
    tags: ["Roy tokens use telemetry"],
  },
];

function $element(tag, content = "", cls = "") {
  const el = document.createElement(tag);
  if (content) el.innerHTML = content;
  if (cls) el.className = cls;
  return el;
}

function merge_openapi_schemas(schemas) {
  const paths = {};
  const definitions = {};

  for (const s of schemas) {
    if (!s?.info?.title) continue;
    console.log("Merge", s.info.title);

    const ref_mapping = {};
    const prefix = s.info.title.replace(/\s+/, "_") + "_";

    // Prefix colliding component names
    for (let key in s.components?.schemas || {}) {
      const def = s.components?.schemas[key];
      if (definitions[key]) {
        ref_mapping[key] = prefix + key;
        key = prefix + key;
      }
      if (definitions[key]) {
        console.error(`Definition collision for ${key}`);
        continue;
      }
      definitions[key] = def;
    }

    // Rewrite components refs accordingly
    object_walk(
      s,
      (k, v) => {
        if (
          k === "$ref" &&
          typeof v === "string" &&
          v.startsWith("#/components/schemas/")
        ) {
          const ref = v.substring("#/components/schemas/".length);
          return "#/components/schemas/" + (ref_mapping[ref] || ref);
        }
        return v;
      },
      true
    );

    // Merge endpoints paths
    for (const p in s.paths || {}) {
      for (const method in s.paths[p]) {
        if (method !== "parameters" && !s.paths[p][method].tags?.length) {
          console.warn(`Endpoint ${method} ${p} has no tag, skipping`);
          continue;
        }
        if (paths[p]?.[method]) {
          console.error(`Endpoint collision for ${method} ${p}`);
          continue;
        }
        paths[p] ||= {};
        paths[p][method] = s.paths[p][method];
      }
    }
  }

  const schema = {
    ...schemas[0],
    openapi: "3.1.0",
    info: {
      title: "Sekoia.io API Documentation",
      description: "Documentation of all Sekoia.io REST API endpoints",
      version: "1.0",
    },
    servers: [
      {
        url: "https://api.sekoia.io",
        description: "Sekoia.io API",
      },
    ],
    paths,
    components: {
      schemas: definitions,
    },

    "x-tagGroups": X_TAG_GROUPS,
  };

  return schema;
}

async function init_openapi_documentation() {
  let _APIKEY = "";
  const region = (
    new URLSearchParams(location.search).get("region") || "fra1"
  ).toLowerCase();

  const openapi_el = document.querySelector("#openapi");
  if (!openapi_el) return;

  // Collect services OpenAPI schema URLs from rendered markdown
  let schema_urls = Array.from(
    new Set(
      openapi_el
        .querySelector("& > section")
        .innerText.split("\n")
        .map((x) => x.trim())
        .filter((x) => x.length > 0)
    )
  );

  // Replace with the selected region's URLs
  if (region !== "fra1") {
    schema_urls = schema_urls.map((url) =>
      url.replace("https://app.sekoia.io/", `https://app.${region}.sekoia.io/`)
    );
  }

  // Convert legacy Swagger 2.0 schemas to OpenAPI 3.1
  const schemas = (
    await Promise.all(
      schema_urls.map(async (url) => {
        try {
          let schema = await fetch(url).then((x) => x.json());
          if (schema.swagger) schema = convert_swagger_to_openapi(schema);

          // Lint the resulting OpenAPI 3.1 schema to polish parameters
          Object.values(schema.paths).forEach((p) => {
            Object.values(p).forEach((endpoint) => {
              // Gather scattered body params into one object body param
              let params = [...(endpoint.parameters || [])];
              let bodyParams = params.filter((p) => p.in === "body");
              if (bodyParams?.length > 0) {
                endpoint.requestBody = {
                  content: {
                    "application/json": {
                      schema: {
                        type: "object",
                        properties: Object.fromEntries(
                          bodyParams.map((p) => [p.name, { type: p.type }])
                        ),
                      },
                    },
                  },
                };
                params = params.filter((p) => p.in !== "body");
              }

              // Get rid of authentication-related fields
              endpoint.parameters = params.filter(
                (p) => !["header", "cookie"].includes(p.in)
              );
            });
          });

          return schema;
        } catch (e) {
          console.error(e);
          console.warn(`Couldn't gather OpenAPI schema at ${url}`);
        }
      })
    )
  ).filter((x) => !!x);

  // Generate Redoc DOM
  const schema = merge_openapi_schemas(schemas);

  if (region !== "fra1")
    schema.servers[0].url = `https://app.${region}.sekoia.io/api`;

  await new Promise((done) =>
    Redoc.init(schema, { hideLoading: true }, openapi_el, done)
  );

  // Gather params for a given {method}+{endpoint}
  function gather_params(method, endpoint) {
    const doc = schema.paths[endpoint][method];
    const params = [];
    // Always prepend API Key field
    params.push({ name: "API Key", in: "header" });
    // ... query params
    params.push(...(doc.parameters || []));

    // ... path params
    for (const pathParam of endpoint.matchAll(/\{([^:\}]+)(:([^:\}]+))?\}/g)) {
      if (!params.find((p) => p.name === pathParam[1] && p.in === "path")) {
        params.push({
          name: pathParam[1],
          in: "path",
          schema: { type: pathParam[3] || "any" },
        });
      }
    }

    // ... body params
    let bodySchema = doc.requestBody?.content?.["application/json"]?.schema;
    if (bodySchema?.["$ref"]) {
      bodySchema = bodySchema?.["$ref"]?.replace(
        /^#\/components\/schemas\//,
        ""
      );
      const body = schema.components?.schemas?.[bodySchema]?.properties || {};
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
    method,
    endpoint,
    params,
    { inline_query_params = true } = {}
  ) {
    method = method.toUpperCase();
    let url = (schema.servers[0]?.url || "") + endpoint;
    const hasBodyParams = !!params?.find((p) => p.in === "body");
    const bodyParams = params?.filter(
      (p) => p.in === "body" && ![undefined, ""].includes(p.value)
    );
    let headers = { Authorization: "Bearer &lt;YOUR_API_KEY&gt;" };
    let body, query_params;

    // Interpolate path params
    url = url.replaceAll(
      /\{([^:\}]+)(:[^\}:]+)?\}/g,
      (m, placeholder) =>
        params.find((p) => p.in === "path" && p.name === placeholder)?.value ||
        ""
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
        } catch {}
      }
      headers["Content-Type"] = "application/json";
      body = JSON.stringify(body);
    }

    return { method, url, headers, body, query_params };
  }

  // Generate a CURL command line for an OpenAPI endpoint
  function generate_curl(method, endpoint, params, el) {
    let { url, headers, body } = generate_query(method, endpoint, params);
    let out = `curl -X ${method.toUpperCase()} ${url}`;
    Object.entries(headers).forEach(([h, v]) => (out += ` -H '${h}:${v}'`));
    if (body) out += ` --data-raw '${body}'`;
    return hljs.highlight(out, { language: "bash" }).value;
  }

  // Generate a Python example code for an OpenAPI endpoint
  function generate_python(method, endpoint, params, el) {
    let { url, headers, body, query_params } = generate_query(
      method,
      endpoint,
      params,
      {
        inline_query_params: false,
      }
    );
    let out = `import requests
import json

result = requests.request(
    "${method.toUpperCase()}",
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
    return hljs.highlight(out, { language: "python" }).value;
  }

  // Generate a Javascript example code for an OpenAPI endpoint
  function generate_js(method, endpoint, params, el) {
    let { url, headers, body } = generate_query(method, endpoint, params);
    let out = `await fetch("${url}", {
    method: "${method.toUpperCase()}",
`;
    if (body) {
      out += `    body: \`${JSON.stringify(
        JSON.parse(body),
        null,
        4
      ).replaceAll("\n", "\n    ")}\`,\n`;
    }
    if (headers) {
      out += `    headers: ${JSON.stringify(headers, null, 4).replaceAll(
        "\n",
        "\n    "
      )},\n`;
    }

    out += `}).then(res=>res.json())
`;
    return hljs.highlight(out, { language: "javascript" }).value;
  }

  async function execute_endpoint(method, endpoint, params, el) {
    document
      .querySelectorAll(".try-it-wrapper button")
      .forEach((b) => b.setAttribute("disabled", ""));

    // Spinner
    el.querySelector(".results")?.remove();
    const results = document.createElement("div");
    results.className = "results";
    results.innerHTML = `<div class="ui-spinner"></div>`;
    el.appendChild(results);

    let { url, headers, body } = generate_query(method, endpoint, params);
    headers = {
      ...headers,
      accept: "application/json",
      Authorization: `Bearer ${_APIKEY}`,
    };

    let status = "success";
    error = null;
    const res = await fetch(url, { method, body, headers })
      .then(async (x) => {
        if (x.status >= 400) {
          status = "error";
          return `Error ${x.status}\n${await x.text()}}`;
        }
        return JSON.stringify(await x.json(), null, 4);
      })
      .catch((e) => {
        status = "error";
        return e;
      });

    results.innerHTML = `<h3>Response</h3><pre class='output ${status}'></pre>`;
    results.querySelector("pre").innerText = res;

    document
      .querySelectorAll(".try-it-wrapper button")
      .forEach((b) => b.removeAttribute("disabled"));
  }

  // Generate a TryIt form
  function generate_try_it(e) {
    const method = e.querySelector(".sc-EgOXT").innerText.trim().toLowerCase();
    const endpoint = e.querySelector(".sc-ejfMa-d").innerText.trim();
    const el = document.createElement("form");
    el.classList.add("try-it-wrapper");

    const params = gather_params(method, endpoint);

    function get_params_data() {
      const data = [...params];
      el.querySelectorAll("input").forEach((input) => {
        const p = data.find((x) => x.name === input.name);
        if (p) {
          p.value = input.value;
        }
      });
      return data;
    }

    el.appendChild(
      $element(
        "div",
        `
          <div class='params headers'><h3>Headers</h3></div>
          <div class='params path-params'><h3>Path parameters</h3></div>
          <div class='params query-params'><h3>Query parameters</h3></div>
          <div class='params body-params'><h3>Body parameters</h3></div>
        `,
        "parameters"
      )
    );
    const [elHeaders, elPathParams, elQueryParams, elBodyParams] = Array.from(
      el.querySelectorAll(".parameters > .params")
    );

    // Generate params inputs
    params?.forEach((p) => {
      const div = document.createElement("div");
      div.className = "param";
      const input = document.createElement("input");

      input.name = p.name;
      input.title = p.name;
      if (p.name === "API Key") {
        input.type = "password";
        input.value = _APIKEY;
      }

      const type = p.schema?.anyOf?.[0]?.type || p.schema?.type;
      if (type && type !== "any") {
        div.innerHTML = `<label>${p.name} (${type})</label>`;
      } else {
        div.innerHTML = `<label>${p.name}</label>`;
      }

      if (p.in === "query") elQueryParams.appendChild(div);
      else if (p.in === "path") elPathParams.appendChild(div);
      else if (p.in === "body") elBodyParams.appendChild(div);
      else if (p.in === "header") elHeaders.appendChild(div);
      div.appendChild(input);

      // Update cURL when input changes
      input.oninput = () => {
        curl.innerHTML = generate_curl(method, endpoint, get_params_data(), el);
        python.innerHTML = generate_python(
          method,
          endpoint,
          get_params_data(),
          el
        );
        js.innerHTML = generate_js(method, endpoint, get_params_data(), el);

        // Propagate API KEY to all endpoints form
        if (p.name === "API Key") {
          document
            .querySelectorAll(
              ".try-it-wrapper input[type=password][name='API Key']"
            )
            .forEach((elt) => (_APIKEY = elt.value = input.value));
        }
      };
    });

    [elBodyParams, elQueryParams, elPathParams].forEach((e) => {
      if (Array.from(e.querySelectorAll("&>div"))?.length === 0) e.remove();
    });

    // Code examples
    el.appendChild($element("h3", "Code examples"));
    el.appendChild(
      $element(
        "div",
        `
        <ul role="tablist">
          <li class="tab-success selected" role="tab" aria-selected="true" aria-disabled="false">cURL</li>
          <li class="tab-success" role="tab" aria-selected="false" aria-disabled="false">Python</li>
          <li class="tab-success" role="tab" aria-selected="false" aria-disabled="false">Javascript</li>
        </ul>
        <div>
          <pre class="curl selected"><code class="language-bash"></code></pre>
          <pre class="python"><code class="language-python"></code></pre>
          <pre class="javascript"><code class="language-javascript"></code></pre>
        </div>
    `,
        "code-examples"
      )
    );

    const [curl, python, js] = Array.from(
      el.querySelectorAll(".code-examples > div > pre > code")
    );

    curl.innerHTML = generate_curl(method, endpoint, get_params_data(), el);
    python.innerHTML = generate_python(method, endpoint, get_params_data(), el);
    js.innerHTML = generate_js(method, endpoint, get_params_data(), el);

    Array.from(el.querySelectorAll(".code-examples > ul > li")).forEach(
      (e, i) => {
        e.onclick = () => {
          el.querySelectorAll(".code-examples > ul > li").forEach((e) =>
            e.classList.remove("selected")
          );
          el.querySelectorAll(".code-examples > div > pre").forEach((e) =>
            e.classList.remove("selected")
          );
          e.classList.add("selected");
          Array.from(el.querySelectorAll(".code-examples > div > pre"))[
            i
          ].classList.add("selected");
        };
      }
    );

    // Send button
    const btn = document.createElement("button");
    btn.type = "submit";
    btn.innerText = "Send";
    el.onsubmit = (e) => {
      execute_endpoint(method, endpoint, get_params_data(), el);
      e.stopPropagation();
      e.preventDefault();
    };
    el.append(btn);
    return el;
  }

  // Instrument Redoc DOM with Try it extension
  document.querySelectorAll("main .bOFhJE").forEach((e) => {
    function switchTab(tab) {
      tabs.querySelectorAll("li").forEach((e) => e.classList.remove("active"));
      tab.classList.add("active");
    }

    e.classList.add("examples");
    const tabs = document.createElement("ul");
    tabs.className = "tabs";
    let tab;
    tabs.appendChild((tab = document.createElement("li")));
    tab.innerText = "Samples";
    tab.classList.add("active");
    tab.onclick = (ev) => {
      switchTab(ev.target);
      e.classList.remove("mode-try-it");
    };
    tabs.appendChild((tab = document.createElement("li")));
    tab.innerText = "Try it";
    tab.classList.add("try-it");
    tab.onclick = (ev) => {
      switchTab(ev.target);
      e.classList.add("mode-try-it");
      if (!e.querySelector(".try-it-wrapper")) {
        e.appendChild(generate_try_it(e));
      }
    };
    e.prepend(tabs);
    e.querySelectorAll(".sc-iGgWBj > div").forEach((e) => {
      if (e.querySelector("h3")?.innerText.includes("Response samples"))
        e.classList.add("response-samples");
      if (e.querySelector("h3")?.innerText.includes("Request samples"))
        e.classList.add("request-samples");
    });
  });

  // Custom left menu additions
  const menu = document.querySelector(".redoc-wrap .menu-content");
  const region_picker = $element(
    "div",
    `
      <label>Select region</label>
      <select>
        ${REGIONS.map((r) => `<option>${r}</option>`).join("")}
      </select>
  `,
    "region-picker"
  );

  menu
    .querySelector(".scrollbar-container")
    .parentNode.insertBefore(
      region_picker,
      menu.querySelector(".scrollbar-container")
    );
  region_picker.onchange = () => {
    document.location.search = `region=${
      region_picker.querySelector("select").selectedOptions[0].innerText
    }`;
  };
  region_picker.querySelectorAll("option").forEach((e) => {
    if (
      ((
        new URLSearchParams(location.search).get("region") || "fra1"
      ).toLowerCase() || "fra1") === (e.innerText.toLowerCase() || "fra1")
    )
      e.setAttribute("selected", true);
  });
}

window.addEventListener("load", init_openapi_documentation);
