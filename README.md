# PowerSlave Developments — Support Site

Static support & privacy site for PowerSlave Developments apps (TVApp, and more as they ship).
Plain HTML/CSS, no build step. Hosted free on GitHub Pages.

## Files
- `index.html` — landing page: app list, FAQ, contact
- `privacy.html` — privacy policy (required by the App Store)
- `style.css` — shared styling

## Before you publish
1. Replace the placeholder support email `support@powerslave.dev` in `index.html` and `privacy.html` with your real inbox.
2. (Optional) Tweak the FAQ / app copy.

## Deploy to GitHub Pages
1. Create a public repo (e.g. `powerslave-support`) and push these files.
2. Repo **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)`.
3. Your site goes live at `https://<user>.github.io/powerslave-support/` within a minute or two.
4. Use that URL (and the `/privacy.html` page) as your App Store **Support URL** and **Privacy Policy URL**.

### Custom domain (optional)
If you own a domain, add it under Settings → Pages → Custom domain, and add a `CNAME` file containing the domain. GitHub provisions HTTPS automatically.
