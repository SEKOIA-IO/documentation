import { object_walk } from "./util";

/** Swagger 2.0 to OpenAPI 3.1 in-browser conversion */
export function convert_swagger_to_openapi(swagger) {
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

          if (endpoint.parameters && endpoint.parameters.length > 0) {
            // Extract body parameters for non-GET methods
            const bodyParams = endpoint.parameters.filter(
                  p =>
                    method.toLowerCase() !== "get" &&
                    !p.name.includes("[") &&
                    !p.name.includes("]") &&
                    !(typeof p.description === "string" && p.description.toLowerCase().includes("filter"))
                );

            // Remove body parameters from the endpoint parameters
            endpoint.parameters = endpoint.parameters.filter(
              p => !bodyParams.includes(p)
            );

            // Incorporate common params defined at path level
            if (commonParams) {
              endpoint.parameters = [
                ...(endpoint.parameters || []),
                ...commonParams,
              ];
            }

            // Convert body parameters to OpenAPI requestBody
            if (bodyParams && bodyParams.length > 0) {
              endpoint.requestBody = {
                required: true,
                content: {
                  "application/json": {
                    schema: {
                      type: "object",
                      properties: Object.fromEntries(
                        bodyParams.map(p => [p.name, p])
                      ),
                      required: bodyParams.filter(p => p.required).map(p => p.name)
                    },
                  },
                },
              };
            }
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
