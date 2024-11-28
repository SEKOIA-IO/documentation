import { reactive } from "vue"
import { Code } from "./Code"
import { Dropdown } from "./Dropdown"
import { TryIt } from "./TryIt"
import './Examples.scss'
import { Chevron } from "./utils"
import { data, resolveSchema } from "./OpenAPIViewer"


/** A Vue component to render sample requests and response payloads */
export const Examples = {
    props: ["endpoint", "schema"],
    setup(props) {
        const ui = reactive({ tab: "samples" })

        const fullURL = (data.schema?.servers?.[0]?.url || "") + props.endpoint.path

        let bodySchema = props.endpoint.requestBody?.content?.["application/json"]?.schema
        if (bodySchema) bodySchema = resolveSchema(bodySchema)

        let responseSchema = null
        for (const code in props.endpoint.responses) {
            const s = props.endpoint.responses[code]?.content?.["application/json"]?.schema
            if (code < 400 && s) {
                responseSchema = resolveSchema(s)
                break;
            }
        }

        return () => {
            const { method, path } = props.endpoint
            return <div class='examples'>
                <nav>
                    <li class={{ active: ui.tab === "samples" }} onClick={() => ui.tab = "samples"}>Samples</li>
                    <li class={{ active: ui.tab === "tryit" }} onClick={() => ui.tab = "tryit"}>Try it</li>
                </nav>
                {ui.tab === "tryit" ? <TryIt endpoint={props.endpoint} /> :
                    <div class="samples">
                        <Dropdown class='path'
                            button={<>
                                <span class="method" class={method}>{method}</span>
                                <div>{path}</div>
                                {Chevron}
                            </>}
                            content={fullURL}
                        />

                        {!!bodySchema &&
                            <>
                                <h3>Request samples</h3>
                                <Code lang="json" src={generateExamplePayload(bodySchema)} />
                            </>
                        }
                        {!!responseSchema && <>
                            <h3>Response samples</h3>
                            <Code lang="json" src={generateExamplePayload(responseSchema)} />
                        </>}
                    </div>}
            </div>
        }
    }
}

/** Generate an example payload for the given endpoint's {type} and {properties} */
export function generateExamplePayload({ type, properties } = {}) {
    const sample = {}
    for (const name in properties) {
        const p = properties[name]
        sample[name] = generateExampleValue(p, name)
    }
    return JSON.stringify(sample, null, 2)
}

/** Generate an example value for the given field {p} */
export function generateExampleValue(p, name = "", stack = null) {
    let v = null;

    if (!p) return null;

    if (p.$ref) {
        if (stack === null) stack = {}
        if (stack?.[p.$ref]) return {}
        stack[p.$ref] = true
        return generateExampleValue(resolveSchema(p.$ref), name, stack)
    }

    if (p.anyOf?.length > 0) {
        for (const alt of p.anyOf) {
            if (alt.type !== 'null') return generateExampleValue(alt, name, stack)
        }
    }

    if (p.type === "integer") v = p.minimum || 0
    else if (p.type === "number") v = (p.minimum || 0.0) + 0.0
    else if (p.type === "string") {
        if (name === "description") v = `This is a *description*`
        else if (["uuid", "community_uuid"].includes(name)) v = crypto.randomUUID()
        else if (name === "email") v = "johndoe@example.com"
        else if (p.format === "uuid") v = crypto.randomUUID()
        else if (p.format === "date-time") v = (new Date()).toISOString()
        else if (p.format === "date") v = (new Date()).toDateString()
        else if (p.default) v = p.default
        else if (p.enum?.[0]) v = p.enum?.[0]
        else v = `${name.toLowerCase().replace(/_/g, " ")}`
    }
    else if (p.type === "boolean") v = true
    else if (p.type === "array") {
        v = [generateExampleValue(p.items, name, stack)]
    } else if (p.type === "object") {
        if (p.properties === undefined) v = {}
        else {
            v = {}
            for (const k in p.properties) {
                v[k] = generateExampleValue(p.properties[k], k, stack)
            }
        }
    }

    // Fallbacks
    if (v === null) {
        if (p.schema?.type || p.schema?.anyOf) return generateExampleValue({ ...p.schema, ...p }, name, stack)
        if (p.schema?.$ref) return generateExampleValue(resolveSchema(p.schema.$ref), name, stack)
        else return null
    }

    return v
}