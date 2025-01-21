/** A Vue component using highlightjs for syntax highlighting of code blocks */
export const Code = ({ src, lang }) => <highlightjs language={lang} code={src} />
