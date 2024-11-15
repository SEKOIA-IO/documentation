// Swagger 2.0 to OpenAPI 3.1 in-browser conversion

function object_walk(obj, fn, replace = false) {
  if (Array.isArray(obj)) {
    if (replace) return obj.map((x, i) => fn(i, x));
    else obj.forEach((x, i) => fn(i, x));
  }
  if (typeof obj === "object") {
    for (const k in obj) {
      const r = fn(k, obj[k]);
      if (replace) obj[k] = r;
      object_walk(obj[k], fn, replace);
    }
  }
}

function convert_swagger_to_openapi(swagger) {
  if (swagger.swagger !== "2.0") throw new Error("Not a swagger spec");

  object_walk(
    swagger,
    (k, v) => {
      if (k === "$ref" && typeof v === "string") {
        return v.replace(/^#\/definitions\//, "#/components/schemas/");
      }
      return v;
    },
    true
  );

  const openapi = {
    openapi: "3.1.0",
    info: {
      ...swagger.info,
    },
    servers: [
      {
        url: "https://api.sekoia.io",
        description: "Sekoia.io API",
      },
    ],
    paths: Object.fromEntries(
      Object.entries(swagger.paths).map(([path, spec]) => {
        const commonParams = spec.parameters;
        Object.entries(spec).forEach(([method, endpoint]) => {
          if (
            !["get", "post", "put", "delete", "patch"].includes(
              method.toLowerCase()
            )
          )
            return;

          if (endpoint.parameters) {
            // Enforce non-querystring params for every methods other than GET
            if (method !== "get") {
              for (const p of endpoint.parameters) {
                if (p.in === "query") p.in = "body";
              }
            }
          }

          // Incorporate common params defined at path level
          if (commonParams) {
            endpoint.parameters = [
              ...(endpoint.parameters || []),
              ...commonParams,
            ];
          }

          Object.entries(endpoint.responses).forEach(([code, res]) => {
            if (!res.schema) return;
            res.content = {
              "application/json": { schema: res.schema },
            };
            delete res.schema;
          });
        });
        return [swagger.basePath + path, spec];
      })
    ),
    components: {
      schemas: swagger.definitions,
    },
  };
  return openapi;
}
