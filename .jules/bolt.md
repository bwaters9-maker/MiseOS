## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.
## 2025-06-25 - [Regex and Formatter Hoisting]
**Learning:** Initializing complex objects like RegExp or Intl.NumberFormat inside high-frequency functions (e.g., input handlers) creates significant garbage collection pressure and CPU overhead. Hoisting these to the global scope ensures they are compiled once and reused.
**Action:** Always move RegExp literals and internationalization formatters outside of performance-critical loops and event handlers.
