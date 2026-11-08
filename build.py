"""Builds Frances Okeke's site into ./public.

To add a piece: add an entry to CONTENT, write its page (copy a file from templates/), then run
    python3 build.py
"""
import pathlib, html

ROOT = pathlib.Path(__file__).parent / "public"

NAV = [("Investigations", "investigations/"), ("Field notes", "field-notes/"),
       ("Building", "building.html"), ("About", "about.html"), ("CV", "cv.html")]

TOPICS = [("cancelling", "Cancelling", "Why is it so hard to cancel?"),
          ("complaining", "Complaining", "What makes a complaint feel heard?"),
          ("switching", "Switching", "Why do people stay with providers they're unhappy with?"),
          ("moving", "Moving home", "Why does a new address take a dozen separate updates?")]
TOPIC_NAME = {s: n for s, n, _ in TOPICS}

# status: "in-progress" or "published"
CONTENT = [
    dict(section="Investigations", title="Why is it so hard to cancel a subscription?",
         summary="Exit friction in cancellation journeys, and what the rules now expect of businesses.",
         topics=["cancelling"], status="in-progress", href="investigations/exit-friction.html"),
]
STATUS = {"in-progress": "In progress", "published": "Published"}


def page(path, title, description, body, current=None, crumbs=None, article=False):
    depth = path.count("/")
    up = "/" if path == "404.html" else "../" * depth
    link = lambda h: f'{up}{h}{"index.html" if h.endswith("/") else ""}'
    nav = "\n".join(
        f'          <li{" class=\"cv\"" if l == "CV" else ""}><a href="{link(h)}"{" aria-current=\"page\"" if l == current else ""}>{l}</a></li>'
        for l, h in NAV)
    crumb_html = ""
    if crumbs:
        parts = [f'<li><a href="{up}index.html">Home</a></li>']
        for label, href in crumbs:
            parts.append(f'<li><a href="{link(href)}">{label}</a></li>' if href else f'<li aria-current="page">{label}</li>')
        crumb_html = f'      <nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>\n'
    doc = f"""<!DOCTYPE html>
<html lang="en-GB" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" href="{up}assets/fo-line-mark.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Literata:opsz,wght@7..72,400;7..72,500;7..72,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{up}styles.css">
  <script src="{up}site.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
{'  <div class="progress" aria-hidden="true"></div>' if article else ''}
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{up}index.html"><img src="{up}assets/fo-line-mark.svg" alt="" width="52" height="26">Frances Okeke</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav"><span>Menu</span></button>
      <nav class="nav" id="site-nav" aria-label="Main">
        <ul>
{nav}
        </ul>
      </nav>
    </div>
  </header>
  <main id="main">
    <div class="wrap">
{crumb_html}{body}
    </div>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <p>Frances Okeke, Glasgow. Follow the question to the fix.</p>
      <ul>
{chr(10).join(f'        <li><a href="{link(h)}">{l}</a></li>' for l, h in NAV)}
        <li><a href="#main">Back to top</a></li>
      </ul>
    </div>
  </footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)


def item(c, up):
    names = ", ".join(TOPIC_NAME[t] for t in c["topics"])
    return f"""        <li class="item" data-topics="{' '.join(c['topics'])}">
          <div class="meta"><span class="status {c['status']}">{STATUS[c['status']]}</span><span>{names}</span></div>
          <h3><a href="{up}{c['href']}">{html.escape(c['title'])}</a></h3>
          <p>{html.escape(c['summary'])}</p>
        </li>"""


HERO_LINE = """      <div class="hero-line" aria-hidden="true">
        <svg viewBox="0 0 1000 120" preserveAspectRatio="xMinYMid meet">
          <path class="route draw" d="M64 92 C26 92 20 30 60 28 C100 26 106 86 72 94 C56 98 92 106 142 88 C262 46 362 46 482 70 C602 94 690 94 782 72"/>
          <line class="tick fade" x1="806" y1="50" x2="806" y2="88"/>
          <path class="route draw" style="animation-delay:2.2s;animation-duration:.6s" d="M830 68 C870 60 900 74 930 74"/>
          <circle class="fix fade" style="animation-delay:2.7s" cx="950" cy="74" r="12"/>
        </svg>
      </div>"""

journeys = "\n".join(
    f'          <li><a href="investigations/index.html#{s}"><span class="name">{n}</span><span class="q">{q}</span></a></li>'
    for s, n, q in TOPICS)

# ---------------- Home ----------------
page("index.html", "Frances Okeke: where customer journeys break",
     "Frances Okeke investigates where customer journeys break, the rules that govern them and the design changes that fix them.", f"""
      <section class="hero" aria-labelledby="hero-title">
        <h1 id="hero-title">Where customer journeys break, and how to fix them.</h1>
        <p class="lede">I'm Frances Okeke, a product and customer experience researcher in Glasgow. I investigate the moments customers find hardest, the rules that govern them and the design changes that make them easier.</p>
{HERO_LINE}
        <h2 class="small muted" style="font-family:var(--sans);font-weight:400;font-size:.95rem;margin:var(--space-8) 0 var(--space-4)">Four journeys I investigate</h2>
        <ul class="journeys">
{journeys}
        </ul>
        <div class="actions">
          <a class="btn btn-primary" href="investigations/index.html">Read the investigations</a>
          <a class="btn" href="cv.html">View my CV</a>
        </div>
      </section>

      <section class="section" aria-labelledby="readers-title">
        <h2 id="readers-title">Start where it's useful to you</h2>
        <div class="readers">
          <div><h3>If you're hiring</h3><p>My experience, qualifications and the way I work, on one page.</p><a href="cv.html">See my CV</a></div>
          <div><h3>If you research or design journeys</h3><p>Questions followed through to evidence and a fix, with sources.</p><a href="investigations/index.html">Read the investigations</a></div>
          <div><h3>If you're building something</h3><p>The ventures that grew out of this work.</p><a href="building.html">See what I'm building</a></div>
        </div>
      </section>

      <section class="section" aria-labelledby="method-title">
        <h2 id="method-title">How I follow a question</h2>
        <ol class="method">
          <li><h3>Notice</h3><p>Spot the moment a customer gets stuck.</p></li>
          <li><h3>Investigate</h3><p>Walk the journey, count the steps and read the rules.</p></li>
          <li><h3>Reframe</h3><p>Ask what the business and the customer each actually need.</p></li>
          <li><h3>Fix</h3><p>Design the simpler version and say how to measure it.</p></li>
        </ol>
      </section>

      <section class="section" aria-labelledby="latest-title">
        <h2 id="latest-title">Latest</h2>
        <ul class="list">
{chr(10).join(item(c, "") for c in CONTENT[:3])}
        </ul>
      </section>

      <section class="section faq measure" aria-labelledby="faq-title">
        <h2 id="faq-title">About this site</h2>
        <details><summary>What is an investigation?</summary><div><p>A question about one customer journey, followed through: what happens today, what the rules say, where it breaks and what a better version looks like. Every claim is sourced.</p></div></details>
        <details><summary>What do "In progress" and "Published" mean?</summary><div><p>"In progress" means I'm still researching or writing it, so please don't quote it yet. "Published" means it's finished and sourced.</p></div></details>
        <details><summary>What are field notes?</summary><div><p>Shorter pieces: what I'm learning, plus a monthly roundup of regulation and customer experience news with a short note on why each item matters.</p></div></details>
      </section>

      <section class="section contact" aria-labelledby="contact-title">
        <div class="inner">
          <h2 id="contact-title">Is a journey breaking somewhere you work?</h2>
          <p class="muted">I'm glad to talk about research, collaboration, roles and speaking.</p>
          <a class="btn" href="about.html#contact">Get in touch</a>
        </div>
      </section>
