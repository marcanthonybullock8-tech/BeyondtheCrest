"""Builds docs/07_Cast_Categories_and_Opening_Credits.pdf"""
from collections import Counter

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from btc_pdf import P, h1, h2, italic, answer, bullets, table, age_on, build, cover
from cast import CAST, CATEGORIES, CORE, FEATURED, UNIQUE_SEQUENCES, ALVIN_JOINS
from season1_episodes import EPISODES, full_cast, season1_calendar

OUT = "docs/07_Cast_Categories_and_Opening_Credits.pdf"

cal = season1_calendar()
counts, first = Counter(), {}
for n in range(1, len(EPISODES) + 1):
    for c in full_cast(n):
        counts[c] += 1
        first.setdefault(c, n)

story = cover("Cast, Categories &amp; Opening Credits — Document 07", [
    "<b>Season 1:</b> Episodes #0001–#0170",
    "<b>Monday, January 5, 2026 – Friday, September 4, 2026</b>",
    f"<b>Total characters:</b> {len(CAST)}",
])
story.append(PageBreak())

story += [
    P("How to Read This Document", h1),
    *bullets([
        "Characters are grouped by contract category, the way a real daytime soap's "
        "casting office tracks them.",
        "<b>Episode counts are computed from the Season 1 episode guide (Document 09)</b>: "
        "each episode's headline cast plus its scheduled runner scenes. They will always "
        "match the guide.",
        "Main character doesn't mean every episode. Focus rotates: a contract player can "
        "be off for a week and then carry the next.",
        "Ages are as of the premiere, Monday, January 5, 2026.",
        "Alvin Donohue joins in Ep #0085 (Wed, May 6, 2026), the halfway point of the "
        "season. Theodore Donohue and his family arrive in the final four episodes "
        "(Eps #0167–#0170) and become Core cast in Season 2.",
    ]),
    P("Category Guide", h2),
    table([
        ["Category", "What it means", "Typical Season 1 episodes"],
        [CORE, "Top-billed contract players in the opening credits", "57–130"],
        [FEATURED, "Contract players carrying major arcs, credited on an “Also "
                   "Starring” card", "39–52"],
        ["Recurring", "Regular non-contract roles that return throughout the season",
         "3–20"],
        ["Supporting", "Family, colleagues, and world-builders who pop in", "1–5"],
        ["Day Players", "One- or two-day roles", "1–2"],
        ["Guest Stars", "Special roles: flashback casting and Season 2 arrivals", "1–4"],
    ], [1.6 * inch, 3.3 * inch, 1.6 * inch]),
    PageBreak(),
]

for cat in CATEGORIES:
    members = sorted((k for k, v in CAST.items() if v[3] == cat),
                     key=lambda k: (-counts[k], CAST[k][0]))
    rows = [["Character", "Born", "Age", "Role", "S1 Eps", "First"]]
    for k in members:
        name, born, died, _, group, role = CAST[k]
        age = str(age_on(born)) if died is None else "—"
        if k.startswith("Y") or k in ("OS", "HW"):
            age = "—"
        rows.append([name, f"{born:%b} {born.day}, {born.year}", age, role,
                     str(counts[k]), f"#{first[k]:04d}" if k in first else "—"])
    story += [P(f"{cat} ({len(members)})", h1),
              table(rows, [1.55 * inch, 0.95 * inch, 0.4 * inch, 2.4 * inch,
                           0.5 * inch, 0.6 * inch])]
    if cat == CORE:
        story.append(P(f"Alvin's count covers Eps #0085–#0170 only: {counts['AL']} of "
                       f"{len(EPISODES) - ALVIN_JOINS + 1} possible episodes.", italic))
    story.append(Spacer(1, 8))

# ---------------- OPENING CREDITS ----------------
core = [k for k, v in CAST.items() if v[3] == CORE]
ensemble = sorted((k for k in core if k not in UNIQUE_SEQUENCES and k != "AL"),
                  key=lambda k: CAST[k][0].replace("Det. ", "").replace("Dr. ", "").split()[-1])
featured = sorted((k for k, v in CAST.items() if v[3] == FEATURED),
                  key=lambda k: CAST[k][0].split()[-1])

