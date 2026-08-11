# PowerSlave Developments — powerslave.dev

Static site for PowerSlave Developments, a senior engineering consultancy that also publishes its own
apps. Plain HTML/CSS, nothing to build at deploy time, and no JavaScript beyond a copyright year, a
computed year count, one legacy-anchor redirect and the theme override button. Hosted free on GitHub
Pages at [powerslave.dev](https://powerslave.dev).

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Home — consultancy pitch, the ten-day proof block, engagement modes, audiences, both principals, clients, apps teaser, articles teaser, contact |
| `services.html` | Services — four ways to engage us, seven specialities, audiences, philosophy |
| `team.html` | Team — full profiles for both principals, and why two people |
| `apps.html` | Our apps — featured app plus the catalogue, with language labels |
| `work.html` | Client work — engagements by sector, from the Oct 2023 CV and the company profile |
| `articles.html` | Articles — index of the eleven articles, newest first |
| `articles/*.html` | One page per article. **Generated — don't hand-edit.** See *Adding an article* |
| `articles/src/*.md` | The articles as written, in markdown. These are the source of truth for the text |
| `contact.html` | Contact — what to put in the first email, who reads it, and faster routes for app and privacy questions |
| `support.html` | Support — Android beta instructions, FAQ, contact |
| `privacy.html` | Privacy policy (TVApp and other apps) — required by the App Store |
| `privacy-wanderer.html` | Privacy policy for Map Wanderer (it uses third-party map/routing services, so it needs its own) |
| `style.css` | Shared styling — design tokens, dark and light themes |
| `404.html` | Not-found page. GitHub Pages serves it for any unknown path |
| `feed.xml` | Atom feed for the articles. **Generated** |
| `favicon.svg` | The symbol mark — gradient squircle with a P. Browser tab and bookmarks |
| `apple-touch-icon.png` | 180×180 home-screen icon. At the root deliberately — see the conventions |
| `icons/` | App icons, 384×384 PNG (displayed at 60–96px) |
| `images/articles/` | Article heroes at 1600px, plus `-800` and `-400` variants for `srcset` |
| `images/og-default.png` | The 1200×630 social card every page but the articles unfurls with |
| `images/logo-powerslave.svg` | The wordmark, vector, 4 KB. Topbar on every page, and the social card |
| `images/logo-powerslave.png` | The same wordmark rasterised from that SVG. **Only** for the structured-data logo |
| `tools/build-articles.py` | Regenerates the Articles section from `articles/src/` |
| `tools/og-image.html` | Source for `og-default.png`. Not served — see the comment in it for the render command |

## Conventions

- **Design tokens** live in `:root` at the top of `style.css`. Dark is the default; light applies when the
  system asks for it or the reader picks it. Change colours there, not in component rules.
- **The theme override.** A button in the topbar switches dark/light and stores the choice in
  `localStorage`, so it survives navigation. Three pieces make it work, and each is defined twice — once
  in the ten hand-written pages and once in `tools/build-articles.py` (`theme_head()`, the button inside
  `chrome()`, and `theme_script()` appended by `footer()`). **Change one and change the other.**

  The palette arbitration is worth reading before touching it. `:root` is dark;
  `@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) }` is the automatic light case;
  `:root[data-theme="light"]` is the explicit one. Both light selectors are (0,2,0) so the explicit choice
  wins on document order, and plain `:root` is (0,1,0) and loses to either — which covers all four
  combinations of system preference and stored choice. **The light palette is therefore written twice, and
  both copies have to change together**; dark needs no second copy because the `:not()` steps aside for it.

  The button ships with the `hidden` attribute and script removes it, so a reader with JavaScript off is
  never shown a control that cannot work — the OS preference still drives the palette on its own. The
  script also rewrites both `<meta name="theme-color">` tags to the effective colour, because those are
  keyed to the *system* preference and would otherwise leave a phone's address bar showing the palette the
  reader just switched away from.
- **The nav is full.** Eight links plus the theme button come to 832px against 860px of content width, so
  `.topnav` was tightened to 3px gaps and 10px padding to keep it on one row. A ninth link will push the
  whole group onto a second line — tighten further, or drop something (`Privacy` is the obvious candidate,
  since it is in the footer on every page).
- **The topbar brand is the wordmark alone**, with no text beside it. The artwork reads "POWERSLAVE", so
  the link's accessible name comes entirely from `alt="PowerSlave Developments"` — that alt is the only
  place the full company name appears in the header, so don't shorten it. The old gradient `.dot` is gone.
- **Every page** shares the same `.topbar` markup and marks its own nav link with `aria-current="page"`.
  The nav is defined twice: literally in the ten hand-written pages, and in `chrome()` in
  `tools/build-articles.py` for the generated article pages (which need `../` on every path). **Change one
  and you must change the other**, or the article pages will drift out of step with the rest of the site.
- **One footer, identical on every page** — the same nine links in the same order, including a link to the
  page you are already on. Pages used to drop their own link from the set, which meant nine subtly
  different footers, one of which (`work.html`) had quietly lost three links with nothing to catch it.
  Uniformity is the point: there is now a single block to check a new page against. It is defined in the
  same two places as the nav — literally in the hand-written pages, and in `footer()` in
  `tools/build-articles.py`. `404.html` carries the same set with root-absolute paths, for the reason
  below. The Map Wanderer policy is deliberately *not* in it — it is one app's policy, and it is linked
  from `privacy.html` twice, `support.html` twice and `apps.html`.
- **Social previews.** Every page carries `og:image` and `twitter:card=summary_large_image`. The nine
  hand-written pages share `images/og-default.png`; each article points at its own hero instead. The card
  is rendered from `tools/og-image.html`, which duplicates the palette rather than linking `style.css` —
  it renders at a fixed 1200×630 with no viewport, so the `clamp()` sizes and the light-mode override
  would both fight it. Change the brand colours in one and change them in the other.
- **The wordmark** in `images/logo-powerslave.png` was supplied as an opaque PNG on a dark ground, with a
  generator watermark below the artwork. It was cropped to the wordmark — which removes the watermark
  rather than painting over it — and its background keyed to transparent from luminance, the letters being
  far brighter than the ground. The result reads correctly on both themes and stays legible down to about
  15px tall.

  The vector arrived and is now the asset used everywhere on the page. It needed the same two fixes: the
  supplied file had an opaque `<rect>` painting a dark radial background across the whole canvas, and the
  watermark as a second `<path>` — the only one not filled with `url(#txt)` — at x 1664–1716, y 479–531.
  Both were removed and the `viewBox` tightened to the glyphs. The text gradient is `userSpaceOnUse`, so
  it stays aligned to the letters despite the new `viewBox`.

  `logo-powerslave.png` is rendered *from* that SVG, so the two cannot drift, and it exists for exactly one
  reason: **Google does not accept SVG for `Organization.logo`**. Don't reference it anywhere else, and
  re-render it if the SVG changes.
- **Structured data.** `index.html` carries `Organization` by hand; the article pages carry `Article` and
  `articles.html` carries `CollectionPage`, all generated. `datePublished` *is* emitted — dates are
  suppressed for readers, not for machines. See the note under *Adding an article*.
- **Responsive images.** Article heroes and index thumbnails use `srcset`. The variants are committed
  next to the originals; regenerate them with the `sips` line under *Adding an article*.
- **`404.html` uses root-absolute paths.** GitHub Pages serves it for any unknown path at any depth, so a
  mistyped `/articles/foo.html` renders it from inside `/articles/`. Relative paths would resolve against
  that directory and break every link and the stylesheet.
- **Legacy anchors.** Six sections have moved off `index.html` over time. A script in its `<head>`
  forwards `#beta`, `#faq` and `#support` to `support.html`, `#apps` to `apps.html`, `#about` to
  `team.html` and `#work` to `services.html`, so old inbound links (App Store support URL, the Google
  group, anything already shared) keep working. Don't remove it without checking what still points at
  the old anchors, and update it if you move a section again.
- **Print.** `@media print` in `style.css` sets A4 and replaces the `background-clip: text` gradients
  with solid ink — Chrome's PDF export otherwise paints their bounding boxes as visible rectangles.
  Render the set with headless Chrome: `--headless=new --no-pdf-header-footer --print-to-pdf=out.pdf`.
- **Two brand marks, on purpose.** The wordmark (`images/logo-powerslave.svg`) is the header lockup; the
  squircle P (`favicon.svg`) is the symbol, used for the browser tab and the home-screen icon. A 8.8:1
  wordmark cannot be a favicon, and a symbol plus a wordmark is the normal arrangement. They share the
  accent gradient, which is what ties them together — keep it that way if either changes.
- **`apple-touch-icon.png` is full-bleed, square and has no alpha channel.** iOS applies its own rounded
  mask, so pre-rounding it double-rounds the corners, and it composites transparency onto black. It also
  lives at the repo root rather than in `images/`, because iOS looks for `/apple-touch-icon.png` when a page
  has no `<link>` for one — so the root copy is a safety net on top of the explicit tags. Every page
  previously pointed at an *app* icon here (`icons/tvapp.png`, and `icons/mapwanderer.png` on the Map
  Wanderer policy), so adding the site to a home screen produced the TVApp icon.
- **Icons** are downscaled to 384px. Originals were 1024px and totalled 3.7 MB for images rendered at
  64px. If you add one, resize it: `sips -Z 384 icons/newapp.png --out icons/newapp.png`.
- **The specialities count is written out in three places** — the `<span class="note">` in the section
  header on `services.html`, the page lede, and its `og:description`. Add or remove a card and all three
  need changing; nothing computes it.
- **The article count is not one of those traps.** It appears in prose on `index.html` and `404.html` and
  three times on `articles.html`, and `sync_counts()` in `tools/build-articles.py` rewrites every copy on
  each run. It can't be computed in the browser, because two of the copies are `<meta>` descriptions a
  crawler reads — so it is written at build time instead. The rewrite anchors on the phrase
  `" articles on what AI actually changes"`, held in `COUNT_PHRASE`: **keep that wording intact in both
  hand-written pages**, or change it in both places and in the script. The build exits with an error if a
  page stops matching, rather than leaving a stale number behind.

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

2. Add the hero image as `images/articles/<slug>.jpg`. Downscale it — the originals were ~2 MB each —
   and make the two `srcset` variants:

   ```sh
   sips -s format jpeg -s formatOptions 82 -Z 1600 in.png --out images/articles/<slug>.jpg
   sips -s format jpeg -s formatOptions 80 -Z 800  images/articles/<slug>.jpg --out images/articles/<slug>-800.jpg
   sips -s format jpeg -s formatOptions 78 -Z 400  images/articles/<slug>.jpg --out images/articles/<slug>-400.jpg
   ```
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
- **The author card** at the foot of every article, from `AUTHOR`, `AUTHOR_ROLE` and `AUTHOR_BIO`. Every
  article is Dominic's, so it is a constant rather than per-entry data — give `ARTICLES` an author field if
  that ever stops being true. It sits *outside* `.article-foot` on purpose: that block is navigation and
  `@media print` drops it, whereas who wrote the piece is content and should survive to paper.
- **The spelled-out article count**, everywhere it appears — see the conventions above.
- **Structured data** — `Article` per page, `CollectionPage` on the index.
- **The Atom feed** at `feed.xml`, newest first, with autodiscovery `<link>`s on the article pages,
  `articles.html` and the home page.
- **A warning if a headline runs over Google's 110-character guidance**, which risks the `Article` rich
  result being dropped for that page. `hiring-system-is-right` is 125 and is left alone deliberately:
  trimming it would misrepresent the title. Shorten the title itself if you want that page to comply.

**Dates are suppressed for readers, not for machines.** No page prints a publication date — the byline
reads "Published on LinkedIn" with no date, and the index cards carry none. But the date is still required
in the source header, and it still feeds everything a machine reads: `article:published_time`, the
`Article` schema's `datePublished`, the sitemap's `lastmod`, and the Atom feed's `<updated>` (which Atom
makes mandatory anyway).

