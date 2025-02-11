
/** Encode the given {tag} for use in HTML anchors */
export const tagEncode = tag => tag.replace(" ", "-")

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

export function scrollToAnchor(hash) {
    const el = document.getElementById(hash.substring(1))
    if (el) window.scrollTo({
        top: document.getElementById(hash.substring(1)).getBoundingClientRect().top + window.scrollY,
        behavior: 'smooth'
    });
}