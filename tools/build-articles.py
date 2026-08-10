#!/usr/bin/env python3
"""Generate the Articles section from the markdown in articles/src/.

The site has no build step: the HTML this emits is the artefact that ships, and
it is committed alongside everything else. This script exists so that a change
to the article template doesn't mean hand-editing eleven files. Run it from the
repo root after editing a source file or the template:

    python3 tools/build-articles.py

It writes articles/<slug>.html for every entry in ARTICLES, plus articles.html
and feed.xml. Nothing else in the repo is touched.
"""

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "articles" / "src"
OUT = ROOT / "articles"
IMG = ROOT / "images" / "articles"

SITE = "https://powerslave.dev"
AUTHOR = "Dominic Frazer-Imregh"

# Oldest first. `blurb` is the meta description and the index standfirst;
# `alt` describes the hero image for screen readers.
ARTICLES = [
    {
        "slug": "nobody-cares-assembler-coder",
        "blurb": "6502 assembler to Swift, and why none of it matters to a hiring "
                 "manager today. AI isn't a threat to engineering — it's the next "
                 "layer of abstraction.",
        "alt": "A CRT monitor showing 6502 assembly beside a MOS 6502 chip, a "
               "weathered page of Objective-C header code, a Java mug and a dusty "
               "copy of The Java Programming Language.",
    },
    {
        "slug": "tdd-bdd-sdd",
        "blurb": "TDD and BDD were both trying to pin down what software should do, "
                 "and both drowned in the syntax of doing it. Here's the one that's "
                 "actually doing the work now.",
        "alt": "Cobwebbed books on a dusty shelf in low light, their spines reading "
               "Test-Driven Development, BDD in Action and Clean Code.",
    },
    {
        "slug": "scenario-engineer",
        "blurb": "My QA fix their own bugs and my PMs ship features. The engineering "
                 "role isn't being replaced — it's unbundling, and the pieces are "
                 "landing in unexpected hands.",
        "alt": "A half-built LEGO castle on a paint-spattered desk, surrounded by "
               "loose bricks, a coffee mug, headphones, an electric guitar and an "
               "open notebook.",
    },
    {
        "slug": "hiring-system-is-right",
        "blurb": "I've written code since the '80s and shipped Apple apps since "
                 "iOS 3. I'd never get hired today — and the uncomfortable part is "
                 "that the funnel isn't wrong.",
        "alt": "An empty, sunlit meeting room with rows of old chairs facing a "
               "projector screen headed “MVC vs MVVM”, comparing Model/View/"
               "Controller with Model/View/ViewModel.",
    },
    {
        "slug": "ceo-built-his-own-battle-station",
        "blurb": "My CEO sent me a two-page technical specification he hadn't read, "
                 "titled “Yo, I have spec for you”. What happens when the people "
                 "above you can build their own proofs.",
        "alt": "A fully assembled LEGO Death Star on an executive desk beside a "
               "closed laptop, a coffee mug, spare bricks and an open handwritten "
               "notebook.",
    },
    {
        "slug": "claude-told-me-42",
        "blurb": "Deep Thought answered 42 because nobody had understood the "
                 "question. The same thing happens with an LLM on a Tuesday "
                 "afternoon, and noticing is your job.",
        "alt": "A LEGO minifigure in a dressing gown and sunglasses holding a book "
               "marked GUIDE, standing on a desk between two screens of code, with "
               "a LEGO Death Star on the shelf behind.",
    },
    {
        "slug": "1000-applicants-3-jobs",
        "blurb": "Three roles, a thousand applicants, and why I'm hiring mid-level "
                 "rather than senior or junior. How you choose when the funnel is "
                 "beyond human reading.",
        "alt": "An office with three empty interview chairs and a monitor reading "
               "“Applications (2,856) — Loading”, while a crowd of candidates "
               "holding CVs presses against the window outside.",
    },
    {
        "slug": "sir-madam-agent",
        "blurb": "An open letter to every agency with a “carefully curated bench of "
                 "senior talent” — three questions I'd like answered before you "
                 "send me a single CV.",
        "alt": "A galvanised bucket crammed with LEGO minifigures and loose bricks, "
               "plastered with labels reading Pre-vetted talent, Top 1%, Senior "
               "specialists, Carefully curated and Hand-picked, beside a contract "
               "and a fan of banknotes.",
    },
    {
        "slug": "daily-standup-is-dead",
        "blurb": "Fifteen minutes, three questions, reported blindly to people who "
                 "aren't really listening. We stopped doing it and replaced it with "
                 "a kitchen.",
        "alt": "Two laptops on a desk — one labelled “Demo Room” showing a pair "
               "programming session, one labelled “Kitchen” showing a six-person "
               "video call of people holding mugs and laughing.",
    },
    {
        "slug": "not-an-ai-guru",
        "blurb": "Like a racing driver, I'm expert at using the tool — not at "
                 "building it. Don't call me a mechanic when all I do is sit behind "
                 "the wheel and press the gas.",
        "alt": "Two LEGO minifigures on a desk: a racing driver in a helmet holding "
               "a steering wheel, and a tuxedoed crooner singing into a microphone.",
    },
    {
        "slug": "measurement-problem",
        "blurb": "AI accelerates whatever direction you're pointed in, including "
                 "deeper into a hole you didn't know you were in. When the "
                 "measurement is wrong, free typing makes it worse.",
        "alt": "A monitor showing a pull request list — eighteen merged PRs and "
               "“0 releases in 6 weeks” — beside a handwritten release checklist, a "
               "wall chart reading “Nothing shipped 0”, and a sticky note saying "
               "“Ship it”.",
    },
]

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], start=1)}


