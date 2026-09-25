"""Builds docs/01_Beyond_the_Crest_Series_Format_Bible.pdf"""
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

OUT = "docs/01_Beyond_the_Crest_Series_Format_Bible.pdf"
GOLD = colors.HexColor("#B8892B")
INK = colors.HexColor("#1B1B1F")
PLUM = colors.HexColor("#3A1F3D")
LIGHT = colors.HexColor("#F4EEE3")

title = ParagraphStyle("t", fontName="Times-Bold", fontSize=34, leading=40,
                       alignment=TA_CENTER, textColor=PLUM)
sub = ParagraphStyle("s", fontName="Times-Italic", fontSize=14, leading=18,
                     alignment=TA_CENTER, textColor=GOLD)
h1 = ParagraphStyle("h1", fontName="Times-Bold", fontSize=18, leading=22,
                    textColor=PLUM, spaceBefore=14, spaceAfter=6)
h2 = ParagraphStyle("h2", fontName="Times-Bold", fontSize=13, leading=16,
                    textColor=GOLD, spaceBefore=10, spaceAfter=4)
body = ParagraphStyle("b", fontName="Times-Roman", fontSize=11, leading=14.5,
                      textColor=INK, spaceAfter=6)
bul = ParagraphStyle("bul", parent=body, leftIndent=16, bulletIndent=4,
                     spaceAfter=3)
answer = ParagraphStyle("a", parent=body, backColor=LIGHT, borderPadding=6,
                        borderColor=GOLD, borderWidth=0.8, spaceBefore=4,
                        spaceAfter=10, fontName="Times-Bold")
cell = ParagraphStyle("c", fontName="Times-Roman", fontSize=9.5, leading=12)
cellb = ParagraphStyle("cb", parent=cell, fontName="Times-Bold",
                       textColor=colors.white)
# screenplay (daytime format) styles
mono = dict(fontName="Courier", fontSize=10, leading=12)
sp_slug = ParagraphStyle("slug", fontName="Courier-Bold", fontSize=10,
                         leading=12, spaceBefore=10, spaceAfter=6)
sp_act = ParagraphStyle("act", fontName="Courier-Bold", fontSize=10,
                        leading=12, alignment=TA_CENTER, spaceBefore=6,
                        spaceAfter=6)
sp_dir = ParagraphStyle("dir", **mono, spaceAfter=6)
sp_char = ParagraphStyle("char", **mono, leftIndent=2.2 * inch)
sp_paren = ParagraphStyle("par", **mono, leftIndent=1.7 * inch)
sp_dial = ParagraphStyle("dial", **mono, leftIndent=1.1 * inch,
                         rightIndent=1.2 * inch, spaceAfter=6)


def P(t, s=body):
    return Paragraph(t, s)


def bullets(items):
    return [Paragraph(i, bul, bulletText="•") for i in items]


def table(rows, widths):
    data = [[Paragraph(str(c), cellb if r == 0 else cell) for c in row]
            for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PLUM),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#C9BFAE")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def scene(slug, lines):
    out = [P(slug, sp_slug)]
    for kind, text in lines:
        if kind == "d":
            out.append(P(text, sp_dir))
        else:
            name, paren, dia = kind, text[0], text[1]
            out.append(P(name, sp_char))
            if paren:
                out.append(P(f"({paren})", sp_paren))
            out.append(P(dia, sp_dial))
    return out


def footer(c, doc):
    c.saveState()
    c.setFont("Times-Italic", 8.5)
    c.setFillColor(colors.grey)
    c.drawString(inch, 0.55 * inch,
                 "BEYOND THE CREST — Series Format Bible — Writers' Room Confidential")
    c.drawRightString(7.5 * inch, 0.55 * inch, f"Page {doc.page}")
    c.restoreState()


story = []

