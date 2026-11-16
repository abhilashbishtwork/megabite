# MegaBite Website: Handover for uEngage

**Live preview:** https://abhilashbishtwork.github.io/megabite/
**Goal:** host this site on **megabite.in**. It replaces the current online-ordering storefront.

## What this site is
- A **brand website only**. **No web ordering.**
- Every order button sends the visitor to the MegaBite app:
  - **iPhone/iPad** → App Store: https://apps.apple.com/in/app/megabite-online-ordering/id6817365667
  - **Android** → Google Play: https://play.google.com/store/apps/details?id=com.app.uengage.megabite
  - **Desktop** → scrolls to the "Download Now" footer, which has both store links.
- No links point to the old megabite.in ordering pages. Privacy, Terms and Refund have their own pages in this site.

## Files
| File | Purpose |
|---|---|
| `index.html` | Home page (all CSS/JS inline) |
| `privacy.html` | Privacy Policy |
| `terms.html` | Terms & Conditions |
| `refund.html` | Refund Policy |
| `img/` | Logo + food photos (from MegaBite's own uEngage menu images) |
| `build/legal.py`, `build/legal_tpl.html` | Source for the 3 legal pages. Edit `legal.py`, then run `python3 build/legal.py` to regenerate them. Not needed on the server. |

## Hosting requirements
- **Plain static HTML.** No backend, database, framework or build step.
- Upload `index.html`, `privacy.html`, `terms.html`, `refund.html` and the `img/` folder to the web root.
- All links are relative, so it works at the domain root as-is.
- External dependency: Google Fonts only (Anton, Figtree, Instrument Serif).
- HTTPS required.

## Please also set up on megabite.in
1. **301 redirects** from the old storefront URLs:
   - `/privacy-policy` → `/privacy.html`
   - `/terms-and-conditions` → `/terms.html`
   - `/refund-policy` → `/refund.html`
   - Old product, menu and order paths, and `/promo-codes` → `/`
2. **Ordering:** turn off web ordering on the domain. App ordering stays as it is.
3. **App deep links:** keep any `apple-app-site-association` and `assetlinks.json` files under `/.well-known/` that the app needs.

## Before go-live (Curefoods side)
- **Legal review:** confirm the legal entity name used in the policies ("Curefoods India Private Limited").
- **Refund page:** confirm the 24-hour window for reporting missing or wrong items.

Contact: megabite@curefoods.in