# --- markdown ----------------------------------------------------------------

def smarten(text):
    """The sources use straight ASCII quotes throughout. Long-form prose reads
    better set properly, so convert on the way out and leave the markdown
    originals exactly as written."""
    # Decade elision ('80s) takes a closing-shaped apostrophe. Handle it before
    # the opening-quote rule below, which would otherwise claim it.
    text = re.sub(r"'(?=\d0s\b)", "’", text)
    # A quote that opens a word after a space, bracket or emphasis marker is a
    # single quotation mark; every other one is an apostrophe.
    text = re.sub(r"(?<![^\s(\[*])'(?=\S)", "‘", text)
    text = text.replace("'", "’")
    text = re.sub(r'(?<![^\s(\[*])"', "“", text)
    text = text.replace('"', "”")
    return text


def attr(text):
    """Escape for a double-quoted attribute. Apostrophes are left alone —
    html.escape(quote=True) turns them into &#x27; for no benefit here."""
    return smarten(text).replace("&", "&amp;").replace("<", "&lt;") \
                        .replace(">", "&gt;").replace('"', "&quot;")


def inline(text):
    """Set the quotes, escape HTML, then apply the only inline markup these
    articles use."""
    out = html.escape(smarten(text), quote=False)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", out)
    return out


def body_to_html(body):
    """Blocks separated by blank lines. A block that is entirely bold is a
    subheading — the articles use that instead of markdown ### headings."""
    parts = []
    for block in re.split(r"\n\s*\n", body.strip()):
        block = block.strip()
        if not block:
            continue
        if block == "---":
            parts.append("        <hr>")
            continue
        if block.startswith(">"):
            quote = " ".join(l.lstrip("> ").strip() for l in block.splitlines())
            parts.append(f"        <blockquote><p>{inline(quote)}</p></blockquote>")
            continue
        flat = " ".join(l.strip() for l in block.splitlines())
        heading = re.fullmatch(r"\*\*(.+)\*\*", flat)
        if heading:
            parts.append(f"        <h2>{inline(heading.group(1))}</h2>")
            continue
        parts.append(f"        <p>{inline(flat)}</p>")
    return "\n".join(parts)


def parse(slug):
    """The date is still required in the source header and still parsed, even
    though the pages no longer show it: it keeps the sources self-describing, it
    fixes the sitemap's lastmod, and it means turning the dates back on is a
    template change rather than an archaeology exercise. Parsing it also catches
    a malformed header instead of letting it through silently."""
    raw = (SRC / f"{slug}.md").read_text(encoding="utf-8")
    head, _, body = raw.partition("\n---\n")
    title = re.search(r"^#\s+(.*)$", head, re.M).group(1).strip()
    date = re.search(r"^\*Published on LinkedIn,\s*(.+?)\*$", head, re.M).group(1)
    day, month, year = date.split()
    iso = f"{int(year):04d}-{MONTHS[month]:02d}-{int(day):02d}"
    return {"title": title, "date": date, "iso": iso, "body": body}


