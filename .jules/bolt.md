## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-25 - [Hoisting Formatters and Regex for Performance]
**Learning:** Redundant initialization of expensive objects like `Intl.NumberFormat` and `RegExp` inside high-frequency functions (e.g., input event handlers) adds unnecessary CPU overhead and GC pressure. Pre-compiling and hoisting these to the global scope yields measurable latency reductions.
**Action:** Define formatters and shared regex patterns outside of hot-path functions to ensure they are only initialized once.