# ---------------- COVER ----------------
story += [Spacer(1, 2.1 * inch),
          P("BEYOND THE CREST", title),
          Spacer(1, 8),
          P("Series Format Bible — Document 01", sub),
          Spacer(1, 30),
          P("A Daytime Drama", ParagraphStyle("x", parent=sub, textColor=INK)),
          Spacer(1, 90),
          P("<b>Series Premiere (in-universe):</b> Monday, January 5, 2026",
            ParagraphStyle("c1", parent=body, alignment=TA_CENTER)),
          P("<b>Setting:</b> A private gated community in affluent metro Atlanta, Georgia",
            ParagraphStyle("c2", parent=body, alignment=TA_CENTER)),
          P("<b>First Family:</b> The Donohues — Victor, Joan, Jasmine, Natasha &amp; Alvin",
            ParagraphStyle("c3", parent=body, alignment=TA_CENTER)),
          PageBreak()]

# ---------------- CANON LOCK ----------------
story += [P("0. Locked Canon (Story Rules)", h1),
          P("These are the standing rules for every document, script, article, and post "
            "produced for <i>Beyond the Crest</i>. They do not change unless the showrunner "
            "changes them in writing."),
          *bullets([
              "<b>Story frame year:</b> 2026 is our storytelling “present.” The story "
              "begins on the premiere date and moves forward in real time from there.",
              "<b>In-universe start date:</b> Monday, January 5, 2026 (Episode #0001).",
              "<b>One layer only:</b> The daytime soap opera <i>is</i> the story. There is no "
              "separate real-world or behind-the-scenes layer.",
              "<b>Storytelling formats:</b> Hollywood media and news media articles and "
              "headlines, social media, and the internet all exist <b>inside the story's "
              "universe</b> and cover the characters and events of the show. Alongside them "
              "runs heavy character-driven dialogue written in screenplay format.",
              "<b>Timeline:</b> Every event carries a date and time. Every character's age "
              "is calculated from a locked birthday on the date of the scene.",
              "<b>Tone:</b> Realistic to real life; creative, entertaining, dramatic, and "
              "original.",
              "<b>Cast:</b> Primarily African American ensemble, with a small number of "
              "non-Black characters.",
              "<b>Deliverables:</b> Every document is delivered as a PDF.",
              "<b>Continuity is paramount:</b> Nothing contradicts established canon. "
              "No character is nerfed — power, wealth, intellect, and status stay "
              "consistent unless the story earns a change on screen.",
          ]),
          P("Premise", h2),
          P("Set in a fictional gated community in the affluent Atlanta area, "
            "<i>Beyond the Crest</i> tells the story of a wealthy Black family in a posh, "
            "gated enclave. At the center is the <b>Donohue Family</b> — <b>Victor, Joan, "
            "Jasmine, Natasha, and Alvin</b> — a powerful and prestigious "
            "multigenerational family known as <b>“Black Royalty.”</b>"),
          P("Character profiles, birthdays, and ages will be locked in Document 02 once "
            "the showrunner delivers the cast.", body),
          ]

# ---------------- 1. EPISODES PER YEAR ----------------
story += [P("1. Episodes Per Year", h1),
          P("RECOMMENDATION: 250 original episodes per broadcast year.", answer),
          P("American daytime dramas air five days a week, Monday through Friday, all year "
            "with no summer hiatus. A calendar has 260–261 weekdays. Subtract about six "
            "network holidays (Thanksgiving, Christmas, New Year's Day, Memorial Day, "
            "Independence Day, Labor Day) and a few sports and breaking-news preemptions, "
            "and you land on roughly <b>250 new episodes</b>. That matches the output of "
            "long-running network soaps like <i>The Young and the Restless</i> and "
            "<i>General Hospital</i>."),
          table([
              ["Item", "Count"],
              ["Weekdays in a broadcast year", "~261"],
              ["Holiday dark days (encore or pre-empted)", "~6"],
              ["Sports / news pre-emptions (average)", "~3–5"],
              ["<b>Original episodes</b>", "<b>250</b>"],
              ["Weekly cadence", "5 episodes (Mon–Fri)"],
              ["Production pace", "~5–6 episodes taped per week, ~6 weeks ahead of air"],
          ], [4.2 * inch, 2.3 * inch]),
          ]

