/**
 * Media types of a request body whose schema properties are shown as body
 * parameters, in order of precedence.
 */
export const BODY_MEDIA_TYPES = [
    "application/json",
    "multipart/form-data",
    "application/x-www-form-urlencoded",
]

/**
 * Return the {mediaType, schema} of an OpenAPI {requestBody}, for the first
 * supported media type it declares, or null when it declares none.
 * The schema is returned as declared: references are not resolved.
 */
export function getRequestBodyContent(requestBody) {
    for (const mediaType of BODY_MEDIA_TYPES) {
        const schema = requestBody?.content?.[mediaType]?.schema
        if (schema) return { mediaType, schema }
    }
    return null
}

/**
 * Whether an OpenAPI {schema} describes a file: a binary string in OpenAPI 3.0
 * (`format: binary`), or a string with a `contentMediaType` in OpenAPI 3.1,
 * which FastAPI emits for `UploadFile`.
 */
export function isFileSchema(schema) {
    if (schema?.type !== "string") return false
    return schema.format === "binary" || !!schema.contentMediaType
}
