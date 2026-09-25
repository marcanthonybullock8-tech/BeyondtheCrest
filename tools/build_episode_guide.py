"""Builds docs/09_Season_1_Episode_Guide.pdf"""
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, KeepTogether

from btc_pdf import (P, h1, h2, body, cell, answer, bullets, table, long_date, build, cover,
                     GOLD, sweeps_on)
from cast import CAST
from season1_episodes import EPISODES, DARK_DAYS, full_cast, season1_calendar

OUT = "docs/09_Season_1_Episode_Guide.pdf"

ep_head = ParagraphStyle("eh", parent=body, fontName="Times-Bold", spaceBefore=8,
                         spaceAfter=2, textColor=GOLD)
castline = ParagraphStyle("cl", parent=cell, fontSize=8.5, leading=10.5,
                          textColor="#555555", spaceAfter=4)

TITLES = ("Det.", "Dr.", "Judge", "SAC", "State", "Sen.", "Gen.", "(Ret.)")


def short(code):
    name = CAST[code][0]
    if "“" in name:
        return name.split("“")[1].split("”")[0]
    if name.startswith("Young "):
        return "Young " + name.split()[1]
    if code in ("TD", "T3", "XD"):
        return {"TD": "Theodore", "T3": "Theo III", "XD": "Xander"}[code]
    return next(w for w in name.split() if w not in TITLES)


cal = season1_calendar()
assert len(cal) == len(EPISODES)

story = cover("Season 1 Episode Guide — Document 09", [
    "<b>Episodes #0001–#0170</b>",
    "Monday, January 5, 2026 – Friday, September 4, 2026",
])
story.append(PageBreak())
story += [
    P("Guide Notes", h1),
    *bullets([
        "<b>Story time runs with air time.</b> Unless noted, an episode takes place on "
        "its air date. Weekend events (the Oscars, the Tonys, Victor's 80th) air on the "
        "next weekday with the story date noted.",
        "<b>SWEEPS</b> marks every episode that airs during a Nielsen sweeps period: "
        "February (Eps #0019–#0038), May (#0076–#0095), and July "
        "(#0120–#0138). See Document 01, Section 9.",
        "★ marks an event episode, one of the 17 standalone-leaning episodes that make "
        "up 10% of the season.",
        "<b>Cast</b> lists every character in the episode: the headline story plus that "
        "day's runner scenes. Document 07's episode counts come from these lists.",
        "Days with no new episode: " + "; ".join(
            f"{d:%a %b} {d.day} ({why})" for d, why in sorted(DARK_DAYS.items())) + ".",
    ]),
]

month, sweep = None, None
for n, ((event, note, synopsis, codes), d) in enumerate(zip(EPISODES, cal), start=1):
    if d.month != month:
        month = d.month
        story.append(P(f"{d:%B %Y}", h1))
    now = sweeps_on(d)
    if now != sweep:
        if sweep:
            story.append(P(f"■ END OF {sweep.upper()}", answer))
        if now:
            story.append(P(f"■ {now.upper()} BEGIN", answer))
        sweep = now
    star = " ★" if event else ""
    head = f"#{n:04d}{star} — {long_date(d)}"
    if now:
        head += " • <font color='#3A1F3D'>SWEEPS</font>"
    if note:
        head += f" <font size='9'>(Story: {note})</font>"
    cast = ", ".join(short(c) for c in full_cast(n))
    story.append(KeepTogether([P(head, ep_head), P(synopsis),
                               P(f"<b>Cast:</b> {cast}", castline)]))

build(OUT, story, "Beyond the Crest — Season 1 Episode Guide",
      "BEYOND THE CREST — Season 1 Episode Guide — Writers' Room Confidential")
