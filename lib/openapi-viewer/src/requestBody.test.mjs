import assert from "node:assert/strict"
import { describe, it } from "node:test"

import { getRequestBodyContent, isFileSchema } from "./requestBody.mjs"

const ref = { $ref: "#/components/schemas/Body" }

describe("getRequestBodyContent", () => {
    it("returns the JSON schema", () => {
        const body = { content: { "application/json": { schema: ref } } }
        assert.deepEqual(getRequestBodyContent(body), { mediaType: "application/json", schema: ref })
    })

    it("falls back to multipart/form-data", () => {
        const body = { required: true, content: { "multipart/form-data": { schema: ref } } }
        assert.deepEqual(getRequestBodyContent(body), { mediaType: "multipart/form-data", schema: ref })
    })

    it("falls back to application/x-www-form-urlencoded", () => {
        const body = { content: { "application/x-www-form-urlencoded": { schema: ref } } }
        assert.deepEqual(getRequestBodyContent(body), { mediaType: "application/x-www-form-urlencoded", schema: ref })
    })

    it("prefers JSON when several media types are declared", () => {
        const json = { type: "object" }
        const body = { content: { "multipart/form-data": { schema: ref }, "application/json": { schema: json } } }
        assert.deepEqual(getRequestBodyContent(body), { mediaType: "application/json", schema: json })
    })

    it("returns null for an unsupported media type or no body", () => {
        assert.equal(getRequestBodyContent({ content: { "text/plain": { schema: { type: "string" } } } }), null)
        assert.equal(getRequestBodyContent(undefined), null)
    })
})

describe("isFileSchema", () => {
    it("recognises an OpenAPI 3.1 file (FastAPI UploadFile)", () => {
        assert.equal(isFileSchema({ type: "string", contentMediaType: "application/octet-stream" }), true)
    })

    it("recognises an OpenAPI 3.0 binary string", () => {
        assert.equal(isFileSchema({ type: "string", format: "binary" }), true)
    })

    it("does not flag other strings", () => {
        assert.equal(isFileSchema({ type: "string" }), false)
        assert.equal(isFileSchema({ type: "string", format: "uuid" }), false)
        assert.equal(isFileSchema({ type: "object", contentMediaType: "application/json" }), false)
        assert.equal(isFileSchema(undefined), false)
    })
})