# ---------------- 2. SEASON NUMBERING ----------------
story += [P("2. Season Numbering", h1),
          P("RECOMMENDATION: Seasons follow the September–August network broadcast "
            "year. Episodes are numbered continuously for the life of the show and never "
            "reset.", answer),
          P("Real daytime soaps don't reset to “Episode 1” each season. The on-screen "
            "and industry identity of an episode is its <b>cumulative episode number plus "
            "its air date</b> (for example, a long-running soap passing Episode #13,000). "
            "“Seasons” exist only as bookkeeping for the network's September–August "
            "broadcast year, which also governs the Daytime Emmy eligibility window."),
          P("Because <i>Beyond the Crest</i> premieres in January, it gets a realistic "
            "<b>shortened launch season</b> that wraps the week before Labor Day. After that, "
            "it runs on the standard broadcast calendar:"),
          table([
              ["Season", "Broadcast Window", "Episodes", "Episode #s"],
              ["Season 1 (launch)", "Mon, Jan 5, 2026 – Fri, Sep 4, 2026", "170",
               "#0001 – #0170"],
              ["Season 2", "Tue, Sep 8, 2026 – Fri, Sep 3, 2027", "250",
               "#0171 – #0420"],
              ["Season 3", "Tue, Sep 7, 2027 – early Sep 2028", "250",
               "#0421 – #0670"],
              ["Each season after", "Tuesday after Labor Day – Friday before Labor Day",
               "250", "+250 per season"],
          ], [1.3 * inch, 2.7 * inch, 0.8 * inch, 1.7 * inch]),
          Spacer(1, 6),
          P("<b>Season 1 math:</b> 175 weekdays from Jan 5 to Sep 4, 2026, minus Memorial Day "
            "(May 25) and Independence Day observed (Fri, Jul 3), minus about 3 "
            "sports/news pre-emptions = <b>170 episodes</b>."),
          P("<b>Season 2 math:</b> 259 weekdays from Sep 8, 2026 to Sep 3, 2027, minus "
            "Thanksgiving (Nov 26), Black Friday (Nov 27), Christmas (Fri, Dec 25), "
            "New Year's Day (Fri, Jan 1), Memorial Day (May 31), and Independence Day "
            "observed (Mon, Jul 5), minus about 3 pre-emptions = <b>250 episodes</b>."),
          P("Labor Day itself (Mon, Sep 7, 2026) is the realistic changeover point: it airs "
            "an encore, and the new season opens Tuesday."),
          P("<b>How it's written on every document:</b> <font name='Courier'>BEYOND THE CREST "
            "— Episode #0001 — Season 1 — Monday, January 5, 2026</font>"),
          ]

# ---------------- 3. SERIALIZED VS STANDALONE ----------------
story += [P("3. Serialized vs. Standalone Split", h1),
          P("RECOMMENDATION: 90% serialized / 10% standalone-leaning. There are no true "
            "standalones: every episode moves continuity forward.", answer),
          P("A daytime soap is the most serialized format in television. Stories braid "
            "across weeks, months, and years, and the audience expects yesterday's cliffhanger "
            "to be answered today. The 10% is reserved for <b>“event” episodes</b>: they "
            "have a self-contained shape but still advance at least one long-term arc and are "
            "fully canon. That works out to about <b>25 per broadcast year</b>, or roughly two "
            "a month:"),
          *bullets([
              "Holiday episodes (Thanksgiving at the Donohue estate, Christmas Eve gala, "
              "New Year's Eve).",
              "Flashback and origin episodes (how Victor built the empire; the Donohues in "
              "earlier decades).",
              "Character-spotlight or “bottle” episodes (a single location or a two-hander "
              "confrontation).",
              "Tentpole events: weddings, funerals, trials, galas, and milestone anniversaries "
              "(Episode #0250, #0500, #1000).",
          ]),
          P("Continuity controls", h2),
          *bullets([
              "<b>Show Bible master timeline:</b> every scene logged with date, time, "
              "location, and characters present.",
              "<b>Age ledger:</b> birthdays locked; ages recomputed on the air date of each "
              "scene.",
              "<b>Story arc tracker:</b> long-term (6–18 months), mid-term (6–12 weeks), and "
              "short-term (1–3 weeks) arcs, cross-referenced by episode number.",
              "<b>Recap rule:</b> no scene contradicts a prior aired scene; any retcon must be "
              "explained on screen.",
          ]),
          ]

