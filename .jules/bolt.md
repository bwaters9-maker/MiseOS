## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-27 - [Scoping and DOM Optimization]
**Learning:** Structural syntax errors (like an orphaned try-catch) can trap global variables/functions in local scopes, breaking application state and hindering performance analysis. Additionally, high-frequency UI updates benefit significantly from DOM batching via string accumulation and hoisting heavy objects like Intl.NumberFormat and RegExp.
**Action:** Always verify script scope and syntax before benchmarking. Use string buffers for innerHTML updates in loops and move static object creation to the global scope.
