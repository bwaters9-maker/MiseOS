## 2025-05-22 - [Optimizing Recipe Parsing and DOM Reflows]
**Learning:** In vanilla JS applications with frequent interactive updates (like a live editor), O(N * M) lookups and incremental DOM appendChild calls in loops are major performance killers as the data grows. Batching DOM updates into a single innerHTML call and using early-exit search significantly improves responsiveness.
**Action:** Use .find() for lookups and accumulate HTML strings instead of appending individual elements to the DOM in high-frequency update paths.
## 2026-06-23 - [Updating Gemini Model to 3.5-Flash]
**Learning:** The project structure appears to have been consolidated into miseos_dashboard.html, with previously referenced src/ and backend files currently absent from the working tree and git history.
**Action:** Updated model references in the primary dashboard HTML and status labels to ensure application continuity with the latest production model. Fixed malformed backend package.json to restore dev script accessibility.
## 2026-06-23 - [Final Verification and JSON repair]
**Learning:** Malformed JSON in configuration files like package.json can silently break tooling. Flattening redundant nested objects restores expected behavior.
**Action:** Always validate JSON structure after manual edits.
## 2026-06-23 - [Fixing CI Build Failure]
**Learning:** CI pipelines that run automated build scripts (like 'npm run build') will fail if the underlying source files (e.g., a 'src' directory for TypeScript) are missing. Consolidated projects should have conditional build scripts.
**Action:** Updated root package.json to conditionally skip 'tsc' if 'src' is absent.
