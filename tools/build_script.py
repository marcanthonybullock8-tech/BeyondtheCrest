"""Renders an episode script (tools/scripts/epNNNN.txt) to a daytime-format PDF.

Usage: python3 tools/build_script.py 1

Script markup (blocks are separated by blank lines):
  == TEASER / == ACT ONE ...   act header (each act starts a new page)
  INT. ... / EXT. ...          scene heading, numbered automatically
  INSERT ... / BACK TO SCENE   non-numbered heading
  ... TO: / FADE OUT. / MAIN TITLE   transition
  NAME                         character cue, followed by (parentheticals) and
  dialogue                     dialogue lines in the same block
  (beat)                       a standalone parenthetical continues the last speaker;
                               the block after it is dialogue
  anything else                action
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                KeepTogether, Table, TableStyle, CondPageBreak)

from btc_pdf import age_on, long_date
from cast import CAST
from season1_episodes import EPISODES, full_cast, season1_calendar

EXTRAS = {
    1: "rower, patrol officers, dive team, photographers, DBC camera crew, waiters, "
       "valets, 500 gala guests, string quartet, jazz band",
    2: "chef, housekeeper, florists, Westbrook students, Trey's friends, APD officers, "
       "reporters and camera crews, BNN anchor (on TV), board member and assistants "
       "(V.O.)",
}
TITLES = {1: "The Crown on the Hill", 2: "A Dead Man Calling"}

F, FB = "Courier", "Courier-Bold"
base = dict(fontName=F, fontSize=12, leading=14)
action = ParagraphStyle("action", **base, spaceAfter=12)
slug = ParagraphStyle("slug", fontName=FB, fontSize=12, leading=14, spaceBefore=6,
                      spaceAfter=12)
act = ParagraphStyle("act", fontName=FB, fontSize=12, leading=14, alignment=TA_CENTER,
                     spaceAfter=24)
trans = ParagraphStyle("trans", **base, alignment=TA_RIGHT, spaceAfter=12)
cue = ParagraphStyle("cue", **base, leftIndent=2.2 * inch)
paren = ParagraphStyle("paren", **base, leftIndent=1.6 * inch, rightIndent=1.5 * inch)
dia = ParagraphStyle("dia", **base, leftIndent=1.0 * inch, rightIndent=1.0 * inch)
title_st = ParagraphStyle("t", fontName=FB, fontSize=20, leading=26, alignment=TA_CENTER)
center = ParagraphStyle("c", **base, alignment=TA_CENTER)
small = ParagraphStyle("s", fontName=F, fontSize=10, leading=12)
smallb = ParagraphStyle("sb", fontName=FB, fontSize=10, leading=12)

CUE_RE = re.compile(r"^[A-Z][A-Z0-9 .'\-]+( \((CONT'D|O\.S\.|V\.O\.)\))*$")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def parse(text):
    """Returns (flowables, scene headings)."""
    out, scenes, n = [], [], 0
    last_was_paren = False
    for block in [b.strip("\n") for b in re.split(r"\n\s*\n", text) if b.strip()]:
        lines = block.split("\n")
        first = lines[0].strip()
        if first.startswith("== "):
            label = first[3:]
            if not label.startswith("END"):
                out.append(PageBreak())
            out.append(Paragraph(label, act))
            last_was_paren = False
        elif first.startswith(("INT.", "EXT.")):
            n += 1
            scenes.append(first)
            out.append(CondPageBreak(1.2 * inch))
            out.append(Paragraph(f"{n}. {esc(first)}", slug))
            last_was_paren = False
        elif first.startswith(("INSERT", "BACK TO SCENE")):
            out.append(Paragraph(esc(first), slug))
            last_was_paren = False
        elif len(lines) == 1 and (first.endswith("TO:") or first in ("FADE OUT.",
                                                                        "MAIN TITLE")):
            out.append(Paragraph(esc(first), trans))
            last_was_paren = False
        elif len(lines) > 1 and CUE_RE.match(first):
            parts = [Paragraph(esc(first), cue)]
            for ln in lines[1:]:
                ln = ln.strip()
                parts.append(Paragraph(esc(ln), paren if ln.startswith("(") else dia))
            parts[-1].style = ParagraphStyle("last", parent=parts[-1].style,
                                             spaceAfter=12)
            out.append(KeepTogether(parts))
            last_was_paren = False
        elif len(lines) == 1 and first.startswith("(") and first.endswith(")"):
            out.append(Paragraph(esc(first), paren))
            last_was_paren = True
        elif last_was_paren:
            out.append(Paragraph(esc(" ".join(l.strip() for l in lines)),
                                 ParagraphStyle("d2", parent=dia, spaceAfter=12)))
            last_was_paren = False
        else:
            out.append(Paragraph(esc(" ".join(l.strip() for l in lines)), action))
            last_was_paren = False
    return out, scenes


def main(ep):
    src = open(f"tools/scripts/ep{ep:04d}.txt").read()
    body, scenes = parse(src)
    air = season1_calendar()[ep - 1]
    out = f"docs/scripts/Episode_{ep:04d}_Script.pdf"

    story = [Spacer(1, 2.2 * inch), Paragraph("BEYOND THE CREST", title_st),
             Spacer(1, 18),
             Paragraph(f"Episode #{ep:04d}", center),
             Paragraph(f"“{TITLES.get(ep, '')}” (working title)", center),
             Spacer(1, 18),
             Paragraph(f"Production Code BTC-S01-{ep:04d}", center),
             Paragraph(f"Air Date: {long_date(air).upper()}", center),
             Paragraph("Season 1", center),
             Spacer(1, 1.6 * inch),
             Paragraph("PRODUCTION DRAFT", center),
             Paragraph("Beyond the Crest Writers' Room", center),
             PageBreak()]

    # Cast list, ages as of air date
    rows = [[Paragraph("CHARACTER", smallb), Paragraph("AGE", smallb),
             Paragraph("ROLE", smallb)]]
    for code in full_cast(ep):
        name, born, died, cat, group, role = CAST[code]
        age = "—" if died and died < air else str(age_on(born, air))
        if code == "TB":
            name, role = "The Man in the River", "Unidentified body (T-Bone Gaines)"
        rows.append([Paragraph(esc(name).upper(), small), Paragraph(age, small),
                     Paragraph(esc(role), small)])
    t = Table(rows, colWidths=[2.3 * inch, 0.5 * inch, 3.2 * inch], repeatRows=1)
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.black),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    story += [Paragraph("CAST", act),
              Paragraph(f"Ages as of {long_date(air)}", center), Spacer(1, 12), t,
              Spacer(1, 12),
              Paragraph("Also: " + EXTRAS.get(ep, "background performers") + ".", small),
              PageBreak()]

    # Sets
    sets = []
    for s in scenes:
        loc = re.sub(r"\s*\(.*\)$", "", s)
        loc = re.sub(r" - (DAWN|DAY|NIGHT|MORNING|AFTERNOON|EARLY EVENING|"
                     r"MOMENTS LATER)$", "", loc)
        if loc not in sets:
            sets.append(loc)
    story += [Paragraph("SETS", act)] + \
             [Paragraph(esc(s), ParagraphStyle("st", **base, spaceAfter=4)) for s in sets] + \
             [Spacer(1, 12), Paragraph(f"{len(scenes)} scenes", center)]
    story += body

    def page(c, doc):
        if doc.page > 1:
            c.saveState()
            c.setFont(F, 10)
            c.drawString(1.5 * inch, 10.5 * inch,
                         f"BEYOND THE CREST #{ep:04d} — {air:%m/%d/%y}")
            c.drawRightString(7.5 * inch, 10.5 * inch, f"{doc.page - 1}.")
            c.restoreState()

    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=1.5 * inch,
                            rightMargin=1.0 * inch, topMargin=1.0 * inch,
                            bottomMargin=1.0 * inch,
                            title=f"Beyond the Crest — Episode #{ep:04d}",
                            author="Beyond the Crest Writers' Room")
    doc.build(story, onFirstPage=page, onLaterPages=page)
    print("wrote", out, f"({len(scenes)} scenes)")


if __name__ == "__main__":
    main(int(sys.argv[1]))
