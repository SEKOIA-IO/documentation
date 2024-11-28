/** Vue component to render documentation for an error code */
export const Error = ({ code, response }) => <div class="response error">
    <span class='status-code'>{code}</span>
    <div>{response?.description}</div>
</div>