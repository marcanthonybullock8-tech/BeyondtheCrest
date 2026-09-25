"""Builds docs/03_The_Donohue_Company.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from btc_pdf import (P, h1, h2, body, italic, answer, bullets, table, long_date,
                     build, cover)

OUT = "docs/03_The_Donohue_Company.pdf"
D = dt.date

story = cover("The Donohue Company — Document 03", [
    "<b>Founded:</b> " + long_date(D(1939, 4, 3)) + ", Atlanta, Georgia",
    "<b>Founder:</b> Alexander Donohue (b. " + long_date(D(1916, 3, 3)) + ")",
    "<b>Valuation:</b> $10 trillion",
])
story.append(PageBreak())

story += [
    P("Corporate Profile", h1),
    table([
        ["Field", "Detail"],
        ["Legal name", "Donohue Enterprises, Inc., doing business as <b>The Donohue Company</b>"],
        ["Ticker", "NYSE: DNHU (Class A common)"],
        ["Controlling shareholder", "Donohue Global Holdings, Inc. (private family holding company)"],
        ["Industry", "Multinational mass media &amp; entertainment conglomerate"],
        ["Headquarters", "Donohue Tower, 1939 Peachtree Street NE, Midtown Atlanta, GA 30309"],
        ["Founder", "Alexander Donohue (1916–2006), with Simone Donohue (1920–2014)"],
        ["Chairman", "Victor Donohue (2006–present)"],
        ["CEO", "Natasha Bullock (2006–present)"],
        ["President &amp; COO", "Marc-Anthony Bullock (named Mon, Jan 5, 2026)"],
        ["Market capitalization", "<b>$10.0 trillion</b> (world's most valuable company)"],
        ["Annual revenue (FY2025)", "$1.62 trillion"],
        ["Net income (FY2025)", "$318 billion"],
        ["Employees", "1.14 million in 96 countries"],
        ["Audience reach", "Some Donohue product touches an estimated 6.1 billion people a month"],
        ["Philanthropy", "The Donohue Foundation (endowment $300 billion+), chaired by Joan "
                         "Donohue. It spares no expense."],
    ], [1.8 * inch, 4.7 * inch]),

    P("The Founder", h1),
    P("<b>Alexander Donohue</b> was born on " + long_date(D(1916, 3, 3)) + ", above a "
      "barbershop on Auburn Avenue, “Sweet Auburn,” then the richest Black "
      "street in America. His father was a Pullman porter who brought home every newspaper "
      "left behind on the trains. His mother took in laundry and read those papers aloud "
      "at night. By 12, Alexander was selling newspapers on street corners, "
      "and he noticed that none of the papers he sold told his neighbors' stories. By 20 he "
      "was setting type at a Black-owned print shop. At 23 he started his own paper."),
    P("He met <b>Simone Batiste</b>, a New Orleans jazz singer four years his junior, when "
      "she played the Top Hat Club on Auburn Avenue in 1938. She had been singing in "
      "clubs since she was 14, and she bankrolled the first printing press with her savings. They married on "
      + long_date(D(1941, 6, 7)) + ". Alexander called her “my first investor and my "
      "only partner,” and meant it."),

    P("History of The Donohue Company", h1),
]

eras = [
    ("1939–1949: The Beacon", [
        long_date(D(1939, 4, 3)) + ": <i>The Atlanta Beacon</i> publishes its first "
        "edition, four pages printed on Simone's press in a back room on Auburn Avenue. "
        "Circulation: 1,100.",
        "1942–1945: The Beacon sends Black war correspondents to Europe and the "
        "Pacific. Circulation passes 200,000, and “The Beacon” becomes the most "
        "trusted Black newspaper in the South.",
        "1947: Launches <i>Crown</i>, a Black lifestyle and society magazine.",
    ]),
    ("1950–1959: Radio, Records &amp; Pictures", [
        "1951: Donohue buys WDON-AM, putting Black voices on Atlanta radio: gospel on "
        "Sunday, jazz on Friday, the news every hour.",
        "1953: <b>Donohue Pictures</b> is founded, first to make films for Black audiences "
        "and then to break them into white theaters.",
        "1958: Alexander and Simone found Belmont Crest (see Document 04).",
        "1959: Donohue Pictures' <i>Sweet Auburn Serenade</i> becomes the first "
        "Black-produced film to top the national box office.",
    ]),
    ("1960–1975: The Movement Years", [
        "1961: <b>Donohue Records</b> launches in Atlanta: soul, gospel, and the sound of "
        "the South. It becomes Motown's great Southern rival.",
        "1960s: The Beacon covers the civil rights movement from the inside. Alexander "
        "quietly bankrolls bail funds and bus fare, and the FBI opens a file on him in "
        "1963.",
        "1966: Victor Donohue, 20, becomes a matinee idol in <i>Midnight on "
        "Peachtree</i>.",
        "1969: Victor marries his co-star Joan Mercer, and the company's first family "
        "becomes America's first family of entertainment.",
        "1972: Launches WDON-TV, a UHF station, the seed of <b>Donohue Broadcasting "
        "Group</b>. Victor originates the lead in the Broadway musical <i>Sweet "
        "Chariot</i>.",
    ]),
    ("1976–1989: Victor's Empire", [
        long_date(D(1976, 1, 5)) + ": Alexander names his younger son Victor CEO over his "
        "elder son Theodore and becomes Chairman. Theodore walks out of the boardroom and "
        "doesn't come back.",
        long_date(D(1978, 10, 16)) + ": <b>IPO</b> on the New York Stock Exchange. "
        "Donohue Enterprises lists Class A shares and keeps super-voting Class B shares "
        "in the family.",
        "1981: Launches the <b>Crown Network</b>, a 24-hour cable channel, and starts "
        "buying stations in 30 markets.",
        "1987: A hostile takeover of Paragon Pictures, a century-old Hollywood studio. The "
        "trade press calls it “the Atlanta Invasion.”",
    ]),
    ("1990–2005: Going Global", [
        "1990: Signs the first <b>Crown License</b> with Smilley Corporation, the master "
        "licensing deal that puts Donohue characters and brands on Smilley products (see "
        "Document 06).",
        "1995: Buys the Continental Broadcasting Company, a national broadcast network, "
        "and rebrands it <b>DBC</b>.",
        "1998: Opens the first <b>Donohue Worlds</b> theme park in Orlando and takes a 4% "
        "strategic stake in Smilley Corporation.",
        "2001: Launches Beacon News Network (BNN), a 24-hour global news channel.",
        "2004: Acquires Crown Comics and its universe of heroes.",
    ]),
    ("2006–2019: The Natasha Era", [
        long_date(D(2006, 1, 9)) + ": Alexander Donohue dies at 89. Victor becomes "
        "Chairman and Natasha becomes CEO at 34.",
        "2009: Donohue Games is founded; its <i>Kingdom of Kora</i> franchise becomes the "
        "best-selling game series of the decade.",
        "2012: Donohue Global Holdings takes a 12% strategic stake in Blackwater Security "
        "International (see Document 05).",
        "2016: <b>Donohue+</b> streaming launches worldwide and reaches 100 million "
        "subscribers in 14 months.",
        "2018: Donohue Worlds opens in Tokyo, Paris, and Dubai.",
        "2019: Market capitalization passes $1 trillion for the first time.",
    ]),
    ("2020–2026: The $10 Trillion Company", [
        "2020: Donohue+ passes 500 million subscribers during the pandemic, and Donohue "
        "Live pioneers virtual concerts and Broadway streams.",
        "2021: Donohue Studios AI launches, with the <b>Donohue Creator Guarantee</b>: "
        "every AI tool pays human artists royalties.",
        "2023: Market cap passes $5 trillion. Marc-Anthony wins his Oscar for a Donohue "
        "Pictures film.",
        long_date(D(2025, 12, 31)) + ": The stock closes at $250 a share. Market cap: "
        "<b>$10.0 trillion</b>.",
        long_date(D(2026, 1, 5)) + ": Series premiere. Victor's Succession Covenant names "
        "Marc-Anthony President &amp; COO.",
    ]),
]
for era, items in eras:
    story.append(P(era, h2))
    story += bullets(items)

story += [
    P("Divisions (2026)", h1),
    table([
        ["Division", "Leader", "What it is"],
        ["Donohue Pictures (incl. Paragon)", "Natasha Bullock (oversight)",
         "The world's No. 1 film studio"],
        ["Donohue Broadcasting Group", "Martin Olson, President",
         "DBC network, the Crown Network, 212 local stations"],
        ["Donohue+", "", "Streaming, 1.3 billion subscribers"],
        ["Donohue Records &amp; Publishing", "", "No. 1 music label and catalog"],
        ["Beacon Media", "", "<i>The Atlanta Beacon</i>, BNN news, <i>Crown</i> magazine, "
         "book publishing"],
        ["Donohue Worlds", "", "Theme parks, resorts, cruise line"],
        ["Donohue Games", "", "Games, esports, <i>Kingdom of Kora</i>"],
        ["Donohue Live", "", "Concerts, Broadway (Donohue Theatricals), live events"],
        ["Donohue Consumer Licensing", "Reports to Marc-Anthony",
         "Licenses Donohue IP worldwide. Home of the Crown License with Smilley"],
        ["Donohue Studios AI", "", "AI production tools under the Creator Guarantee"],
        ["Crown Comics", "", "Publisher of the Crown Universe of heroes"],
    ], [1.9 * inch, 1.6 * inch, 3.0 * inch]),
    Spacer(1, 6),
    P("The Crown License and the Smilleys", h2),
    P("Donohue Consumer Licensing sells Smilley Corporation the rights to put Donohue "
      "characters, films, and brands on toys, clothes, cosmetics, and home goods. That one "
      "agreement drives about <b>41% of Smilley revenue</b> and only about 0.6% of Donohue's. "
      "Donohue is also Smilley's largest outside shareholder. The current license expires "
      "at <b>11:59 PM on Monday, August 31, 2026</b>. That deadline drives Season 1."),
    PageBreak(),
]

# ---------------- SHARE DISTRIBUTION ----------------
DE_TOTAL = 40.0  # billion shares
B_VOTES = 10
de_rows = [
    # holder, class B, class A (billions of shares)
    ("Donohue Global Holdings, Inc.", 9.0, 1.0),
    ("The Donohue Foundation", 0.0, 1.2),
    ("Directors &amp; officers (excl. DGH)", 0.0, 0.2),
    ("Employee stock plans (ESOP &amp; 401k)", 0.0, 0.8),
    ("Index &amp; passive fund managers", 0.0, 9.6),
    ("Active institutional investors", 0.0, 8.4),
    ("Public pension funds", 0.0, 2.4),
    ("Sovereign wealth funds", 0.0, 2.0),
    ("Retail &amp; other public holders", 0.0, 5.4),
]
tot_b = sum(r[1] for r in de_rows)
tot_a = sum(r[2] for r in de_rows)
assert abs(tot_b + tot_a - DE_TOTAL) < 1e-9
tot_votes = tot_b * B_VOTES + tot_a
rows = [["Holder", "Class B (bn)", "Class A (bn)", "Economic %", "Voting %", "Value"]]
for h, b, a in de_rows:
    econ = (a + b) / DE_TOTAL
    vote = (b * B_VOTES + a) / tot_votes
    rows.append([h, f"{b:.1f}", f"{a:.1f}", f"{econ:.1%}", f"{vote:.1%}",
                 f"${econ * 10_000:,.0f}B"])
rows.append(["<b>TOTAL</b>", f"<b>{tot_b:.1f}</b>", f"<b>{tot_a:.1f}</b>", "<b>100%</b>",
             "<b>100%</b>", "<b>$10,000B</b>"])

story += [
    P("Share Distribution: Donohue Enterprises, Inc. (NYSE: DNHU)", h1),
    P("The Donohue Company uses the same kind of <b>dual-class structure</b> that "
      "controls many real family media empires: the public owns most of the economic "
      "value, while the family keeps control through super-voting shares held by a "
      "private holding company."),
    *bullets([
        "<b>Class A common</b> (NYSE: DNHU): 1 vote per share, publicly traded.",
        f"<b>Class B common</b>: {B_VOTES} votes per share, not traded, 100% owned by "
        "Donohue Global Holdings. Converts to Class A if sold outside the family.",
        f"Shares outstanding: {DE_TOTAL:.1f} billion at $250.00 = $10.0 trillion market cap.",
    ]),
    table(rows, [2.3 * inch, 0.8 * inch, 0.8 * inch, 0.8 * inch, 0.75 * inch,
                 0.85 * inch]),
    Spacer(1, 6),
    P("RESULT: The family owns 25% of the company's value ($2.5 trillion, the Donohue "
      "family fortune) and controls 75.2% of the vote.", answer),
]

# ---------------- DGH ----------------
dgh = [
    ("Victor Donohue (Victor Donohue Revocable Trust)", 26, 51),
    ("Joan Donohue (Joan Mercer Donohue Trust)", 14, 10),
    ("Natasha Bullock (Natasha Donohue Bullock Trust)", 12, 15),
    ("Jasmine Olson (Jasmine Donohue Olson Trust)", 12, 12),
    ("Alvin Donohue (Alvin Donohue Trust)", 8, 5),
    ("Theodore Donohue Family Trust", 8, 0),
    ("Marc-Anthony Bullock (Dynasty Trust, sub-trust)", 8, 7),
    ("Martin Olson (Dynasty Trust, sub-trust)", 4, 0),
    ("Elxa Jackson (Dynasty Trust, sub-trust)", 2, 0),
    ("Grace Bullock (Dynasty Trust, sub-trust)", 2, 0),
    ("Mallory Olson (Dynasty Trust, sub-trust)", 2, 0),
    ("The Donohue Foundation", 2, 0),
]
assert sum(r[1] for r in dgh) == 100 and sum(r[2] for r in dgh) == 100
drows = [["Owner", "Economic %", "Value", "Voting % (Crown Voting Trust)"]]
for o, e, v in dgh:
    drows.append([o, f"{e}%", f"${e * 25:,}B", f"{v}%"])
drows.append(["<b>TOTAL</b>", "<b>100%</b>", "<b>$2,500B</b>", "<b>100%</b>"])

story += [
    P("Share Distribution: Donohue Global Holdings, Inc. (private)", h1),
    P("Donohue Global Holdings (DGH) is the family's private holding company. It owns all "
      "the Class B shares and 1 billion Class A shares, which is 25% of the economic value "
      "and 75.2% of the vote. DGH itself is owned by family trusts. Its <b>votes</b> are "
      "pooled in the <b>Crown Voting Trust</b>, set up by Alexander in 1978 at the IPO, "
      "so that the family always votes as one bloc."),
    table(drows, [3.1 * inch, 0.9 * inch, 0.9 * inch, 1.6 * inch]),
    Spacer(1, 6),
    P("Rules that drive the drama", h2),
    *bullets([
        "<b>The Chairman's Share.</b> The Chairman of The Donohue Company serves as sole "
        "trustee of the Crown Voting Trust and personally votes the 51% bloc.",
        "<b>Section 7 of the Alexander Charter.</b> The sitting Chairman may designate the "
        "next trustee. If he dies without a designation, trusteeship passes to the "
        "eldest child. That's Jasmine, and after her, Martin.",
        "<b>The 1976 Stripping.</b> When Victor was made CEO, Alexander converted "
        "Theodore's branch to economic-only units: 8% of the money and 0% of the vote. "
        "Theodore has contested it privately for fifty years.",
        "<b>The Dynasty Trust.</b> The third generation holds economic units only, except "
        "Marc-Anthony, whom Victor gave 7% of the vote on January 5, 2026, the first "
        "grandchild with a vote.",
        "<b>Alvin's children.</b> Under the Charter, any biological child of a Donohue "
        "trust holder becomes a Dynasty Trust beneficiary. Every paternity claim against "
        "Alvin is a claim on the fortune.",
        "<b>Victor's 80th (Saturday, May 30, 2026).</b> Victor planned to announce his "
        "Section 7 designation that night. He collapsed before he could say the name.",
    ]),
    P("Net worth check (as of January 5, 2026)", h2),
    table([
        ["Person", "DGH stake", "Other holdings", "Approx. net worth"],
        ["Victor Donohue", "$650B", "Real estate, art, Broadway royalties", "~$680B"],
        ["Joan Donohue", "$350B", "Film royalties, jewels", "~$365B"],
        ["Natasha Bullock", "$300B", "CEO compensation, film &amp; music royalties", "~$330B"],
        ["Jasmine Olson", "$300B", "", "~$305B (with Peter's fortune, far more)"],
        ["Marc-Anthony Bullock", "$200B", "58% of BSI ($754B), personal investments ($40B+)",
         "<b>$994B+, rising daily</b>"],
        ["Martin Olson", "$100B", "", "~$104B"],
    ], [1.6 * inch, 0.9 * inch, 2.5 * inch, 1.5 * inch]),
]

build(OUT, story, "Beyond the Crest — The Donohue Company",
      "BEYOND THE CREST — The Donohue Company — Writers' Room Confidential")
