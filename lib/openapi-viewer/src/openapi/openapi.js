import { convert_swagger_to_openapi } from "./swagger-converter";
import { object_walk } from "./util";

/** Merge a list of OpenAPI {schemas} into a single OpenAPI 3.1-compliant schema */
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
  };

  return schema;
}

export async function fetch_and_merge_openapi_schemas(urls) {
  // Convert legacy Swagger 2.0 schemas to OpenAPI 3.1
  const schemas = (
    await Promise.all(
      urls.map(async (url) => {
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
  return merge_openapi_schemas(schemas);
}
