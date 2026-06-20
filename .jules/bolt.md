## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2025-05-23 - [Restoring Scope and Batching DOM Updates]
**Learning:** Structural syntax errors (like malformed tags or unclosed try-catch blocks) can silent-fail by trapping global functions in local scopes, making them "undefined" to external callers like Playwright. Once scope is restored, performance can be dramatically improved by replacing O(N) DOM appends with a single innerHTML update from a string buffer.
**Action:** Always verify global scope availability if functions are reported as undefined, and prioritize DOM update batching in high-frequency event handlers.
