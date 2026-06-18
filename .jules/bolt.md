## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.
## 2025-06-18 - [Optimizing high-frequency costing engine]
**Learning:** Significant performance gains in vanilla JS can be achieved by hoisting expensive object creation (RegExp, Intl.NumberFormat) and batching DOM updates using string buffers instead of incremental appends.
**Action:** Always hoist object instantiation out of hot paths and use innerHTML for bulk updates.
