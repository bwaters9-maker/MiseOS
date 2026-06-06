## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.

## 2026-06-06 - [Structural Fixes and Regex Optimization]
**Learning:** Logic that resides within a standalone HTML file is highly susceptible to structural breakage (e.g., code accidentally nested in `catch` blocks or function names split across lines). Performance can be significantly improved by moving high-frequency regex literals to the global scope to avoid redundant compilation.
**Action:** Always verify syntax integrity after structural edits. Pre-compile regex patterns in the global scope for hot paths like Markdown parsing and recipe line processing.
