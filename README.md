# PowerSlave Developments — powerslave.dev

Static site for PowerSlave Developments: studio front door, app catalogue, support, and privacy policies.
Plain HTML/CSS, no build step, no JavaScript beyond a copyright year and one legacy-anchor redirect.
Hosted free on GitHub Pages at [powerslave.dev](https://powerslave.dev).

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Home — studio intro, featured app, catalogue, client-work teaser, origin story, contact |
| `work.html` | Client work — projects by sector, sourced from the Oct 2023 CV |
| `support.html` | Support — Android beta instructions, FAQ, contact |
| `privacy.html` | Privacy policy (TVApp and other apps) — required by the App Store |
| `privacy-wanderer.html` | Privacy policy for Map Wanderer (it uses third-party map/routing services, so it needs its own) |
| `style.css` | Shared styling — design tokens, dark and light themes |
| `favicon.svg` | Brand mark |
| `icons/` | App icons, 384×384 PNG (displayed at 60–96px) |

## Conventions

- **Design tokens** live in `:root` at the top of `style.css`. Dark is the default; the light palette is a
  `prefers-color-scheme: light` override. Change colours there, not in component rules.
- **Every page** shares the same `.topbar` markup and marks its own nav link with `aria-current="page"`.
- **Legacy anchors.** `#beta`, `#faq` and `#support` used to live on `index.html`. A small script in the
  `<head>` of `index.html` forwards those hashes to `support.html`, so old inbound links (App Store
  support URL, the Google group, anything already shared) keep working. Don't remove it without checking
  what still points at the old anchors.
- **Icons** are downscaled to 384px. Originals were 1024px and totalled 3.7 MB for images rendered at
  64px. If you add one, resize it: `sips -Z 384 icons/newapp.png --out icons/newapp.png`.

## Adding an app

Copy a `.card.app` block in the `#apps` section of `index.html`. Keep shipped apps above
"Coming soon" ones. The featured slot at the top of the page is a separate `.card.feature` block.

## Deploy

Push to `main` — GitHub Pages serves the repo root. Settings → Pages is set to
*Deploy from a branch*, branch `main`, folder `/ (root)`. The `CNAME` file pins the custom domain and
GitHub provisions HTTPS automatically.

## The "N years in the App Store" line

The hero on `index.html` claims our oldest app has been on the App Store for N years. **Don't hardcode
the number.** It lives in `data-years-since="2010-12-01"` on a `<span>`, and a script counts *completed*
years, so the figure can never overstate before the anniversary. Replace that date with TreeWise's exact
v1.0 release date from App Store Connect and the copy maintains itself forever.

## Known follow-ups

- **Confirm TreeWise's exact v1.0 date.** `2010-12-01` is a deliberately conservative placeholder chosen
  so the hero renders "15 years", matching what App Store Connect reports. The real date makes it exact.
- **Two dates in the source CV are impossible** and were reduced to years on `work.html` rather than
  guessed at: Zalando reads "Oct 2020 – Mar 2020" (published as 2019–2020), and Tignum reads
  "Jul 2019 – Sep 2020" for a stated 3-month contract (published as 2019). Correct at source if it matters.
- **Client names on `work.html` are published as-is from the CV.** Several were agency engagements
  (Candyspace/ITV, Cognizant) that can carry no-publicity clauses. Worth a check. The SapientNitro
  attribution on the Lloyds entry has already been removed.
- `og:image` is not set on any page, so links unfurl without a preview image. Needs a 1200×630 PNG.
- `index.html` still has a `TODO` for the Paprika description.
- `privacy.html` is linked as the general policy but its body text is written specifically about TVApp.
  Worth broadening the wording to cover Contagion, JetPack and TreeWise explicitly.
