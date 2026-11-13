import { isFileSchema } from "./requestBody.mjs"

/** Shown in code snippets in place of a file the user has not chosen */
export const FILE_PLACEHOLDER = "<path/to/file>"

/** Whether a request body of {mediaType} is sent as form fields instead of JSON */
export function isFormMediaType(mediaType) {
    return mediaType === "multipart/form-data" || mediaType === "application/x-www-form-urlencoded"
}

/** Whether a form field {schema} is a file, including an optional one (`anyOf: [file, null]`) */
export function isFileField(schema) {
    return isFileSchema(schema) || !!schema?.anyOf?.some(isFileSchema)
}

/**
 * Return the {name, value, file} entries of a form body from its body {params}.
 * Text fields left empty are skipped; file fields are always kept, so that the
 * code snippets show how to send them.
 */
export function formEntries(params) {
    return params
        .filter(p => p.file || ![undefined, ""].includes(p.value))
        .map(p => ({ name: p.name, value: p.value, file: !!p.file }))
}

/** Return the body `fetch` sends for form {entries}: FormData, or URLSearchParams */
export function buildFormBody(mediaType, entries) {
    if (mediaType === "multipart/form-data") {
        const body = new FormData()
        for (const { name, value, file } of entries) {
            if (file) {
                if (value instanceof Blob) body.append(name, value, value.name)
            } else body.append(name, `${value}`)
        }
        return body
    }
    return new URLSearchParams(entries.filter(e => !e.file).map(e => [e.name, `${e.value}`]))
}

function fileName(value) {
    return value?.name || FILE_PLACEHOLDER
}

function textFields(entries) {
    return Object.fromEntries(entries.filter(e => !e.file).map(e => [e.name, `${e.value}`]))
}

/** Quote {s} as a single POSIX shell word */
function shellQuote(s) {
    return `'${s.replaceAll("'", `'\\''`)}'`
}

function indent(s) {
    return s.replaceAll("\n", "\n    ")
}

/** curl arguments sending form {entries} */
export function curlFormArgs(mediaType, entries) {
    if (mediaType === "multipart/form-data") {
        return entries.map(({ name, value, file }) =>
            ` -F ${shellQuote(file ? `${name}=@${fileName(value)}` : `${name}=${value}`)}`
        ).join("")
    }
    return entries.filter(e => !e.file).map(({ name, value }) => ` --data-urlencode ${shellQuote(`${name}=${value}`)}`).join("")
}

/** Keyword arguments of `requests.request()` sending form {entries} */
export function pythonFormArgs(mediaType, entries) {
    let out = ""
    const data = textFields(entries)
    if (Object.keys(data).length > 0) out += `    data=${indent(JSON.stringify(data, null, 4))},\n`
    const files = mediaType === "multipart/form-data" ? entries.filter(e => e.file) : []
    if (files.length > 0) {
        out += `    files={\n`
        for (const { name, value } of files) {
            out += `        ${JSON.stringify(name)}: open(${JSON.stringify(fileName(value))}, "rb"),\n`
        }
        out += `    },\n`
    }
    return out
}

/** Javascript statements building the `body` const that sends form {entries} */
export function jsFormBody(mediaType, entries) {
    if (mediaType === "multipart/form-data") {
        let out = "const body = new FormData()\n"
        for (const { name, value, file } of entries) {
            out += file
                ? `body.append(${JSON.stringify(name)}, file) // a File or Blob, e.g. from <input type="file">\n`
                : `body.append(${JSON.stringify(name)}, ${JSON.stringify(`${value}`)})\n`
        }
        return out
    }
    return `const body = new URLSearchParams(${JSON.stringify(textFields(entries), null, 4)})\n`
}