# ---------------- 4. GENRE / RATING / RUNTIME ----------------
story += [P("4. Genre, Subgenres, Rating &amp; Runtime", h1),
          table([
              ["Element", "Recommendation"],
              ["Primary genre", "Daytime drama (soap opera), a continuing serial drama"],
              ["Subgenres",
               "Family dynasty saga • Wealth &amp; power drama (“Black Royalty”) • "
               "Romance &amp; romantic triangles • Corporate / boardroom intrigue • "
               "Legal &amp; political drama • Mystery / suspense (whodunit arcs) • "
               "Melodrama"],
              ["Rating", "<b>TV-14</b>, with content descriptors (D, L, S, V) applied per "
               "episode. That is today's standard for prime daytime dramas and allows adult "
               "stakes without prime-time explicitness."],
              ["Runtime", "<b>60-minute time slot</b>, about <b>42 minutes</b> of story "
               "content plus about 18 minutes of commercials and network promos"],
              ["Format", "Multi-camera, taped “as live” on soundstage sets with "
               "occasional location remotes (Atlanta exteriors, galas, weddings)"],
              ["Timeslot", "Weekdays, 12:30 PM or 1:00 PM ET / PT (network daytime block)"],
          ], [1.4 * inch, 5.1 * inch]),
          ]

# ---------------- 5. EPISODE TITLES ----------------
story += [P("5. Episode Titling", h1),
          P("RECOMMENDATION: No on-air episode titles. Each episode is identified by "
            "number and air date, with a one-line logline for listings. An internal "
            "working title is used in the writers' room only.", answer),
          P("That's how real daytime soaps work. Episodes aren't titled on screen; networks, "
            "TV listings, and soap magazines identify them by <b>air date</b> and describe "
            "them with a short <b>logline</b>. Writers' rooms often keep informal working "
            "titles for tracking."),
          table([
              ["Field", "Example"],
              ["Official ID", "Episode #0001 — Monday, January 5, 2026"],
              ["Production code", "BTC-S01-0001"],
              ["Listing logline",
               "Victor Donohue makes a stunning announcement at the family's New Year gala."],
              ["Internal working title (room only)", "“The Crown on the Hill”"],
          ], [2.2 * inch, 4.3 * inch]),
          ]

# ---------------- 6. SCRIPT LENGTH / ACTS / SCENES ----------------
story += [PageBreak(),
          P("6. Script Length, Acts &amp; Scenes", h1),
          P("RECOMMENDATION: 85–95 pages (target 90), a Teaser plus 6 Acts, and "
            "22–26 scenes (target 24) per episode.", answer),
          P("Daytime scripts run much longer per minute than prime-time screenplays. The "
            "pages are almost all dialogue, written in the wider daytime script format, and "
            "an hour-long soap usually delivers about 2 pages per minute of screen time. Each "
            "episode braids <b>4–5 storylines</b> (A, B, C, D, and sometimes a runner), "
            "and each act ends on a hook before a commercial break. Act 6 ends on the "
            "episode's cliffhanger, the “Friday hook” being the biggest of the week."),
          table([
              ["Segment", "Pages", "Screen Time", "Scenes", "Purpose"],
              ["Teaser (Cold Open)", "5–6", "~3 min", "1–2",
               "Pick up yesterday's cliffhanger; hook the audience"],
              ["Main Title", "—", "~0:30", "—", "Opening credits &amp; theme"],
              ["Act 1", "14–15", "~6.5 min", "4", "Establish today's A/B/C stories"],
              ["Act 2", "14–15", "~6.5 min", "4", "Complications; introduce D story"],
              ["Act 3", "14–15", "~6.5 min", "4", "Midpoint turn / confrontation"],
              ["Act 4", "14–15", "~6.5 min", "4", "Escalation; secrets surface"],
              ["Act 5", "13–14", "~6.5 min", "3–4", "Collisions between storylines"],
              ["Act 6", "10–12", "~6 min", "3", "Payoffs and the closing cliffhanger"],
              ["<b>TOTAL</b>", "<b>~90</b>", "<b>~42 min</b>", "<b>~24</b>",
               "4–5 storylines braided"],
          ], [1.3 * inch, 0.65 * inch, 0.9 * inch, 0.65 * inch, 3.0 * inch]),
          Spacer(1, 8),
          P("Each episode also carries: a title page (episode #, production code, air date, "
            "in-universe date/time span), a <b>cast list with ages as of the episode date</b>, "
            "a sets list, and a scene breakdown."),
          ]

