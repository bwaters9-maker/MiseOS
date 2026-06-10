## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-10 - [Hoisting Intl.NumberFormat for massive gains]
**Learning:** Initializing 'Intl.NumberFormat' inside a loop is a significant performance bottleneck. Hoisting the formatter to a global/constant scope can reduce execution time by over 90% for functions performing repeated currency formatting.
**Action:** Always memoize or hoist 'Intl' formatters when they are used inside high-frequency execution paths like recipe cost calculations.
