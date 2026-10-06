# Sambecca’s Closet | Website v1

A complete interactive storefront review, prepared for GitHub and Cloudflare Pages. The supplied logo is included. No build tools, paid theme or npm installation are required.

## Deploy with your usual workflow

1. Extract this ZIP.
2. Create a dedicated GitHub repository, for example `sambeccas-closet`.
3. Upload the **contents** of the extracted folder into the repository root. `index.html`, `assets`, `data`, `_redirects` and `_headers` should be at the top level. Do not upload the ZIP itself or an extra enclosing folder.
4. Connect that repository to a new Cloudflare Pages project. Select **None** as the framework preset, leave the build command empty, and use `/` as the build output directory.
5. Deploy and open the generated `pages.dev` URL.
6. Test the homepage, a product, the bag and a direct `/shop` URL. `_redirects` handles the clean page routes.

This package targets **Cloudflare Pages**. A Workers deployment requires separate routing/configuration; do not choose Workers when following these steps.

## What to review

- Editorial homepage, category cards, new arrivals, best-seller preview, brand story, benefits, social inspiration and newsletter preview.
- Shop: category, size, colour, price and availability filters; sorting; grid/list views; search.
- Product pages: gallery, zoom, colour and size selection, disabled sold-out sizes, quantity, bag, Buy Now, wishlist and sharing.
- Cart drawer: quantities, removal, subtotal and checkout.
- Checkout walkthrough: guest delivery details, order summary and sample `PREVIEW10` discount. It **does not take payment or place orders**.
- About, Contact, FAQ, Size Guide, Delivery, Returns, Privacy, Terms and account-launch information.
- Owner preview editor at `/admin`: products, prices, descriptions, sizes, colours, stock per variant, photo paths, banner and catalogue import/export.
- Mobile layouts, touch-visible product actions, keyboard focus, native dialogs and reduced-motion support.

## Important boundaries of this version

This is a review website, not an operational ecommerce backend. Sample product names, prices, fabric details, stock and images do not describe actual Sambecca’s Closet merchandise. Products designated as best sellers are demo selections, not verified sales claims. Real stock photographs are used to establish the design direction.

The owner editor is **not a protected admin dashboard**. It changes only the catalogue saved on the current browser. It does not publish edits or share stock between devices. There is no order database, server authentication, image-upload service, payment gateway, live account registration, email confirmation, sales analytics or abandoned-cart automation yet.

The contact form opens an email draft in the visitor’s email app. Newsletter signup is a walkthrough and does not store or submit addresses. Social sections link to the supplied accounts; they are not a fetched Instagram feed. The chat button opens email/Instagram until the owner supplies the official WhatsApp link.

Delivery charges, garment measurements and returns terms remain explicitly awaiting confirmation. No testimonials have been invented. Search indexing is disabled intentionally for this review build.

## Update products during review

1. Open `/admin` and choose **Edit piece & stock** or **Add a piece**.
2. Update the product, price and variant quantities. Quantity zero makes a size unavailable. Zero across all variants makes a product Out of Stock.
3. Save. The change is visible on that browser.
4. Choose **Export catalogue** to download `catalogue.js`.
5. Replace `data/catalogue.js` in GitHub with that exported file and commit. Cloudflare redeploys the updated preview.
6. Existing reviewers with local edits should use **Restore original sample catalogue** to reload the newly deployed catalogue, or clear their browser preview data on `/privacy`.

For newly added sizes or colours, save the product once, reopen it and set their quantities. Each new variant starts at zero.

To use actual photographs, upload files into `assets/images/`, then enter `/assets/images/your-file.jpg` in the photo field. Multiple photos can be listed one per line. Uploads are performed through GitHub, not through this browser editor.

## Photography and internet connection

The logo and icon are bundled. Stock images load from the Pexels CDN; fonts load from Google Fonts. The site needs an internet connection for those assets. Source pages and the license are listed in `docs/PHOTO_SOURCES.md`.

This environment could verify the photo source pages but could not download their image bytes. The ZIP therefore references those real source images remotely. Check that the photos load on the deployed preview. Replace them with the client’s actual photographs before accepting customer purchases. Local photos are preferable for final performance and reliability.

## Local preview

Do not double-click `index.html`: the clean routes and absolute paths expect a web server. For a local preview, run `python preview.py` from the extracted folder and open `http://localhost:8000`. This is optional; Cloudflare is the normal review workflow.

## Production next steps

See `docs/LAUNCH_INPUTS.md` for client assets and `docs/PRODUCTION_SCOPE.md` for the backend work still required. No API keys or customer passwords should ever be put into these public source files.

See `docs/QA.md` for the checks completed and the remaining visual verification.
