import { reactive, ref, watchEffect } from "vue";
import { useTippy } from "vue-tippy";

/** A ComboxBox dropdown button with multiselect options */
export const Filter = {
    props: ["items", "selection", "onClick", "separator", "placeholder"],
    setup(props, { slots }) {
        const target = ref(null)
        const { show } = useTippy(target, {
            trigger: "manual",
            interactive: true,
            placement: "bottom-start",
            offset: [0, 4],
            content: {
                setup() {
                    const data = reactive({ search: "", items: [...props.items || []] })
                    watchEffect(() => {
                        data.items = props.items?.filter(x => !data.search?.length || x.toLowerCase().includes(data.search.toLowerCase()))
                    })

                    return () => <div class="filter-dropdown">
                        <input class="doc-input" placeholder={props.placeholder} onInput={({ target }) => data.search = target.value} />
                        <ul>
                            {data.items?.map(x => <li class="item" onClick={() => props.onClick(x)}>
                                <input type="checkbox" checked={!!props.selection?.includes?.(x)} /><label>{x}</label>
                            </li>)}
                        </ul>
                    </div>
                }
            },
        });

        return () => {
            return <div class="doc-filter">
                <button ref={target} class='doc-input' onClick={() => show()}>
                    {slots?.default?.()}
                </button>

                <b>{props.selection?.length > 0 && <>{props.selection?.length} selected</>}</b>
            </div>
        }
    }
}