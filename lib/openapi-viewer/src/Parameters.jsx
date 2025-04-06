import { Chevron } from "./utils"
import { resolveSchema } from "./OpenAPIViewer"

/** A Vue component to render an API endpoint's parameters */
export const Parameters = {
    props: ["endpoint"],
    setup(props) {
        return () => {
            const { parameters, requestBody } = props.endpoint
            if (!parameters?.length > 0 && !requestBody) return <div class='no-parameters'>No parameters</div>

            const pathParameters = parameters.filter(p => p.in === "path")
            const queryParameters = parameters.filter(p => p.in === "query")
            const bodyParameters = parameters.filter(p => p.in === "body")

            // Incorporate requestBody to body parameters list
            let bodySchema = requestBody?.content?.["application/json"]?.schema
            if (bodySchema) bodySchema = resolveSchema(bodySchema)
            if (bodySchema?.properties) bodyParameters.push(...Object.entries(bodySchema.properties).map(([name, p]) => {
                p.name = name;
                return p
            }))

            return <div class='parameters'>
                {pathParameters?.length > 0 && <>
                    <h6>Path parameters</h6>
                    {Properties(pathParameters)}
                </>}
                {queryParameters?.length > 0 && <>
                    <h6>Query parameters</h6>
                    {Properties(queryParameters)}
                </>}
                {bodyParameters?.length > 0 && <>
                    <h6>Body parameters</h6>
                    {Properties(bodyParameters)}
                </>}
            </div>
        }
    }
}

/** Check if a OpenAPI property has constraints set */
export function hasConstraints(p) {
    if (p.minimum !== undefined) return true
    if (p.maximum !== undefined) return true
    if (p.minLength !== undefined) return true
    if (p.maxLength !== undefined) return true
    if (p.enum?.[0]) return true
    return false
}

/** Vue component to render a table of OpenAPI properties */
export const Properties = (p) => <div class="parameter-overflow-table"><table>
    <tr>
        <th>Name</th>
        <th></th>
        <th>Type</th>
        <th>{p?.filter(p => hasConstraints(p))?.length > 0 && "Constraints"}</th>
        <th>{p?.filter(p => p.default !== undefined)?.length > 0 && "Default value"}</th>
        <th width="100%">{p?.filter(p => !!p.description) && "Description"}</th>
    </tr>
    {p?.map(Property)}
</table></div>


/**
 * Vue component to render a single OpenAPI property
 * {prop}: the property
 * {override}: optional (non-reactive) overrides merged with the prop at render time
 * {stack}: a stack to prevent infinite recursion for cyclicly-nested property schemas
 * {level}: 0-based nesting level
 */
export const Property = (prop, override = {}, stack = null, level = 0) => {
    const name = override.name || prop.name || prop.title?.toLowerCase()
    delete override.name

    if (!prop.type) {
        if (typeof (prop.default) === "string") prop.type = "string"
    }

    if (prop.$ref) {
        if (stack === null) stack = {}
        if (stack?.[prop.$ref]) return {}
        stack[prop.$ref] = true
        return Property(resolveSchema(prop.$ref), { name }, stack, level)
    }

    if (prop.anyOf?.length > 0 || prop.schema?.anyOf?.length > 0) {
        for (const alt of (prop.anyOf || prop.schema.anyOf)) {
            if (alt.type !== 'null') return Property(alt, { name }, stack, level)
        }
    }

    const p = { ...prop, ...override }
    let isExpandable = p.type === 'array' || p.items?.type === 'object' || p.type === "object"

    let type = p.type
    if (type === "array") {
        if (!p.items?.type && p.items?.$ref) p.items.type = "object"
        if (p.items?.type) type += ` of ${p.items?.type}s`
        if (p.items?.format) type += ` (${p.items?.format})`
    }
    if (!type) {
        if (p.enum?.[0]) type = "enum"
        else if (p.schema?.type) return Property(prop, p.schema, stack, level)
        else {
            console.warn("No type for ", p)
            type = "object"
        }
    }
    if (type === "string" && p.enum?.[0]) type += " (enum)"


    let subProperties = p.properties
    if (isExpandable) {
        if (p.items?.properties) subProperties = p.items?.properties
        else if (p.items?.$ref) subProperties = resolveSchema(p.items?.$ref)?.properties
    }

    // If the property is expandable but has no sub-properties, display it
    // as a non-expandable JSON object/array
    if (isExpandable && !Object.keys(subProperties || {})?.length > 0) {
        isExpandable = false
        if (type === "object") type = "json"
        else type = "json array"
    }

    return <><tr
        class='param' class={`level-${level}`}
        class={{ expandable: isExpandable, expanded: !!prop.expanded }}
        onClick={!!isExpandable && (() => prop.expanded = !prop.expanded)}
    >
        <td class='name'
            style={{ paddingLeft: (level * 36) + 6 + "px" }}
        >
            {isExpandable && Chevron}
            {name}
        </td>
        <td>{p.required ? <span class="required">* required</span> : <span class="optional">optional</span>}</td>
        <td class="type">{type || "-"} {!!p.format && <>({p.format})</>}
        </td>
        <td class="constraints">
            <div>
                {p.minimum !== undefined && <span class='bound min'>≥ {p.minimum}</span>}
                {p.maximum !== undefined && <span class='bound max'>≤ {p.maximum}</span>}
                {p.minLength !== undefined && <span class='bound min'>len ≥ {p.minLength}</span>}
                {p.maxLength !== undefined && <span class='bound max'>len ≤ {p.maxLength}</span>}
                {p.enum?.[0] && p.enum.filter(v => v !== null).map(v => <span class='bound'>{`${v}`}</span>)}
            </div>
        </td>
        <td>{p.default !== undefined && `${p.default}` !== "[object Object]" && p.default} </td>
        <td class="description" width="100%">{p.description}</td>
    </tr>
        {prop.expanded && level < 6 && Object.entries(subProperties || {}).map(([name, p]) => Property(p, { name }, null, level + 1))}
    </>
}