# Operational store work after visual approval

The first ZIP establishes the complete customer-facing design and review interactions. A static website alone cannot safely manage multi-customer inventory or verify payments. These capabilities remain a distinct implementation stage, not features already live in this package.

## Catalogue and secure admin

Use a durable server database with products, variants, quantities, images, prices and visibility. Protect owner routes and APIs with server-side authentication and authorization. Validate all writes. Store actual photos in object storage. Include audit history and export/backups. The current local `/admin` workspace must be replaced with protected administration; a client-side password is not sufficient.

## Orders and inventory

Calculate all prices, promo codes and delivery fees on the server. Check stock when preparing checkout and again when finalizing a verified payment. Use transactional inventory reservation and expiry so two buyers cannot purchase the same last unit. Store durable orders, status history, payment references and delivery data. Keep retries and callbacks idempotent.

## Payment

Connect the approved Nigerian merchant gateway on the server. Keep secret keys in server environment variables. Verify gateway webhook signatures and transaction amount, currency and order reference before marking an order paid. A browser callback is not proof of payment. Never collect raw card details in this frontend.

## Customer experience

Add authenticated accounts, password recovery or passwordless sign-in, saved addresses and authorized order history. Keep guest checkout. Connect transactional email, customer support, order tracking and the approved newsletter provider. Add real reviews only with approval.

## Hosting and launch

Cloudflare Pages can host the current storefront. An operational backend can use Pages Functions/Workers with an appropriate persistent database and image storage, or a managed commerce service. Provider limits, payment fees and any subscription costs must be agreed separately once the owner selects the services.

After operational checks pass: replace sample assets, complete policies, remove review banners and noindex declarations from HTML, `_headers` and `robots.txt`, generate a sitemap with the approved domain, add real canonical URLs and product metadata, and configure Search Console and any approved analytics. Clean URLs are already supported; this client-rendered review does not claim fully deployed product SEO.