""")

# ---------------- Investigations ----------------
chips = "\n".join(['        <button class="chip" type="button" data-topic="all" aria-pressed="true">All</button>'] +
                  [f'        <button class="chip" type="button" data-topic="{s}" aria-pressed="false">{n}</button>' for s, n, _ in TOPICS])
inv = [c for c in CONTENT if c["section"] == "Investigations"]
page("investigations/index.html", "Investigations: Frances Okeke",
     "Customer journey investigations: one question followed through to evidence and a fix.", f"""
      <header class="page-head measure">
        <h1>Investigations</h1>
        <p class="lede">Each one starts with a question a customer would ask, then follows it through: what happens today, what the rules say, where it breaks and what a better version looks like.</p>
      </header>
      <fieldset class="filters">
        <legend>Show journeys about</legend>
{chips}
      </fieldset>
      <p class="result-count" aria-live="polite"></p>
      <ul class="list">
{chr(10).join(item(c, "../") for c in inv)}
      </ul>
      <div class="empty" hidden>
        <p>Nothing on <strong class="empty-topic"></strong> yet. It's on the list.</p>
        <p><button type="button">Show all investigations</button></p>
      </div>
""", current="Investigations", crumbs=[("Investigations", None)])

page("investigations/exit-friction.html", "Why is it so hard to cancel a subscription? Frances Okeke",
     "Exit friction in subscription cancellation journeys.", """
      <article class="article">
        <div class="meta"><span class="status in-progress">In progress</span><span>Cancelling</span></div>
        <h1>Why is it so hard to cancel a subscription?</h1>
        <p class="lede"><span class="todo">One or two sentences on the main finding.</span></p>
        <nav class="toc" aria-label="On this page">
          <p>On this page</p>
          <ol>
            <li><a href="#why">Why this matters</a></li>
            <li><a href="#rules">What the rules say</a></li>
            <li><a href="#found">What I found</a></li>
            <li><a href="#fix">The fix</a></li>
            <li><a href="#sources">Sources</a></li>
          </ol>
        </nav>
        <h2 id="why">Why this matters</h2>
        <p><span class="todo">The customer problem in plain words. Who it affects and how often.</span></p>
        <h2 id="rules">What the rules say</h2>
        <p><span class="todo">The relevant regulation in plain English, with a link to the official source for every claim.</span></p>
        <h2 id="found">What I found</h2>
        <p><span class="todo">Your evidence: journeys walked, steps counted, screenshots and data.</span></p>
        <h2 id="fix">The fix</h2>
        <p><span class="todo">What a business could change, and how to measure whether it worked.</span></p>
        <h2 id="sources">Sources</h2>
        <ol><li><span class="todo">Official source, with link</span></li></ol>
        <div class="next">
          <p><strong>Where next?</strong></p>
          <p><a href="index.html">All investigations</a> or <a href="../field-notes/index.html">field notes</a></p>
        </div>
      </article>
