/** Recursively walks nested objects and arrays */
export function object_walk(obj, fn, replace = false) {
  if (Array.isArray(obj)) {
    if (replace) return obj.map((x, i) => fn(i, x));
    else obj.forEach((x, i) => fn(i, x));
  }
  if (typeof obj === "object") {
    for (const k in obj) {
      const r = fn(k, obj[k]);
      if (replace) obj[k] = r;
      object_walk(obj[k], fn, replace);
    }
  }
}