def dimensions(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
                         capture_output=True, text=True).stdout
    w = re.search(r"pixelWidth:\s*(\d+)", out)
    h = re.search(r"pixelHeight:\s*(\d+)", out)
    if not (w and h):
        sys.exit(f"could not read dimensions for {path}")
    return w.group(1), h.group(1)


# --- structured data ---------------------------------------------------------

PUBLISHER = {
    "@type": "Organization",
    "name": "PowerSlave Developments",
    "url": f"{SITE}/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/images/logo-powerslave.png",
             "width": 1560, "height": 250},
}


def ld(data, indent="  "):
    """Serialise as a JSON-LD script block. json.dumps escapes what needs
    escaping and emits real UTF-8, so the curly quotes in titles survive."""
    body = json.dumps(data, indent=2, ensure_ascii=False)
    body = "\n".join(indent + line for line in body.splitlines())
    return f'{indent}<script type="application/ld+json">\n{body}\n{indent}</script>'


def article_ld(entry, meta, w, h):
    """Article schema. datePublished is present because the dates are only
    suppressed for readers, not for machines — same call as the sitemap and the
    feed. Nothing here renders on the page."""
    return ld({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": smarten(meta["title"]),
        "description": smarten(entry["blurb"]),
        "image": {
            "@type": "ImageObject",
            "url": f"{SITE}/images/articles/{entry['slug']}.jpg",
            "width": int(w),
            "height": int(h),
        },
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{SITE}/team.html"},
        "publisher": PUBLISHER,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{SITE}/articles/{entry['slug']}.html",
        },
        "isPartOf": {
            "@type": "Blog",
            "name": "Articles — PowerSlave Developments",
            "@id": f"{SITE}/articles.html",
        },
        "datePublished": meta["iso"],
        "inLanguage": "en-GB",
        "wordCount": len(meta["body"].split()),
    })


def index_ld(entries):
    """The index as a collection, with the articles as an ordered list. Newest
    first, matching the order they are rendered in."""
    return ld({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Articles — PowerSlave Developments",
        "url": f"{SITE}/articles.html",
        "isPartOf": {"@type": "WebSite", "name": "PowerSlave Developments",
                     "url": f"{SITE}/"},
        "publisher": PUBLISHER,
        "inLanguage": "en-GB",
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(entries),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i,
                    "url": f"{SITE}/articles/{e['slug']}.html",
                    "name": smarten(e["meta"]["title"]),
                }
                for i, e in enumerate(reversed(entries), start=1)
            ],
        },
    })


# --- templates ---------------------------------------------------------------