""", current="Investigations", crumbs=[("Investigations", "investigations/"), ("Cancelling a subscription", None)], article=True)

# ---------------- Field notes ----------------
page("field-notes/index.html", "Field notes: Frances Okeke",
     "Short notes on what I'm learning, plus a monthly roundup.", """
      <header class="page-head measure">
        <h1>Field notes</h1>
        <p class="lede">Shorter pieces: what I'm learning about product, research and building something new, plus a monthly roundup of regulation and customer experience news.</p>
      </header>
      <div class="empty measure">
        <p><strong>The first field notes are on their way.</strong></p>
        <p>In the meantime, <a href="../investigations/index.html">read the investigations</a>.</p>
      </div>
""", current="Field notes", crumbs=[("Field notes", None)])

# ---------------- Building ----------------
page("building.html", "Building: Frances Okeke",
     "Ventures that grew out of Frances Okeke's investigations.", """
      <header class="page-head measure">
        <h1>Building</h1>
        <p class="lede">Some investigations end in a fix that a business can make. Others end in something that needs building.</p>
      </header>
      <ul class="list measure">
        <li class="item">
          <div class="meta"><span class="status in-progress">In development</span><span>CXInsight Ltd</span></div>
          <h3>AxeoMove</h3>
          <p><span class="todo">One or two sentences: the problem it solves and who it is for. Add a link to its own site when it has one.</span></p>
        </li>
        <li class="item">
          <div class="meta"><span>Company</span></div>
          <h3>CXInsight Ltd</h3>
          <p>A consulting company in Scotland, which I founded and run. It's the home for my client work and for AxeoMove.</p>
        </li>
      </ul>
