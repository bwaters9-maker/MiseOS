## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Hoisting Intl.NumberFormat and Regex Patterns]
**Learning:** Initializing `Intl.NumberFormat` and RegExp objects inside high-frequency loops (like a 400-line recipe parser) adds significant overhead. Hoisting these to the global scope can yield massive performance gains (e.g., reducing execution time from ~81ms to ~9ms).
**Action:** Always move `Intl.NumberFormat` and complex Regular Expression literals to the global scope in performance-critical paths.
