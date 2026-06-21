## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-22 - [DOM Batching and Regex Hoisting Impact]
**Learning:** In high-frequency interactive paths like the `calculateRecipeCost` function which runs on every keystroke, the cumulative overhead of (N)$ DOM updates and redundant RegExp/Intl object initialization becomes a major bottleneck (~692ms for 1500 lines).
**Action:** Always batch DOM updates into a single `innerHTML` call and hoist RegExp/Intl literals to a global scope to maintain sub-300ms responsiveness for large datasets.
