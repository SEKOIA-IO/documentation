import { Property, hasConstraints } from "./Parameters";
import { resolveSchema } from "./OpenAPIViewer"

/** Vue component to render an API endpoint's responses */
export const Response = ({ code, response }) => <div class="response ok">
    {response?.content ? Object.entries(response?.content || {})?.map(([mime, schema]) => <>
        <div class='with-model'>
            <span class='status-code-ok'>{code}</span>
            <div class='description'>{response?.description}</div>
            <div class='mime'>{mime}</div>
        </div>
        {ResponseModel(schema)}
    </>) :
        (!!response.description && <div>
            <span class='status-code-ok'>{code}</span>
            <div class='description'>{response?.description}</div>
        </div>)
    }

</div>

/** Vue component to render an OpenAPI response schema */
export const ResponseModel = (schema) => {
    const { properties = {}, required } = resolveSchema(schema)
    if (!Object.entries(properties)?.length > 0) return null;
    return <table class="response-model">
        <tr>
            <th>Name</th>
            <th></th>
            <th>Type</th>
            <th>{Object.values(properties)?.filter(p => hasConstraints(p))?.length > 0 && "Constraints"}</th>
            <th>{Object.values(properties)?.filter(p => p.default !== undefined)?.length > 0 && "Default value"}</th>
            <th width="100%">{Object.values(properties)?.filter(p => !!p.description) && "Description"}</th>
        </tr>
        {Object.entries(properties).map(([name, p]) => Property(p, { name, required: required?.includes(name) }))}
    </table>
}