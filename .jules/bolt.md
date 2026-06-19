## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Structural Corruption as a Performance & Functionality Blocker]
**Learning:** Structural syntax errors (like malformed tags or broken function names) can not only break functionality but also trap global variables and functions in local scopes (e.g., inside a malformed try...catch), making them inaccessible for benchmarking or external tools.
**Action:** Always verify global accessibility and syntax validity before attempting to benchmark or optimize core logic.