So the rule is: dates are fine in metadata, just not in text a reader sees. Turning them back on visibly
is a change to two lines of the template — the `byline` and the index card.

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

- **`contact.html` and the `services.html` FAQ deliberately answer nothing commercial.** No response-time
  commitment, no day rate, no minimum engagement, no IP-ownership position, and no stated availability.
  NDAs are the one exception — the contact page says we'll sign one either way, which needs no published
  document. Every other answer on those two surfaces is derivable from the record on `work.html` and
  `team.html`; those four are not, and inventing them would put claims about the business on the site that
  the business hasn't made. The FAQ closes by saying they're better answered against a real situation and
  routing to email — which is defensible, but it is a stopgap. Supply the facts and they become the most
  valuable answers on the page, because they are the ones every buyer actually wants.
- **No LinkedIn links anywhere on the site.** The eight testimonials on `work.html` are quoted from
  LinkedIn recommendations and say so, and all eleven articles were published there first — but nothing
  links to either principal's profile, and the `Organization` block in `index.html` has no `sameAs`. That
  costs twice: a reader can't verify the quotes, and search engines have no edge joining this site to two
  established profiles. Adding the two profile URLs fixes both.

- **Two dates in the source CV are impossible** and were reduced to years on `work.html` rather than
  guessed at: Zalando reads "Oct 2020 – Mar 2020" (published as 2019–2020), and Tignum reads
  "Jul 2019 – Sep 2020" for a stated 3-month contract (published as 2019). Correct at source if it matters.
