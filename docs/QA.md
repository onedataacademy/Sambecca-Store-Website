# Verification for v1

JavaScript syntax validation passed. Twenty deterministic logic checks passed in a minimal DOM harness, covering initial rendering, catalogue validation, malformed imports, sold-out products/sizes, required size selection, bag addition, per-variant stock limits, price totals, sample discounts, stock changes, combined filters, sale/search/empty results, public routes, HTML escaping and unsafe URL rejection.

The harness checks application logic and generated markup. It is not a substitute for rendered-browser tests.

Browser checks could not be completed here: the local browser executable was unavailable, browser installation returned an invalid download, and the cloud browser could not reach the local preview. Pexels CDN image bytes were unavailable in this environment. The source pages and their image URLs were verified through web retrieval.

Before calling this visually approved, check on the deployed Cloudflare preview:

- Desktop at approximately 1440 px, tablet at 768 px and phones at 390 px and 320 px.
- Hero/model framing, image loading, category/product photographs and font loading.
- No horizontal overflow, readable content, keyboard focus and dialog close/Escape behavior.
- Search, filter combinations, sort, grid/list, sold-out sizes, wishlist, bag quantities and removal.
- Empty bag and checkout preview, form validation, discount and summary.
- Direct product/shop URLs and back/forward navigation.
- Owner edit/export/import and changes retained on the same browser.

Do not treat this preview as an approved or operational shop until the real catalogue and production features are completed.
