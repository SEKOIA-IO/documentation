
/** Encode the given {tag} for use in HTML anchors */
export const tagEncode = tag => tag.replaceAll(" ", "-").toLowerCase()

export const Chevron = <svg class="nav-chevron" version="1.1" viewBox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0" aria-hidden="true"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

export function debounce(func, wait) {
    let timeout;
    return function (...args) {
        const context = this;
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func.apply(context, args);
        }, wait);
    };
}

let suppressScrollSpyUntil = 0

/** True while a programmatic scroll from {scrollToAnchor} is still in flight */
export function isScrollSpySuppressed() {
    return Date.now() < suppressScrollSpyUntil
}

export function scrollToAnchor(hash) {
    const targetId = hash.substring(1)
    let el = document.getElementById(targetId)
    if (!el) {
        const normalizedTargetId = targetId.toLowerCase()
        el = Array.from(document.querySelectorAll("[id]"))
            .find(({ id }) => id?.toLowerCase() === normalizedTargetId)
    }
    if (!el) return

    // Async panels keep resizing the page after the first scroll, moving the
    // anchor away from the viewport, and the scroll spy rewrites the hash with
    // every endpoint crossed mid-flight. Keep the spy quiet and re-issue the
    // scroll until the anchor position is stable and reached.
    const targetTop = () => el.getBoundingClientRect().top + window.scrollY - 150
    let lastTop = null
    let attempts = 0
    const settle = () => {
        const top = targetTop()
        suppressScrollSpyUntil = Date.now() + 400
        if (Math.abs(window.scrollY - top) < 2) return
        if (lastTop === null || Math.abs(top - lastTop) > 1) {
            window.scrollTo({ top, behavior: attempts === 0 ? 'smooth' : 'auto' })
            lastTop = top
        }
        if (++attempts < 40) setTimeout(settle, 150)
    }
    settle()
}

export function capitalize(s) {
    return s.charAt(0).toUpperCase() + s.slice(1);
}

export const filter_falsey_keys = obj => Object.fromEntries(Object.entries(obj || {}).filter(([k, v]) => v))