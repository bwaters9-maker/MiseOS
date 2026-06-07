## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Regex and Formatter Overhead]
**Learning:** Even small object initializations like `new RegExp()` or `new Intl.NumberFormat()` inside high-frequency loops (or functions called by them) add up. Moving these to a global scope or pre-creating them can shave off several milliseconds in tight loops.
**Action:** Move all regex literals and formatters to the global scope to ensure they are only initialized once.
