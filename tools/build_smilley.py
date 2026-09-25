"""Builds docs/06_The_Smilley_Family.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer, KeepTogether

from btc_pdf import (P, h1, h2, body, italic, answer, bullets, table, scene,
                     age_on, long_date, build, cover)
from cast import CAST

OUT = "docs/06_The_Smilley_Family.pdf"
D = dt.date

story = cover("The Smilley Family &amp; Smilley Corporation — Document 06", [
    "<b>The secondary family of Beyond the Crest</b>",
    "<b>Smilley Corporation</b>: founded " + long_date(D(1974, 9, 9)) + ", New York City",
    "<b>Home:</b> Tuxedo Park, Buckhead, Atlanta, just across the ridge from Belmont Crest",
])
story.append(PageBreak())

story += [
    P("The Feud in One Page", h1),
    P("The Smilleys are the Donohues' fiercest rivals and competitors, and the two families "
      "are always at odds. The Donohues are old money that built Black Atlanta. The Smilleys "
      "are the family Atlanta threw out, who came back rich enough to buy the block. And "
      "the thing the Smilleys hate most: <b>their empire still runs on Donohue "
      "oxygen.</b>", answer),
    *bullets([
        "<b>1958:</b> Alexander Donohue fires Otis Smilley, the Beacon's press foreman, for "
        "stealing printing plates. Otis swears he was framed. His son Gus is 15.",
        "<b>1962:</b> Otis applies to live in Belmont Crest. Simone Donohue casts the "
        "deciding vote: no.",
        "<b>1963:</b> Gus leaves for Harlem, vowing to come back richer than the "
        "Donohues.",
        "<b>1966:</b> In New York, Gus falls for a Broadway ingenue named Joan Mercer and "
        "proposes. She says “not yet,” then goes home and marries Victor Donohue "
        "in 1969.",
        "<b>1990:</b> The Crown License makes Smilley dependent on Donohue characters and "
        "brands.",
        "<b>1996:</b> Gus moves the company to Atlanta and buys in Tuxedo Park, where he can "
        "see Summit House from his terrace.",
        "<b>1996:</b> Gus writes the <b>Allegiance Clause</b> into the family charter.",
        "<b>2026:</b> Esther, his chosen heir, has been hiding two Donohue great-"
        "granddaughters for fourteen years.",
    ]),
    P("The Allegiance Clause", h2),
    P("<i>“No Designated Heir of Smilley International shall be joined by marriage, "
      "or bound by blood through their children, to the House of Donohue. Any such heir "
      "is disqualified.”</i> Section 4(c), Smilley Family Charter, adopted "
      + long_date(D(1996, 6, 3)) + ".", italic),
    P("That clause is why Esther told the world she used IVF and a sperm donor. If anyone "
      "proves that Emma and Victoria are Marc-Anthony Bullock's daughters, Esther loses "
      "everything, and Nathaniel and Camille get it."),
    PageBreak(),
    P("The Smilley Family", h1),
]

TREE = [
    ("Otis Smilley", "1919–1988", "Gus's father, fired from the Beacon in 1958 (seen in flashback)"),
    ("Augustus “Gus” Smilley ∞ Loretta Hayes", "m. " + long_date(D(1963, 12, 21)),
     "Founders"),
    ("└ Leonard Smilley ∞ Celeste Beaumont", "m. " + long_date(D(1984, 6, 30)),
     "Chairman &amp; CEO / Foundation Chair"),
    ("   └ Nathaniel ∞ Monique Carter", "m. 2010", "Their son: Trey (b. 2012)"),
    ("   └ Camille ∞ Dorian Ward", "m. 2016", "No children"),
    ("   └ Esther", "Never married", "Twins Emma &amp; Victoria (b. 2012; "
     "father: Marc-Anthony Bullock, SECRET)"),
    ("└ Delphine Smilley", "Divorced three times", "Her son: Desmond (b. 1994)"),
]
story += [table([["Line", "Marriage", "Notes"]] + [list(r) for r in TREE],
                [3.1 * inch, 1.6 * inch, 1.8 * inch]), Spacer(1, 8)]

PROFILES = [
    ("GS", "Chairman Emeritus of Smilley Corporation and Chairman of Smilley International",
     "The Founder. Gus is 82 and still sharp: charming, vindictive, and funny. He has spent "
     "sixty years trying to prove that Alexander Donohue was wrong about his father. He "
     "built a $1.6 trillion company out of a Harlem pharmacy and a grudge. He still keeps "
     "Joan Mercer's 1966 reply letter in his desk.",
     ["Born in Vine City, Atlanta. Watched his father fired in 1958 and the family "
      "rejected by Belmont Crest in 1962.",
      "Moved to Harlem at 20. Married Loretta Hayes in December 1963. Separated from her "
      "in 1966 while he chased Joan Mercer, then came home to Loretta for good in 1967.",
      "Founded Smilley Corporation in 1974 and moved it home to Atlanta in 1996. Wrote the "
      "Allegiance Clause the same year.",
      "Named Esther heir over his son's older children because “she's the only one "
      "who's as mean as me.”"],
     ("GUS", ("", "The Donohues own the sky over Atlanta. Fine. I own everything people "
                  "buy while they're looking up at it."))),
    ("LO", "Co-founder; creator of Loretta's Crown Pomade",
     "The Matriarch. Loretta is the quiet genius: her hair pomade, mixed in a Harlem "
     "kitchen in 1971, was Smilley Corporation's first product. She forgave Gus once. "
     "She's never forgiven Joan.",
     ["Harlem beautician turned billionaire chemist.",
      "Knows every secret in the family, including Esther's. She has figured out the "
      "twins, and she is saying nothing, for now."],
     ("LORETTA", ("", "I built this company with a spoon and a stove, baby. Don't you "
                      "dare tell me what I can't cook."))),
    ("LE", "Chairman &amp; CEO, Smilley Corporation (CEO since 2003; Chairman since 2020)",
     "The Son. Leonard is a brilliant operator in his father's shadow, obsessed with "
     "freeing Smilley from Donohue dependence. He secretly funds Pryor's primary "
     "challenge to Jasmine.",
     ["Howard University and Harvard Business School.",
      "Grew Smilley from $40 billion to $1.6 trillion, and resents that the Crown License "
      "made half of it possible."],
     ("LEONARD", ("", "Every dollar we make, Donohue takes a cut. I want a company that "
                      "doesn't have to say thank you."))),
    ("CE", "Chair, Smilley Family Foundation; Atlanta society general",
     "The Social General. Celeste is a Beaumont of New Orleans, elegant and ferocious, and "
     "she runs Atlanta society's calendar. She adores her grandchildren and her daughter "
     "Esther, in that order.",
     ["Beaumont family, New Orleans. Spelman class of 1987.",
      "Her lifelong rival is Joan Donohue. Their charity galas are held on the same "
      "night every year."],
     ("CELESTE", ("", "Joan Donohue has a Foundation. I have a guest list. Guess which "
                      "one people actually want to be on."))),
    ("DE", "President, Smilley Home",
     "The Truth-Teller. Delphine is Gus's daughter, three times divorced and never "
     "boring, and the one Smilley who says what everyone thinks. She's the family's "
     "wild card and Desmond's fiercest defender.",
     ["Runs the Smilley Home division: furniture, bedding, and home fragrance.",
      "Secretly friends with Alvin Donohue since a 1999 night in Monaco nobody talks "
      "about."],
     ("DELPHINE", ("", "This family has more skeletons than closets, and I'm the only "
                       "one who ever opens a door."))),
    ("NA", "EVP; President, Smilley Consumer &amp; Digital (includes RootsKit)",
     "The Eldest Son Who Was Passed Over. Nathaniel is 40, polished, cold, and patient. He "
     "was raised to be heir and lost the title to his little sister. His RootsKit DNA "
     "division becomes the weapon that exposes her.",
     ["Morehouse and Stanford MBA. Launched RootsKit in 2017.",
      "Forms the “Spare Alliance” with Martin Olson (Ep #0058).",
      "Secretly finances Harmony's film to get close to Esther."],
     ("NATHANIEL", ("", "My sister didn't win. Grandfather just hadn't met the real me "
                        "yet."))),
    ("MQ", "Nathaniel's wife; former Donohue Records singer",
     "Monique was a Donohue Records R&amp;B star until Alvin Donohue dropped her from the "
     "label in 2009. She married a Smilley and never forgot it.",
     ["Mother of Trey.", "Wants revenge on Alvin the day he comes home (Season 1, second "
      "half)."],
     ("MONIQUE", ("", "Alvin Donohue ended my career over a bar tab. I married up just "
                      "to watch him fall down."))),
    ("TR", "8th grader, Westbrook Academy",
     "Trey is the Smilley heir's heir's son: charming, cocky, and quick. He is Lyric "
     "Baker's first crush. Romeo, meet Juliet.",
     ["Classmate of the twins and Lyric.", "Kisses Lyric on the first day of 9th grade "
      "(Ep #0149), and Victoria punches him."],
     ("TREY", ("", "My grandpa says never trust a Donohue. Lyric's not a Donohue. "
                   "Technically."))),
    ("CA", "Chief Financial Officer, Smilley Corporation",
     "The Middle Child. Camille is a numbers assassin. She's loyal to Nathaniel, jealous "
     "of Esther, and willing to frame her own cousin to win.",
     ["Wharton. Became CFO at 34.",
      "Frames Desmond for stealing HEIRLOOM's formulas (Ep #0069) and launches the "
      "copycat line (Ep #0106)."],
     ("CAMILLE", ("", "Numbers don't lie. People do. That's why I prefer numbers."))),
    ("DO", "Chief Strategy Officer, Smilley Corporation",
     "Dorian is Camille's husband. Natasha Donohue fired him from The Donohue Company in "
     "2019, and he's Martin's back channel inside Smilley.",
     ["Knows Donohue Consumer Licensing's playbook by heart."],
     ("DORIAN", ("", "I didn't leave Donohue. Donohue left me. I just took the playbook "
                     "with me."))),
    ("DS", "Creative Director, Smilley Beauty (resigns in Ep #0114)",
     "Desmond is Delphine's son, a gentle and brilliant artist who falls for Mallory Olson. "
     "The Montague who loves a Capulet.",
     ["Framed by Camille, then clears his name.",
      "Tells Mallory he'll wait for her, as long as it takes."],
     ("DESMOND", ("", "I don't care whose granddaughter you are. I care who you are."))),
]
for code, title, who, back, voice in PROFILES:
    name, born, died, cat, group, role = CAST[code]
    head = [P(name.upper(), h2),
            P(f"<b>Born:</b> {long_date(born)} • <b>Age:</b> {age_on(born)}"),
            P(f"<b>Title:</b> {title}"), P(who)]
    story.append(KeepTogether(head))
    story += bullets(back)
    story += scene("IN THEIR OWN WORDS", [voice])

story += [
    P("Also Smilleys", h2),
    P("<b>Esther, Emma, and Victoria Smilley</b> are fully profiled in Document 02. "
      "Esther is President &amp; COO of Smilley Corporation and designated heir of Smilley "
      "International. She oversees Smilley Retail, Smilley Beauty, and every Donohue "
      "license negotiation."),
    PageBreak(),
    P("History of Smilley Corporation", h1),
    table([
        ["Field", "Detail"],
        ["Legal name", "Smilley Corporation (NYSE: SMLY)"],
        ["Controlling shareholder", "Smilley International Holdings, Ltd. (private family "
                                    "holding company)"],
        ["Industry", "Multinational consumer products, retail &amp; lifestyle "
                     "conglomerate"],
        ["Founded", long_date(D(1974, 9, 9)) + ", Harlem, New York City"],
        ["Headquarters", "Smilley Plaza, 3400 Peachtree Road NE, Buckhead, Atlanta (since "
                         "1996)"],
        ["Market capitalization", "<b>$1.6 trillion</b>"],
        ["Revenue (FY2025)", "$640 billion"],
        ["Employees", "880,000"],
        ["Dependence on Donohue", "<b>~41% of revenue</b> is tied to the Crown License: "
                                  "Donohue characters, films, and brands on Smilley "
                                  "products, plus ad inventory on Donohue networks"],
    ], [1.8 * inch, 4.7 * inch]),
]

eras = [
    ("1971–1984: Harlem", [
        "1971: Loretta mixes the first batch of <b>Loretta's Crown Pomade</b> on her "
        "stove on West 137th Street. Gus sells it out of a pharmacy on Lenox Avenue.",
        long_date(D(1974, 9, 9)) + ": Smilley Corporation is incorporated with $3,800 "
        "and one product.",
        "1978–1984: Expands into cosmetics, skin care, and household goods. "
        "The Black press starts calling Gus “the Black Procter.”",
    ]),
    ("1985–1995: The Big Time", [
        "1985: IPO on the NYSE, with dual-class shares that keep control in the family.",
        "1987: Opens the first <b>Smilley's</b> department store on 125th Street.",
        "1990: Signs the first <b>Crown License</b> with The Donohue Company, putting "
        "Donohue characters on Smilley toys, clothes, and school supplies. Revenue "
        "triples in five years. Gus calls it “the best deal I ever hated.”",
    ]),
    ("1996–2010: Coming Home", [
        "1996: Moves headquarters to Atlanta and builds Smilley Plaza in Buckhead. The "
        "family buys in Tuxedo Park. Gus writes the Allegiance Clause.",
        "1998: Donohue takes a 4% stake in Smilley, now Smilley's largest outside "
        "shareholder. Gus signs the deal and then breaks his hand punching a wall.",
        "2003: Leonard becomes CEO.",
        "2005: Launches Smilley Beauty. 2008: Launches Smilley Home.",
    ]),
    ("2011–2026: The Empire", [
        "2012: Esther, 19, announces her “IVF twins.” The family closes ranks.",
        "2017: Nathaniel launches <b>RootsKit</b>, the world's No. 1 consumer DNA test.",
        "2020: Leonard becomes Chairman and Gus becomes Chairman Emeritus. Gus names "
        "Esther designated heir on " + long_date(D(2020, 1, 6)) + ".",
        "2023: Esther becomes President &amp; COO.",
        "2025: Market cap reaches $1.6 trillion. Leonard begins “Project Independence” "
        "to end reliance on the Crown License.",
        long_date(D(2026, 8, 31)) + ", 11:59 PM: The Crown License expires. It's the "
        "season-long battle, and it ends in Ep #0166.",
    ]),
]
for era, items in eras:
    story.append(P(era, h2))
    story += bullets(items)

story += [
    P("Divisions", h2),
    table([
        ["Division", "Leader", "What it is"],
        ["Smilley Consumer &amp; Digital", "Nathaniel", "Household goods, personal care, "
                                                        "RootsKit DNA"],
        ["Smilley Beauty", "Esther (oversight); Desmond (creative)", "Cosmetics, hair care, "
                                                                  "fragrance"],
        ["Smilley Retail", "Esther", "Smilley's department stores (1,900 worldwide) and "
                                     "SMLY.com"],
        ["Smilley Home", "Delphine", "Furniture, bedding, home fragrance"],
        ["Smilley Licensed Brands", "Esther", "Every Donohue-licensed product: the Crown "
                                              "License business"],
        ["Smilley Wellness", "Camille (interim)", "Vitamins, fitness, wellness"],
    ], [1.9 * inch, 2.0 * inch, 2.6 * inch]),
    PageBreak(),
]

# ---------------- SHARES ----------------
SC_TOTAL, B_VOTES, PRICE = 8.0, 5, 200
sc_rows = [
    ("Smilley International Holdings, Ltd.", 2.0, 0.56),
    ("Donohue Enterprises (strategic stake, 1998)", 0.0, 0.32),
    ("Smilley Family Foundation", 0.0, 0.08),
    ("Directors &amp; officers (excl. SIH)", 0.0, 0.04),
    ("Employee stock plans", 0.0, 0.20),
    ("Index &amp; passive fund managers", 0.0, 1.60),
    ("Active institutional investors", 0.0, 1.60),
    ("Public pension &amp; sovereign funds", 0.0, 0.80),
    ("Retail &amp; other public holders", 0.0, 0.80),
]
tb = sum(r[1] for r in sc_rows)
ta = sum(r[2] for r in sc_rows)
assert abs(tb + ta - SC_TOTAL) < 1e-9
tv = tb * B_VOTES + ta
rows = [["Holder", "Class B (bn)", "Class A (bn)", "Economic %", "Voting %", "Value"]]
for h, b, a in sc_rows:
    e = (a + b) / SC_TOTAL
    v = (b * B_VOTES + a) / tv
    rows.append([h, f"{b:.2f}", f"{a:.2f}", f"{e:.1%}", f"{v:.1%}",
                 f"${e * 1600:,.0f}B"])
rows.append(["<b>TOTAL</b>", f"<b>{tb:.2f}</b>", f"<b>{ta:.2f}</b>", "<b>100%</b>",
             "<b>100%</b>", "<b>$1,600B</b>"])

sih = [
    ("Augustus “Gus” Smilley", 30, 40),
    ("Loretta Smilley", 10, 10),
    ("Leonard Smilley", 22, 25),
    ("Esther Smilley (Designated Heir)", 10, 15),
    ("Nathaniel Smilley", 8, 5),
    ("Camille Smilley-Ward", 8, 5),
    ("Delphine Smilley", 8, 0),
    ("Desmond Smilley", 2, 0),
    ("Smilley Family Foundation", 2, 0),
]
assert sum(r[1] for r in sih) == 100 and sum(r[2] for r in sih) == 100
sih_value = 0.32 * 1600
srows = [["Owner", "Economic %", "Value", "Family Council vote"]]
for o, e, v in sih:
    srows.append([o, f"{e}%", f"${e / 100 * sih_value:,.1f}B", f"{v}%"])
srows.append(["<b>TOTAL</b>", "<b>100%</b>", f"<b>${sih_value:,.0f}B</b>", "<b>100%</b>"])

story += [
    P("Share Distribution: Smilley Corporation (NYSE: SMLY)", h1),
    *bullets([
        "<b>Class A common</b>: 1 vote per share, publicly traded.",
        f"<b>Class B common</b>: {B_VOTES} votes per share, not traded, 100% owned by Smilley "
        "International Holdings.",
        f"Shares outstanding: {SC_TOTAL:.1f} billion at ${PRICE} = $1.6 trillion.",
    ]),
    table(rows, [2.3 * inch, 0.8 * inch, 0.8 * inch, 0.8 * inch, 0.75 * inch, 0.85 * inch]),
    Spacer(1, 6),
    P("RESULT: The Smilley family owns 32% of the company ($512 billion) and controls "
      f"{(2.0 * B_VOTES + 0.56) / tv:.1%} of the vote. Donohue Enterprises holds 4.0% "
      "of the economics and 2.0% of the votes, which makes it the largest shareholder "
      "outside the family.", answer),
    P("Share Distribution: Smilley International Holdings, Ltd. (private)", h1),
    P("Smilley International Holdings (SIH) is the family holding company, governed by "
      "the <b>Smilley Family Council</b> under the 1996 Family Charter, including the "
      "Allegiance Clause."),
    table(srows, [2.8 * inch, 1.0 * inch, 1.2 * inch, 1.5 * inch]),
    Spacer(1, 6),
    P("Rules that drive the drama", h2),
    *bullets([
        "<b>The Designated Heir</b> inherits Gus's 30% and his 40% Council vote when he "
        "dies. That would make Esther the most powerful Smilley alive.",
        "<b>Section 4(c), the Allegiance Clause:</b> disqualifies any heir tied to the "
        "House of Donohue by marriage or through their children. The Council can invoke it "
        "by majority vote. Gus plus any one other member is enough.",
        "<b>Succession if disqualified:</b> the title passes to the eldest eligible "
        "grandchild. That's Nathaniel.",
        "<b>Season 1:</b> Nathaniel presents the RootsKit evidence at the Family Council "
        "(Ep #0163). Gus invokes Section 4(c) (Ep #0164). Esther is suspended unless a DNA "
        "test clears her by Labor Day (Ep #0165).",
    ]),
]

build(OUT, story, "Beyond the Crest — The Smilley Family",
      "BEYOND THE CREST — The Smilley Family — Writers' Room Confidential")
