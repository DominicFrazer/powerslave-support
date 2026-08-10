# PowerSlave Developments — powerslave.dev

Static site for PowerSlave Developments, a senior engineering consultancy that also publishes its own
apps. Plain HTML/CSS, nothing to build at deploy time, no JavaScript beyond a copyright year, a computed
year count, and one legacy-anchor redirect. Hosted free on GitHub Pages at
[powerslave.dev](https://powerslave.dev).

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Home — consultancy pitch, the ten-day proof block, engagement modes, audiences, both principals, clients, apps teaser, contact |
| `services.html` | Services — four ways to engage us, six specialities, audiences, philosophy |
| `team.html` | Team — full profiles for both principals, and why two people |
| `apps.html` | Our apps — featured app plus the catalogue, with language labels |
| `work.html` | Client work — engagements by sector, from the Oct 2023 CV and the company profile |
| `articles.html` | Articles — index of the eleven articles, newest first |
| `articles/*.html` | One page per article. **Generated — don't hand-edit.** See *Adding an article* |
| `articles/src/*.md` | The articles as written, in markdown. These are the source of truth for the text |
| `support.html` | Support — Android beta instructions, FAQ, contact |
| `privacy.html` | Privacy policy (TVApp and other apps) — required by the App Store |
| `privacy-wanderer.html` | Privacy policy for Map Wanderer (it uses third-party map/routing services, so it needs its own) |
| `style.css` | Shared styling — design tokens, dark and light themes |
| `favicon.svg` | Brand mark |
| `icons/` | App icons, 384×384 PNG (displayed at 60–96px) |
| `images/articles/` | Article hero images, 1600px-wide JPEG (~300 KB each) |
| `tools/build-articles.py` | Regenerates the Articles section from `articles/src/` |

## Conventions

- **Design tokens** live in `:root` at the top of `style.css`. Dark is the default; the light palette is a
  `prefers-color-scheme: light` override. Change colours there, not in component rules.
- **Every page** shares the same `.topbar` markup and marks its own nav link with `aria-current="page"`.
  The nav is defined twice: literally in the nine hand-written pages, and in `chrome()` in
  `tools/build-articles.py` for the generated article pages (which need `../` on every path). **Change one
  and you must change the other**, or the article pages will drift out of step with the rest of the site.
- **Legacy anchors.** Six sections have moved off `index.html` over time. A script in its `<head>`
  forwards `#beta`, `#faq` and `#support` to `support.html`, `#apps` to `apps.html`, `#about` to
  `team.html` and `#work` to `services.html`, so old inbound links (App Store support URL, the Google
  group, anything already shared) keep working. Don't remove it without checking what still points at
  the old anchors, and update it if you move a section again.
- **Print.** `@media print` in `style.css` sets A4 and replaces the `background-clip: text` gradients
  with solid ink — Chrome's PDF export otherwise paints their bounding boxes as visible rectangles.
  Render the set with headless Chrome: `--headless=new --no-pdf-header-footer --print-to-pdf=out.pdf`.
- **Icons** are downscaled to 384px. Originals were 1024px and totalled 3.7 MB for images rendered at
  64px. If you add one, resize it: `sips -Z 384 icons/newapp.png --out icons/newapp.png`.

## Adding an app

Copy a `.card.app` block in the `#apps` section of `apps.html`. Give it a `.platforms` row, a `.stack`
row naming the language, and keep the games at the bottom. The featured slot is a separate
`.card.feature` block.

## Adding an article

The eleven article pages and `articles.html` are generated, so the only files you edit by hand are the
markdown and the script's manifest.

1. Write the article as `articles/src/<slug>.md`, following the house header exactly — the parser depends
   on it:

   ```markdown
   # The title, as published

   **Dominic Frazer-Imregh**
   *Published on LinkedIn, 10 August 2026*

   ---

   First paragraph…
   ```

2. Add the hero image as `images/articles/<slug>.jpg`. Downscale it — the originals were ~2 MB each:
   `sips -s format jpeg -s formatOptions 82 -Z 1600 in.png --out images/articles/<slug>.jpg`.
3. Append an entry to `ARTICLES` in `tools/build-articles.py` with the `slug`, a `blurb` (the meta
   description and the index standfirst, ~150 characters) and an `alt` describing the image.
4. Run `python3 tools/build-articles.py`.
5. Add a `<url>` entry to `sitemap.xml`, using the publication date as `lastmod`.

Things the generator handles, so you don't have to:

- **Markdown.** Paragraphs, `**bold**`, `*italic*`, `>` blockquotes and `---` breaks. A paragraph that is
  *entirely* bold becomes an `<h2>` — that's how the articles mark their own sections, and why none of
  them use `##` headings.
- **Typography.** The sources are written with straight ASCII quotes; the generator converts them to
  curly on the way out, including `'80s` → `’80s` and single-quoted phrases. The markdown keeps the
  straight quotes, so don't "fix" them there.
- **Social previews.** Each article gets `og:type=article`, `og:image` pointing at its hero, and real
  image dimensions read off the file with `sips`.
- **Prev/next links**, ordered by position in `ARTICLES`, oldest first.

**Dates are deliberately not shown.** The header date is still required, still parsed, and still sets the
sitemap's `lastmod` — but no page prints it, and `article:published_time` is not emitted, because leaving
it in lets a search result display a date the pages themselves don't. Turning dates back on is a change to
two lines of the template (the `byline` and the index card), not a data problem.

## Deploy

Push to `main` — GitHub Pages serves the repo root. Settings → Pages is set to
*Deploy from a branch*, branch `main`, folder `/ (root)`. The `CNAME` file pins the custom domain and
GitHub provisions HTTPS automatically.

## The "N years in the App Store" line

The home page and `apps.html` both claim our oldest app has been on the App Store for N years. **Don't hardcode
the number.** It lives in `data-years-since="2010-09-17"` on a `<span>`, and a script counts *completed*
years, so the figure can never overstate before the anniversary.

That date is TreeWise v1.0's "Ready for Sale" timestamp from App Store Connect — 17 September 2010,
10:22 PM. It ticks over to 16 on 17 September 2026 with no edit needed.

## Known follow-ups

- **Two dates in the source CV are impossible** and were reduced to years on `work.html` rather than
  guessed at: Zalando reads "Oct 2020 – Mar 2020" (published as 2019–2020), and Tignum reads
  "Jul 2019 – Sep 2020" for a stated 3-month contract (published as 2019). Correct at source if it matters.
- **Client names on `work.html` are published as-is from the CV.** Several were agency engagements
  (Candyspace/ITV, Cognizant) that can carry no-publicity clauses. Worth a check. The SapientNitro
  attribution on the Lloyds entry has already been removed.
- **`JetPack Space Arcade` has supplied no privacy details to Apple.** The listing reads "the developer
  has not provided details about its privacy practices", and Apple will require them on the next update.
  The answer is Data Not Collected across every category, matching the other three apps.
- **App names on the site don't match the App Store titles.** `Contagion` is listed as *The Brigands of
  Venatus*; `JetPack` and `TreeWise` are prefixes of *JetPack Space Arcade* and *TreeWise: Tree Field
  Guide*. Keeping the site's names is a deliberate decision — but a user arriving from the Brigands
  listing won't see it named in the privacy policy.
- **`og:image` is set on the Articles pages only** — each article unfurls with its own hero, and
  `articles.html` borrows the newest one. The nine other pages still have no `og:image` and unfurl without
  a preview. Needs a 1200×630 PNG.
- **The LinkedIn originals are still the canonical copy in Google's eyes** for anything it indexed before
  these pages existed, and a `rel="canonical"` can't be set on a LinkedIn article. The fix is to trim each
  LinkedIn version to an intro plus a link to the page here, which keeps LinkedIn's distribution and moves
  the ranking signal onto this domain. Not done yet.
- **`articles.html` isn't teased anywhere on the home page.** The articles are the "how we think" proof
  that sits naturally between `services.html` and `work.html`, but nothing on `index.html` points at them
  beyond the nav.
- `apps.html` still has a `TODO` for the Paprika description.
- **Back end and platform engineering is not one of the six specialities**, though both principals list
  substantial back-end skills on `team.html`. Worth adding if it is work you want to be hired for.
