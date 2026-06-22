## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-22 - [Hoisting Expensive Constructors and Batching DOM Updates]
**Learning:** Re-instantiating `Intl.NumberFormat` and `RegExp` objects inside high-frequency functions (like those triggered by `oninput`) adds significant CPU overhead. Combined with DOM reflows from multiple `appendChild` calls, this can cause noticeable lag in larger documents.
**Action:** Move `Intl.NumberFormat` and static `RegExp` patterns to the global scope. Accumulate HTML strings to perform a single `innerHTML` update per event cycle.