# ---------------- 7. MULTI-PLATFORM STORYTELLING ----------------
story += [P("7. Multi-Platform Storytelling Toolkit", h1),
          P("The soap opera is the story. Every article, headline, post, and web page "
            "below exists <b>inside the story's universe</b>, written by in-universe "
            "outlets, reporters, and users about in-universe people and events. Nothing "
            "here is real-world coverage of the show. Every item is timestamped and canon, "
            "and what the characters read, post, or see online can drive the plot."),
          table([
              ["Format", "In-Universe Use"],
              ["Screenplay scenes", "Primary vehicle; character-driven dialogue"],
              ["Hollywood media", "Entertainment and celebrity press covering the Donohues and "
               "other characters: galas, red carpets, celebrity relationships, and any "
               "family ventures in film, music, fashion, or media"],
              ["News media", "Atlanta and national news, business and financial press on "
               "Donohue holdings, society pages, politics, crime and court coverage, "
               "legal filings"],
              ["Social media", "Characters' own posts, DMs, and livestreams; public reactions; "
               "trending hashtags about the family and the community"],
              ["Internet", "Gossip blogs, message boards, anonymous leak sites, search "
               "results, viral videos, online reviews"],
          ], [1.9 * inch, 4.6 * inch]),
          ]

# ---------------- 8. SAMPLE SCRIPT FORMAT ----------------
story += [PageBreak(),
          P("8. Script Page Format Sample", h1),
          P("A format illustration only, not canon dialogue. Canon scenes will be written "
            "once the cast is locked.", ParagraphStyle("i", parent=body,
                                                       fontName="Times-Italic")),
          P("BEYOND THE CREST", sp_act),
          P("EPISODE #0001 — PROD. BTC-S01-0001", sp_act),
          P("AIR DATE: MONDAY, JANUARY 5, 2026", sp_act),
          P("TEASER", sp_act),
          *scene("1. INT. DONOHUE ESTATE — GRAND FOYER — NIGHT (MON 1/5/26, 8:02 PM)", [
              ("d", "Crystal. Marble. Old money that is <i>ours</i>. A string quartet plays "
                    "beneath the sweeping staircase. GUESTS in black tie turn as a figure "
                    "appears on the landing."),
              ("CHARACTER A", ("low, to Character B", "He only comes down those stairs "
                               "when he's about to change somebody's life.")),
              ("CHARACTER B", ("", "Then let's hope it's not ours.")),
              ("d", "Glasses rise. The music stops. Every eye goes to the top of the stairs."),
          ]),
          P("CUT TO: MAIN TITLE", sp_act),
          ]

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=inch, rightMargin=inch,
                        topMargin=0.9 * inch, bottomMargin=0.9 * inch,
                        title="Beyond the Crest — Series Format Bible",
                        author="Beyond the Crest Writers' Room")
doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=footer)
print("wrote", OUT)
