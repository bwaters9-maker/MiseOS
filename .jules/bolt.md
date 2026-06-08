## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Optimizing Formatters and Regex Pre-compilation]
**Learning:** Repeatedly initializing `Intl.NumberFormat` or compiling Regex literals inside high-frequency loops (like a throttled editor input) creates significant GC pressure and overhead. In single-file JS applications, globalizing these instances is a low-risk, high-reward optimization.
**Action:** Pre-create formatters and regex patterns in the global scope. Watch for syntax corruption when editing large script blocks in single-file HTML apps.