def chrome(prefix, current):
    """The shared topbar. `current` is the nav file to mark as the live page."""
    links = [("services.html", "Services"), ("work.html", "Work"),
             ("apps.html", "Apps"), ("team.html", "Team"),
             ("articles.html", "Articles"), ("support.html", "Support"),
             ("privacy.html", "Privacy")]
    nav = "\n".join(
        f'        <a href="{prefix}{href}"'
        f'{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in links)
    return f"""  <div class="topbar">
    <div class="topbar-inner">
      <a class="brand" href="{prefix}index.html"><img src="{prefix}images/logo-powerslave-400.png" alt="PowerSlave Developments" width="400" height="64"></a>
      <nav class="topnav" aria-label="Main">
{nav}
      </nav>
    </div>
  </div>"""


def footer(prefix):
    links = [("index.html", "Home"), ("services.html", "Services"),
             ("team.html", "Team"), ("work.html", "Client work"),
             ("apps.html", "Our apps"), ("articles.html", "Articles"),
             ("support.html", "Support"), ("privacy.html", "Privacy Policy")]
    items = "\n".join(f'        <a href="{prefix}{h}">{l}</a>' for h, l in links)
    return f"""  <footer>
    <div class="wrap">
      <div>© <span id="year">2026</span> PowerSlave Developments. All rights reserved.</div>
      <div class="links">
{items}
      </div>
    </div>
  </footer>

  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>"""


def article_page(entry, meta, prev_entry, next_entry):
    slug = entry["slug"]
    w, h = dimensions(IMG / f"{slug}.jpg")
    title = attr(meta["title"])
    blurb = attr(entry["blurb"])
    alt = attr(entry["alt"])

    nav = []
    if prev_entry:
        nav.append(f'          <a class="prev" href="{prev_entry["slug"]}.html">'
                   f'<span class="dir">Previous</span>'
                   f'{attr(prev_entry["title"])}</a>')
    if next_entry:
        nav.append(f'          <a class="next" href="{next_entry["slug"]}.html">'
                   f'<span class="dir">Next</span>'
                   f'{attr(next_entry["title"])}</a>')
    nav_block = ("\n        <nav class=\"article-nav\" aria-label=\"More articles\">\n"
                 + "\n".join(nav) + "\n        </nav>\n") if nav else "\n"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — PowerSlave Developments</title>
  <meta name="description" content="{blurb}">
  <link rel="canonical" href="{SITE}/articles/{slug}.html">

  <meta property="og:type" content="article">
  <meta property="og:site_name" content="PowerSlave Developments">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{blurb}">
  <meta property="og:url" content="{SITE}/articles/{slug}.html">
  <meta property="og:image" content="{SITE}/images/articles/{slug}.jpg">
  <meta property="og:image:width" content="{w}">
  <meta property="og:image:height" content="{h}">
  <meta property="og:image:alt" content="{alt}">
  <meta property="article:published_time" content="{meta['iso']}">
  <meta property="article:author" content="{AUTHOR}">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="alternate" type="application/atom+xml" href="../feed.xml" title="Articles — PowerSlave Developments">
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#0b0d12" media="(prefers-color-scheme: dark)">
  <meta name="theme-color" content="#fbfbfd" media="(prefers-color-scheme: light)">

  <link rel="stylesheet" href="../style.css">

{article_ld(entry, meta, w, h)}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

{chrome("../", "articles.html")}

  <main id="main" class="wrap">
    <article class="article">

      <header class="article-head">
        <p class="eyebrow"><a href="../articles.html">Articles</a></p>
        <h1>{title}</h1>
        <p class="byline"><strong>{AUTHOR}</strong> · Published on LinkedIn</p>
      </header>

      <figure class="article-hero">
        <img src="../images/articles/{slug}.jpg"
             srcset="../images/articles/{slug}-800.jpg 800w,
                     ../images/articles/{slug}.jpg 1600w"
             sizes="(max-width: 760px) 100vw, 720px"
             alt="{alt}" width="{w}" height="{h}">
      </figure>

      <div class="article-body">
{body_to_html(meta['body'])}
      </div>

      <div class="article-foot">{nav_block}        <p><a href="../articles.html">← All articles</a></p>
      </div>

    </article>
  </main>

{footer("../")}
</body>
</html>
"""


def index_page(entries):
    cards = []
    for entry in reversed(entries):          # newest first
        slug, meta = entry["slug"], entry["meta"]
        w, h = dimensions(IMG / f"{slug}.jpg")
        cards.append(f"""        <article class="card post-card">
          <img src="images/articles/{slug}.jpg"
               srcset="images/articles/{slug}-400.jpg 400w,
                       images/articles/{slug}-800.jpg 800w,
                       images/articles/{slug}.jpg 1600w"
               sizes="(max-width: 620px) 100vw, 200px"
               alt="{attr(entry['alt'])}" width="{w}" height="{h}" loading="lazy">
          <div class="post-card-body">
            <h3><a href="articles/{slug}.html">{attr(meta['title'])}</a></h3>
            <p>{attr(entry['blurb'])}</p>
          </div>
        </article>""")

    blurb = attr("Eleven articles on what AI actually changes about senior "
                 "engineering — the hiring funnel, the unbundling of the "
                 "engineering role, and the habits that stop a team "
                 "accelerating in the wrong direction.")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Articles — PowerSlave Developments</title>
  <meta name="description" content="{blurb}">
  <link rel="canonical" href="{SITE}/articles.html">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="PowerSlave Developments">
  <meta property="og:title" content="Articles — PowerSlave Developments">
  <meta property="og:description" content="{blurb}">
  <meta property="og:url" content="{SITE}/articles.html">
  <meta property="og:image" content="{SITE}/images/articles/{entries[-1]['slug']}.jpg">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="alternate" type="application/atom+xml" href="feed.xml" title="Articles — PowerSlave Developments">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#0b0d12" media="(prefers-color-scheme: dark)">
  <meta name="theme-color" content="#fbfbfd" media="(prefers-color-scheme: light)">

  <link rel="stylesheet" href="style.css">

{index_ld(entries)}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

{chrome("", "articles.html")}

  <main id="main" class="wrap">

    <header class="hero">
      <p class="eyebrow">Articles</p>
      <h1>How we think about the work</h1>
      <p class="lede">{blurb}</p>
    </header>

    <section>
      <div class="post-list">
{chr(10).join(cards)}
      </div>
    </section>

    <section>
      <div class="panel center">
        <h2>Want this thinking applied to your codebase?</h2>
        <p class="lede-sm">We take on senior engineering work — architecture reviews, AI-assisted delivery, and teams that need to ship faster than their headcount suggests.</p>
        <a class="email" href="mailto:support@powerslave.dev">support@powerslave.dev</a>
        <p class="note">Or read <a href="services.html">how we engage</a>.</p>
      </div>
    </section>

  </main>

{footer("")}
</body>
</html>
"""


def feed_xml(entries):
    """Atom feed, newest first.

    Atom makes <updated> mandatory on the feed and on every entry, so unlike the
    pages this does carry dates — a feed without them is not a feed. Same call as
    the sitemap's lastmod: machine-readable plumbing, not page furniture.
    """
    newest = max(e["meta"]["iso"] for e in entries)
    items = []
    for e in reversed(entries):
        meta = e["meta"]
        items.append(f"""  <entry>
    <title>{attr(meta['title'])}</title>
    <link href="{SITE}/articles/{e['slug']}.html"/>
    <id>{SITE}/articles/{e['slug']}.html</id>
    <updated>{meta['iso']}T00:00:00Z</updated>
    <summary>{attr(e['blurb'])}</summary>
  </entry>""")
    joined = "\n".join(items)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Articles — PowerSlave Developments</title>
  <subtitle>What AI actually changes about senior engineering.</subtitle>
  <link href="{SITE}/feed.xml" rel="self"/>
  <link href="{SITE}/articles.html"/>
  <id>{SITE}/articles.html</id>
  <updated>{newest}T00:00:00Z</updated>
  <author>
    <name>{AUTHOR}</name>
    <uri>{SITE}/team.html</uri>
  </author>
  <rights>© PowerSlave Developments</rights>

{joined}

</feed>
"""


# --- main --------------------------------------------------------------------

def main():
    entries = []
    for entry in ARTICLES:
        entry = dict(entry)
        entry["meta"] = parse(entry["slug"])
        entry["title"] = entry["meta"]["title"]
        entries.append(entry)

    for i, entry in enumerate(entries):
        prev_entry = entries[i - 1] if i else None
        next_entry = entries[i + 1] if i + 1 < len(entries) else None
        path = OUT / f"{entry['slug']}.html"
        path.write_text(article_page(entry, entry["meta"], prev_entry, next_entry),
                        encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")

    index = ROOT / "articles.html"
    index.write_text(index_page(entries), encoding="utf-8")
    print(f"wrote {index.relative_to(ROOT)}")

    feed = ROOT / "feed.xml"
    feed.write_text(feed_xml(entries), encoding="utf-8")
    print(f"wrote {feed.relative_to(ROOT)}")

    # Google drops the Article rich result when the headline runs long. Say so
    # rather than silently truncating someone's title.
    over = [(e["slug"], len(e["meta"]["title"]))
            for e in entries if len(e["meta"]["title"]) > 110]
    for slug, n in over:
        print(f"note: {slug} headline is {n} chars, over Google's 110-character "
              f"guidance — the Article rich result may be dropped")


if __name__ == "__main__":
    main()
