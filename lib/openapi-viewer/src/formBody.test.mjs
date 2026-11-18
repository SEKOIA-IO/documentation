import assert from "node:assert/strict"
import { describe, it } from "node:test"

import {
    buildFormBody,
    curlFormArgs,
    FILE_PLACEHOLDER,
    formEntries,
    isFileField,
    isFormMediaType,
    jsFormBody,
    pythonFormArgs,
} from "./formBody.mjs"

const MULTIPART = "multipart/form-data"
const URLENCODED = "application/x-www-form-urlencoded"
const csv = new File(["a,b\n1,2\n"], "dataset.csv", { type: "text/csv" })

describe("isFormMediaType", () => {
    it("is true for form media types only", () => {
        assert.equal(isFormMediaType(MULTIPART), true)
        assert.equal(isFormMediaType(URLENCODED), true)
        assert.equal(isFormMediaType("application/json"), false)
        assert.equal(isFormMediaType(undefined), false)
    })
})

describe("isFileField", () => {
    it("recognises a required and an optional file", () => {
        const file = { type: "string", contentMediaType: "application/octet-stream" }
        assert.equal(isFileField(file), true)
        assert.equal(isFileField({ anyOf: [file, { type: "null" }] }), true)
        assert.equal(isFileField({ anyOf: [{ type: "string" }, { type: "null" }] }), false)
    })
})

describe("formEntries", () => {
    it("skips empty text fields but keeps file fields", () => {
        const params = [
            { name: "name", value: "assets" },
            { name: "community_uuid", value: "" },
            { name: "file", file: true, value: undefined },
        ]
        assert.deepEqual(formEntries(params), [
            { name: "name", value: "assets", file: false },
            { name: "file", value: undefined, file: true },
        ])
    })
})

describe("buildFormBody", () => {
    it("builds FormData with the chosen file", () => {
        const body = buildFormBody(MULTIPART, [
            { name: "name", value: "assets", file: false },
            { name: "file", value: csv, file: true },
        ])
        assert.ok(body instanceof FormData)
        assert.equal(body.get("name"), "assets")
        assert.equal(body.get("file").name, "dataset.csv")
    })

    it("leaves out a file field with no file chosen", () => {
        const body = buildFormBody(MULTIPART, [{ name: "file", value: undefined, file: true }])
        assert.equal(body.has("file"), false)
    })

    it("builds URLSearchParams for a URL-encoded body", () => {
        const body = buildFormBody(URLENCODED, [{ name: "q", value: "a b", file: false }])
        assert.ok(body instanceof URLSearchParams)
        assert.equal(body.toString(), "q=a+b")
    })
})

describe("snippets", () => {
    const entries = [
        { name: "name", value: "it's", file: false },
        { name: "file", value: csv, file: true },
    ]

    it("curl sends multipart fields with -F, quoting values", () => {
        assert.equal(curlFormArgs(MULTIPART, entries), ` -F 'name=it'\\''s' -F 'file=@dataset.csv'`)
    })

    it("curl shows a placeholder for a file not chosen", () => {
        assert.equal(curlFormArgs(MULTIPART, [{ name: "file", file: true }]), ` -F 'file=@${FILE_PLACEHOLDER}'`)
    })

    it("curl sends URL-encoded fields with --data-urlencode", () => {
        assert.equal(curlFormArgs(URLENCODED, [{ name: "q", value: "a b", file: false }]), ` --data-urlencode 'q=a b'`)
    })

    it("python sends text fields as data and files as files", () => {
        assert.equal(
            pythonFormArgs(MULTIPART, entries),
            `    data={\n        "name": "it's"\n    },\n    files={\n        "file": open("dataset.csv", "rb"),\n    },\n`,
        )
    })

    it("javascript builds a FormData body", () => {
        assert.equal(
            jsFormBody(MULTIPART, entries),
            `const body = new FormData()\nbody.append("name", "it's")\n` +
            `body.append("file", file) // a File or Blob, e.g. from <input type="file">\n`,
        )
    })

    it("javascript builds a URLSearchParams body", () => {
        assert.equal(
            jsFormBody(URLENCODED, [{ name: "q", value: "a b", file: false }]),
            `const body = new URLSearchParams({\n    "q": "a b"\n})\n`,
        )
    })
})