story += [
    PageBreak(),
    P("The Opening Credits", h1),
    P("The main titles run about 60 seconds, set to the theme <i>“Beyond the "
      "Crest”</i>: strings, a gospel choir, and a slow 808 heartbeat. Only the Core "
      "/ Contract cast appears in the main titles. Victor, Joan, Natasha, and Jasmine each "
      "get their own unique sequence. Everyone else shares the ensemble sequence. "
      "Featured Contract players appear on an “Also Starring” card at the end.",
      answer),
    P("1. Victor Donohue: “The King”", h2),
    P("Dawn over Belmont Crest. The camera climbs the Summit House grand staircase to find "
      "Victor at the top, silhouetted against a stained-glass window of the 1939 Beacon "
      "press. He turns the brass key to that press in his fingers and looks straight "
      "down the lens. <b>VICTOR DONOHUE</b> is stamped across the screen in gold "
      "type."),
    P("2. Joan Donohue: “The Queen Mother”", h2),
    P("The Summit House rose garden. Joan in white, pouring tea into two cups. Behind her, "
      "a wall of framed Emmy, Grammy, Oscar, and Tony photos. She sets down the second "
      "cup for someone not yet in frame, and smiles like she knows exactly who's coming. "
      "<b>JOAN DONOHUE</b> in rose-gold script."),
    P("3. Natasha Bullock: “The Queen Regent”", h2),
    P("The top-floor boardroom of Donohue Tower, the Atlanta skyline at night. A red-carpet "
      "flashbulb freezes into a stock-ticker glow. Natasha walks the length of the "
      "boardroom table in stilettos as 30 board members stand. She places her new Oscar "
      "at the head of the table. <b>NATASHA BULLOCK</b> in bold silver type."),
    P("4. Congresswoman Jasmine Olson: “The Firstborn”", h2),
    P("The steps of the U.S. Capitol, then the Georgia State Capitol dome. Jasmine at a "
      "podium, a sea of campaign signs. She takes off her reading glasses mid-speech and "
      "the crowd roars. A final beat: she looks back toward the Summit House portrait "
      "wall, where she was always first. <b>JASMINE OLSON</b> in navy-and-gold "
      "type."),
    P(f"5. Alvin Donohue: “The Wild Card” (added from Ep #{ALVIN_JOINS:04d})", h2),
    P("A helicopter swoops over the Riviera, then over Belmont Crest. Alvin on a yacht deck "
      "at midnight, then in a smoky back room shaking hands with men whose faces we never "
      "see, then on a VIP balcony with champagne raining down. He tips his sunglasses "
      "down and winks. <b>ALVIN DONOHUE</b> in neon-gold type that flickers once, like "
      "it's up to something. Starting with Ep #0085, his sequence plays right after "
      "Jasmine's."),
    P("6. The Ensemble Sequence", h2),
    P("One continuous gliding shot through the Belmont Crest gates: the Summit House "
      "fountain, the Country Club terrace, the 18th green above the Chattahoochee, "
      "Midtown's towers, a Westbrook Academy hallway, APD headquarters, a courtroom, and "
      "Tuxedo Park across the ridge. Each actor appears in a single signature moment, "
      "with their name in white serif type, in alphabetical order by last name:"),
    table([["Order", "Credit", "Signature moment"]] + [
        [str(i + 1), CAST[k][0].upper(), MOMENT] for i, (k, MOMENT) in enumerate(
            (k, {
                "LY": "Lyric twirls on a soundstage under one spotlight",
                "AM": "Amond fastens his cufflinks, eyes on the camera",
                "RB": "Robert snaps a briefcase shut in an empty courtroom",
                "MA": "Marc-Anthony laughs on a red carpet, then turns, and his smile "
                      "goes cold",
                "GR": "Grace sings one note on a Broadway stage",
                "AR": "Arianna takes the oath with her hand on a Bible",
                "HD": "Harmony frames a shot with her fingers, alone on a rooftop",
                "EL": "Elxa pins on four stars in her dress blues",
                "JJ": "Jeremy writes in a notebook at a crime scene",
                "ML": "Mallory signs a contract and caps her pen",
                "MO": "Martin buttons his jacket in a mirror, and the reflection doesn't "
                      "smile",
                "PO": "Peter snaps on surgical gloves",
                "ES": "Esther on her Tuxedo Park terrace, looking across the ridge at "
                      "Summit House",
                "EM": "Emma curtsies at a piano recital",
                "VI": "Victoria cartwheels across a school lawn",
            }[k]) for k in ensemble)
    ], [0.5 * inch, 2.1 * inch, 3.9 * inch]),
    Spacer(1, 6),
    P("7. “Also Starring” Card (Featured Contract Cast)", h2),
    P(", ".join(CAST[k][0] for k in featured) + "."),
    P("8. Title Card", h2),
    P("The camera rises past Summit House into clouds as the choir hits the final chord. "
      "<b>BEYOND THE CREST</b> glows in gold over the ridge."),
    P("Season 2 changes", h2),
    *bullets([
        "Theodore Donohue and his family (Lorraine, Xander, Celestine, Theo III, and "
        "Sienna) join the Core cast, and young August joins the Westbrook kids.",
        "<i>Proposal, pending your approval:</i> Theodore gets a unique sequence of his "
        "own, and the rest of his family joins the ensemble sequence.",
        "Alvin keeps his unique sequence.",
    ]),
]

build(OUT, story, "Beyond the Crest — Cast & Opening Credits",
      "BEYOND THE CREST — Cast & Opening Credits — Writers' Room Confidential")
