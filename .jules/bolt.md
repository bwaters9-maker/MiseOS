## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Cumulative Gains: Hoisting, Batching, and Early-Exit]
**Learning:** Combining multiple small optimizations in the hot path of a vanilla JS application (like a live recipe editor) can lead to massive performance gains. Hoisting 'Intl.NumberFormat' and RegExp literals saves significant initialization overhead, while DOM batching (innerHTML vs appendChild) and early-exit lookups (.find() vs forEach) reduce computational complexity and layout reflows.
**Action:** Always hoist object and regex initializations outside of loops/high-frequency functions, and batch DOM updates into a single operation.
