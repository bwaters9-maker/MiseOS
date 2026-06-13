## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-13 - [Hoisting Shared Resources for Hot Paths]
**Learning:** Redundant initialization of heavy objects like `Intl.NumberFormat` or `RegExp` inside loops or high-frequency event handlers (e.g., `oninput`) significantly degrades performance. Pre-compiling and hoisting these to the global scope eliminates this overhead.
**Action:** Always hoist formatting instances and regex literals outside of functions called during interactive UI updates.