""", current="Building", crumbs=[("Building", None)])

# ---------------- About ----------------
page("about.html", "About: Frances Okeke", "About Frances Okeke, a product and customer experience researcher in Glasgow.", """
      <header class="page-head measure">
        <h1>Hello, I'm Frances.</h1>
        <p class="lede">I'm a product and customer experience researcher based in Glasgow.</p>
      </header>
      <div class="measure">
        <p>I've spent more than ten years in customer experience, operations and product research across telecoms, travel and technology. That work showed me where customer journeys tend to break: cancellations, complaints and the moments when someone just wants something sorted.</p>
        <p>Now I investigate how UK consumer protection rules shape those journeys, and I build things that make them easier. I'm the founder of CXInsight Ltd.</p>
        <p>The line in my logo comes from uli, the line art of Igbo women, where the line leads and empty space matters as much as what is drawn. It's how I like to work: one clear line of thought, and room to think.</p>
        <p><a href="cv.html">See my full CV</a></p>
      </div>

      <section class="section contact" id="contact" aria-labelledby="contact-title">
        <div class="inner">
          <h2 id="contact-title">Get in touch</h2>
          <p class="muted">For research, collaboration, roles or speaking.</p>
          <div class="actions">
            <button class="btn btn-primary" type="button" data-copy="EMAIL_ADDRESS">Copy my email address</button>
            <a class="btn" href="LINKEDIN_URL">LinkedIn</a>
          </div>
          <p class="copy-status" aria-live="polite"></p>
          <p class="small"><span class="todo">Replace EMAIL_ADDRESS and LINKEDIN_URL in build.py (About section), then run python3 build.py.</span></p>
        </div>
      </section>
""", current="About", crumbs=[("About", None)])

# ---------------- CV ----------------
page("cv.html", "CV: Frances Okeke", "Frances Okeke's CV: experience, education and certifications.", """
      <header class="page-head measure">
        <h1>CV</h1>
        <p class="lede">Product and customer experience professional with more than ten years across customer experience, case investigation, product research and operational process improvement.</p>
        <p class="small"><span class="todo">Add a downloadable PDF: save it as public/cv.pdf and add a "Download CV (PDF)" link here.</span></p>
      </header>

      <section aria-labelledby="exp-title">
        <h2 id="exp-title">Experience</h2>
        <dl class="cv-grid">
          <dt><span class="todo">Dates</span></dt><dd><strong>Specialist Care Advisor, Executive Office</strong><br><span class="muted">VodafoneThree</span></dd>
          <dt><span class="todo">Dates</span></dt><dd><strong><span class="todo">Role</span></strong><br><span class="muted">Three UK</span></dd>
          <dt><span class="todo">Dates</span></dt><dd><strong><span class="todo">Role</span></strong><br><span class="muted">Jet2</span></dd>
          <dt><span class="todo">Dates</span></dt><dd><strong>Product Researcher</strong><br><span class="muted">Seamfix</span></dd>
          <dt><span class="todo">Dates</span></dt><dd><strong><span class="todo">Role</span></strong><br><span class="muted">Vovida Communications</span></dd>
          <dt><span class="todo">Dates</span></dt><dd><strong><span class="todo">Role</span></strong><br><span class="muted">Smile Communications</span></dd>
          <dt>From Feb 2015</dt><dd><strong><span class="todo">Role</span></strong><br><span class="muted">AGL Consulting</span></dd>
          <dt>Ongoing</dt><dd><strong>Founder</strong><br><span class="muted">CXInsight Ltd</span></dd>
        </dl>
      </section>

      <section class="section" aria-labelledby="edu-title">
        <h2 id="edu-title">Education</h2>
        <dl class="cv-grid">
          <dt>MBA</dt><dd>Global MBA, Glasgow Caledonian University</dd>
          <dt>MSc</dt><dd>Operations and Production Management<span class="todo">, institution</span></dd>
          <dt>BSc</dt><dd>Business Administration<span class="todo">, institution</span></dd>
        </dl>
      </section>

      <section class="section" aria-labelledby="cert-title">
        <h2 id="cert-title">Certifications and training</h2>
        <dl class="cv-grid">
          <dt>Product</dt><dd>Certified Scrum Product Owner (CSPO)</dd>
          <dt>UX</dt><dd>Certificate in AI Fundamentals for UX, UX Design Institute (2026)</dd>
          <dt>Design</dt><dd>Product Design bootcamp</dd>
          <dt>Analysis</dt><dd>Business Analysis Essentials, CBAP preparation course, Certification Edge (2025)</dd>
        </dl>
      </section>
""", current="CV", crumbs=[("CV", None)])

# ---------------- 404 ----------------
page("404.html", "Page not found: Frances Okeke", "Page not found", """
      <header class="page-head measure">
        <h1>This page doesn't exist</h1>
        <p class="lede">The link may be out of date, or the address may have a typo. These might help:</p>
      </header>
      <ul class="measure">
        <li><a href="/investigations/index.html">Investigations</a></li>
        <li><a href="/cv.html">CV</a></li>
        <li><a href="/index.html">Homepage</a></li>
      </ul>
""")
print("built")
