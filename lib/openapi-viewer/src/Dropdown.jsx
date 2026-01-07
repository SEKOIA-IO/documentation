import { ref } from "vue";
import { useTippy } from "vue-tippy";
import 'tippy.js/animations/shift-away.css';
import "./Dropdown.scss"

/** A Dropdown Vue component */
export const Dropdown = {
    props: ["button", "class", "content"],
    setup(props, { slots }) {
        const target = ref(null)
        const { show } = useTippy(target, {
            trigger: "manual",
            interactive: true,
            placement: "bottom-start",
            offset: [0, 4],
            animation: "shift-away",
            maxWidth: 'none',
            content: {
                setup() {
                    return () => <div class={props.class}>
                        {props.content}
                    </div>
                }
            },
        });

        return () => {
            return <button ref={target} class='dropdown-button' class={props.class} onClick={() => show()}>
                {props.button}
            </button>
        }
    }
}