- **Client names on `work.html` are cleared, on the grounds that they are already public.** Cognizant and
  Candyspace/ITV both appear on Dominic's own LinkedIn profile, so naming them here adds no exposure that
  doesn't already exist — checked and confirmed on 10 August 2026. That reasoning is the record; if a name
  is ever removed from the profile, this page stops being covered by it. The SapientNitro attribution on
  the Lloyds entry was removed earlier and stays removed.
- **`JetPack Space Arcade` has supplied no privacy details to Apple.** The listing reads "the developer
  has not provided details about its privacy practices", and Apple will require them on the next update.
  The answer is Data Not Collected across every category, matching the other three apps.
- **App names on the site don't match the App Store titles.** `Contagion` is listed as *The Brigands of
  Venatus*; `JetPack` and `TreeWise` are prefixes of *JetPack Space Arcade* and *TreeWise: Tree Field
  Guide*. Keeping the site's names is a deliberate decision — but a user arriving from the Brigands
  listing won't see it named in the privacy policy.
- **The LinkedIn originals are left at full length on purpose. This is a decision, not an oversight — don't
  "fix" it.** For anything Google indexed before these pages existed, LinkedIn is the canonical copy in its
  eyes, and `rel="canonical"` can't be set on a LinkedIn article. The available remedy is to trim each
  LinkedIn version to an intro plus a link to the page here, which keeps LinkedIn's distribution while
  leaving only one full copy of the text for Google to rank. That is on hold because linking back to
  powerslave.dev from LinkedIn isn't wanted yet.

  What it costs while it stays on hold: both copies remain live and LinkedIn keeps the ranking for that
  text. Nothing else on the site is affected, and nothing here needs changing when the decision changes —
  the trimmed text is derived from `articles/src/`, so it can be regenerated on demand.
- **Two `TODO`s are still live in shipped markup.** `apps.html` needs the Paprika one-liner once it is
  announced, and `support.html` needs real support content for two of the games — controls, saving and
  progress. Both need product facts rather than copywriting.
- **`hiring-system-is-right` has a 125-character headline**, over Google's 110-character guidance for
  `Article`, so that page's rich result may be dropped. Left as-is because trimming misrepresents the
  title; the build prints a reminder each run.
