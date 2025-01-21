import { marked } from "marked"
import DOMPurify from "dompurify"

/** A Vue component to render (sanitized) markdown descriptions */
export const Markdown = ({ src }) => <div class="description" v-html={DOMPurify.sanitize(marked.parse(src || ""))} />
