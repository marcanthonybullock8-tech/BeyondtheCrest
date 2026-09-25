"""Shared styles and helpers for Beyond the Crest PDF documents."""
import datetime as dt

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle)

GOLD = colors.HexColor("#B8892B")
INK = colors.HexColor("#1B1B1F")
PLUM = colors.HexColor("#3A1F3D")
LIGHT = colors.HexColor("#F4EEE3")

PREMIERE = dt.date(2026, 1, 5)

title = ParagraphStyle("t", fontName="Times-Bold", fontSize=34, leading=40,
                       alignment=TA_CENTER, textColor=PLUM)
sub = ParagraphStyle("s", fontName="Times-Italic", fontSize=14, leading=18,
                     alignment=TA_CENTER, textColor=GOLD)
center = ParagraphStyle("ce", fontName="Times-Roman", fontSize=11,
                        leading=14.5, alignment=TA_CENTER, textColor=INK)
h1 = ParagraphStyle("h1", fontName="Times-Bold", fontSize=18, leading=22,
                    textColor=PLUM, spaceBefore=14, spaceAfter=6)
h2 = ParagraphStyle("h2", fontName="Times-Bold", fontSize=13, leading=16,
                    textColor=GOLD, spaceBefore=10, spaceAfter=4)
body = ParagraphStyle("b", fontName="Times-Roman", fontSize=11, leading=14.5,
                      textColor=INK, spaceAfter=6)
italic = ParagraphStyle("i", parent=body, fontName="Times-Italic")
bul = ParagraphStyle("bul", parent=body, leftIndent=16, bulletIndent=4,
                     spaceAfter=3)
answer = ParagraphStyle("a", parent=body, backColor=LIGHT, borderPadding=6,
                        borderColor=GOLD, borderWidth=0.8, spaceBefore=4,
                        spaceAfter=10, fontName="Times-Bold")
cell = ParagraphStyle("c", fontName="Times-Roman", fontSize=9.5, leading=12)
cellb = ParagraphStyle("cb", parent=cell, fontName="Times-Bold",
                       textColor=colors.white)

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
    """lines: ("d", direction) or (CHARACTER, (parenthetical, dialogue))."""
    out = [P(slug, sp_slug)]
    for kind, text in lines:
        if kind == "d":
            out.append(P(text, sp_dir))
        else:
            paren, dia = text
            out.append(P(kind, sp_char))
            if paren:
                out.append(P(f"({paren})", sp_paren))
            out.append(P(dia, sp_dial))
    return out


def age_on(born, on=PREMIERE):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


def long_date(d):
    return f"{d:%A, %B} {d.day}, {d.year}"


def build(out, story, doc_title, running_head):
    def footer(c, doc):
        c.saveState()
        c.setFont("Times-Italic", 8.5)
        c.setFillColor(colors.grey)
        c.drawString(inch, 0.55 * inch, running_head)
        c.drawRightString(7.5 * inch, 0.55 * inch, f"Page {doc.page}")
        c.restoreState()

    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=inch,
                            rightMargin=inch, topMargin=0.9 * inch,
                            bottomMargin=0.9 * inch, title=doc_title,
                            author="Beyond the Crest Writers' Room")
    doc.build(story, onFirstPage=lambda c, d: None, onLaterPages=footer)
    print("wrote", out)


def cover(doc_line, extra_lines):
    return [Spacer(1, 2.1 * inch), P("BEYOND THE CREST", title), Spacer(1, 8),
            P(doc_line, sub), Spacer(1, 30),
            P("A Daytime Drama", ParagraphStyle("x", parent=sub, textColor=INK)),
            Spacer(1, 90)] + [P(x, center) for x in extra_lines]
