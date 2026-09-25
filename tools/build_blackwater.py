"""Builds docs/05_Blackwater.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from btc_pdf import (P, h1, h2, italic, answer, bullets, table, scene, long_date,
                     build, cover)

OUT = "docs/05_Blackwater.pdf"
D = dt.date

story = cover("Blackwater — Document 05", [
    "<b>The Blackwater Syndicate</b>: secretly founded " + long_date(D(2010, 9, 18)),
    "<b>Blackwater Security International (BSI)</b>: founded " + long_date(D(2011, 10, 3)),
    "<b>Founder of both:</b> Marc-Anthony Bullock",
    "<b>WRITERS' ROOM EYES ONLY</b>",
])
story.append(PageBreak())

# ---------------- SYNDICATE ----------------
story += [
    P("Part One: The Blackwater Syndicate", h1),
    P("The Blackwater Syndicate is a 100% criminal organization, a true mafia, and the "
      "largest, most powerful, most feared, most deadly, and most valuable criminal "
      "organization in the world. It is also, strangely, the most beloved. It spares no "
      "expense on the communities it protects. Its boss is known inside the organization "
      "only as <b>“The Architect.”</b> The Architect is Marc-Anthony Bullock.",
      answer),
    table([
        ["Field", "Detail"],
        ["Founded", long_date(D(2010, 9, 18)) + ", Atlanta. Marc-Anthony was 18"],
        ["Founding members", "Marc-Anthony Bullock, Amond Baker, Kane Mitchell"],
        ["Headquarters", "None on paper. The Table meets in rotating locations; the "
                         "Atlanta seat is a sealed room beneath a BSI training facility"],
        ["Estimated annual take", "$400–$600 billion across all operations "
                                  "(FBI estimate: “unknowable”)"],
        ["Made members", "About 9,000 worldwide"],
        ["Associates", "Several hundred thousand, most of whom have never heard the "
                       "word “Architect”"],
        ["Territories", "43 countries. Every major U.S. city"],
        ["Street name", "“Blackwater,” after the dark stretch of the "
                        "Chattahoochee below Belmont Crest where Marc used to fish with "
                        "his great-grandfather"],
        ["Police name", "APD files call it the “ghost network”; the FBI calls "
                        "it “Organization X”"],
        ["Calling card", "A black river stone, left behind only when the Syndicate wants "
                         "credit"],
    ], [1.8 * inch, 4.7 * inch]),

    P("The Chain of Command", h2),
    table([
        ["Rank", "Name", "Public face", "Born / Age"],
        ["The Architect (Boss)", "Marc-Anthony Bullock",
         "Actor, President &amp; COO of The Donohue Company, BSI founder",
         "Jan 5, 1992 / 34"],
        ["Underboss", "Amond Baker", "Businessman, Marc's best friend", "Feb 10, 1992 / 33"],
        ["Consigliere", "Ezekiel “Zeke” Hart",
         "BSI General Counsel; retired Army intelligence colonel and former federal "
         "prosecutor", "Apr 4, 1958 / 67"],
        ["Enforcer", "Kane Mitchell", "Marc's head of personal security", "Nov 17, 1990 / 35"],
        ["Intelligence Chief", "Nova Sinclair", "BSI Chief Technology Officer",
         "Jan 29, 1996 / 29"],
        ["The Banker", "Cyrus Bell", "Private wealth manager", "Dec 1, 1979 / 46"],
        ["Captain, Atlanta", "Darnell “Deuce” Whitaker", "Nightclub owner",
         "Jun 12, 1987 / 38"],
        ["Captain, East Coast", "Idris Vance", "Real estate developer, New York",
         "May 25, 1981 / 44"],
        ["Captain, West Coast", "Tasha “Queenie” Monroe",
         "Film financier, Los Angeles", "Oct 3, 1986 / 39"],
        ["Captain, Africa", "Chidi Okafor", "Shipping magnate, Lagos", "Aug 18, 1979 / 46"],
        ["Captain, Europe", "Lorenzo Ferraro", "Hotelier, Milan", "Jan 14, 1975 / 50"],
    ], [1.35 * inch, 1.5 * inch, 2.45 * inch, 1.2 * inch]),
    P("<b>The Table</b> is the ruling council: the Architect, Underboss, Consigliere, "
      "Enforcer, Intelligence Chief, Banker, and the five Captains. Only the Table has "
      "ever seen the Architect's face. Everyone below them takes orders through the "
      "Underboss."),

    P("The Seven Laws of Blackwater", h2),
    P("Every made member swears these on a black river stone:", italic),
    *bullets([
        "<b>I.</b> Children are never touched, never used, never harmed.",
        "<b>II.</b> No powder. Blackwater doesn't sell poison to its own people.",
        "<b>III.</b> No one is ever bought or sold.",
        "<b>IV.</b> The neighborhood eats first.",
        "<b>V.</b> Silence is the price of the stone.",
        "<b>VI.</b> Betrayal is answered once, and completely.",
        "<b>VII.</b> The Architect's family is the Syndicate's family. Touch them and the "
        "river rises.",
    ]),

    P("What Blackwater Does", h2),
    P("The rackets (always named on screen, never shown as a how-to):", italic),
    *bullets([
        "Underground high-stakes gambling and a global sports book.",
        "Smuggling of luxury goods, art, and high-end contraband.",
        "Protection: the Syndicate “taxes” corrupt businesses and landlords "
        "who prey on the neighborhoods under its care.",
        "Loan-sharking to the powerful. Never to the poor.",
        "Money laundering through shell companies on five continents.",
        "Political corruption: judges, councilmen, and commissioners on the payroll.",
        "Intelligence brokering: secrets bought, sold, and buried.",
        "Fixing: Blackwater makes problems disappear, for a price or for a favor.",
    ]),
    P("Why it's beloved: “The Envelope”", h2),
    P("Every Friday, in every city Blackwater controls, envelopes appear: rent paid, "
      "medical debt erased, funeral costs covered, HBCU tuition settled. More than $20 "
      "billion a year flows back into Black neighborhoods, and nobody knows where it "
      "comes from. Grandmothers on the Westside light candles for “the people from "
      "the river.”"),
    PageBreak(),
    P("History of the Syndicate", h1),
]

eras = [
    ("2010: Genesis", [
        "Summer 2010: Developer Warren Kessler and a ring of crooked city officials bleed "
        "Baker &amp; Sons Contracting dry with rigged permits and a fraudulent lien. Gerald "
        "Baker loses nearly everything, and the courts shrug.",
        "July to September 2010: Marc-Anthony, 18 and a year out of Yale, takes them apart "
        "in 90 days using his trust fund, secrets that Amond digs up, and Kane Mitchell's "
        "persuasion. Kessler flees the country. Two officials resign. The Bakers get "
        "their business back.",
        long_date(D(2010, 9, 18)) + ": On the riverbank below Belmont Crest, Marc, Amond, "
        "and Kane each pick up a black river stone. The Blackwater Syndicate is born.",
    ]),
    ("2011–2014: Atlanta", [
        "2011: Ezekiel Hart, Marc's former mock-trial coach and a retired colonel, becomes "
        "consigliere.",
        long_date(D(2011, 10, 3)) + ": BSI is incorporated as the Syndicate's legitimate "
        "twin.",
        "2012: Nova Sinclair, a 16-year-old hacker who broke into BSI's servers for fun, is "
        "recruited instead of prosecuted.",
        long_date(D(2013, 8, 24)) + ": <b>“The Peace of Peachtree.”</b> Marc "
        "brokers an end to a three-crew war in Atlanta, and all three crews swear to "
        "Blackwater. Killings in the city's worst neighborhoods fall by half in a year.",
    ]),
    ("2015–2019: National", [
        "2015: New York (Idris Vance) and Los Angeles (Queenie Monroe) join the Table.",
        "2017: Chicago, Houston, Detroit, and Miami fall in line. The Morrow Organization "
        "loses Atlanta's ports to Blackwater, and Vincent Morrow's hatred begins.",
        "2019: The FBI opens a file on “Organization X.” It has no names.",
    ]),
    ("2020–2025: Global", [
        "2020: Lagos (Chidi Okafor) and Milan (Lorenzo Ferraro) join. Blackwater becomes the "
        "largest criminal organization on Earth.",
        "2021: The Syndicate buries Julian Cummings's hit-and-run: the car and the evidence "
        "vanish. Marc keeps both, “just in case.” Blackwater quietly pays the "
        "victim's daughter, Journee Holloway, through an anonymous scholarship. The same "
        "February, a sealed family court order places Lyric with Marc.",
        "2024: Terrence “T-Bone” Gaines, an Atlanta lieutenant, starts selling "
        "Syndicate secrets.",
        long_date(D(2026, 1, 4)) + ", 11:40 PM: T-Bone is murdered under the Paces Ferry "
        "Road bridge. Blackwater didn't do it. (Martin Olson did. The audience learns this "
        "in Ep #0060.)",
    ]),
]
for era, items in eras:
    story.append(P(era, h2))
    story += bullets(items)

story += [
    P("Enemies &amp; Threats (Season 1)", h2),
    table([
        ["Threat", "Who", "Danger"],
        ["Law enforcement", "Det. Jeremy Jackson; FBI SAC Nadia Brooks",
         "Jeremy's “ghost network” file and the joint task force"],
        ["The family", "Chief Elxa Jackson",
         "Doesn't know. She suspects her father. Figures it out in the finale"],
        ["Rival mob", "Vincent Morrow, the Morrow Organization",
         "Wants Atlanta back. Uses Alvin to reach the World Cup security plans"],
        ["The cousin", "Martin Olson", "Knows “the Architect lives on the ridge.” "
                                       "Killed T-Bone"],
        ["The press", "Journee Holloway", "Digging into 2021 without knowing it leads "
                                          "to Blackwater"],
    ], [1.3 * inch, 2.2 * inch, 3.0 * inch]),

    P("Who Knows Marc Is The Architect (as of Jan 5, 2026)", h2),
    *bullets([
        "<b>The Table</b>: Amond, Hart, Kane, Nova, Cyrus, and the five Captains.",
        "<b>Grace Bullock</b>: knows, and would hide a body for him.",
        "<b>Arianna Cummings</b>: knows the Syndicate exists and that Marc runs it. "
        "Chooses not to know details.",
        "<b>Nobody else.</b> Robert figures it out in Ep #0147. Elxa figures it out in "
        "Ep #0170.",
    ]),
    PageBreak(),
]

# ---------------- BSI ----------------
story += [
    P("Part Two: Blackwater Security International (BSI)", h1),
    P("BSI is the legitimate company: a multinational private security and "
      "risk-management corporation and one of the largest, most successful, powerful, "
      "influential, respected, beloved, feared, and valuable companies in the world. It "
      "is 100% legal on paper. It is also the Syndicate's eyes, ears, and armor.",
      answer),
    table([
        ["Field", "Detail"],
        ["Legal name", "Blackwater Security International, Inc. (private)"],
        ["Founded", long_date(D(2011, 10, 3)) + ", Atlanta, by Marc-Anthony Bullock, 19"],
        ["Headquarters", "BSI Tower, 2011 Northside Parkway NW, Atlanta, GA 30327"],
        ["Chairman", "Marc-Anthony Bullock"],
        ["CEO", "Gen. (Ret.) Calvin Whitmore, the clean public face, who has no "
                "knowledge of the Syndicate"],
        ["General Counsel", "Ezekiel Hart"],
        ["CTO", "Nova Sinclair"],
        ["Valuation", "<b>$1.3 trillion</b> (last private round, November 2025)"],
        ["Annual revenue", "$118 billion"],
        ["Employees", "410,000 in 71 countries"],
        ["Clients", "Governments, 83 of the Fortune 100, royal families, stadiums, "
                    "Hollywood, and all of Belmont Crest"],
    ], [1.8 * inch, 4.7 * inch]),
    P("Divisions", h2),
    *bullets([
        "<b>BSI Executive Protection</b>: bodyguards for heads of state and superstars.",
        "<b>BSI Cyber</b>: cybersecurity and threat intelligence.",
        "<b>BSI Crisis Response</b>: kidnap and ransom, evacuations, disaster response.",
        "<b>BSI Events</b>: security for the Olympics, the Super Bowl, and the <b>2026 "
        "FIFA World Cup matches in Atlanta</b> (Season 1, Eps #0111–#0134).",
        "<b>BSI Maritime</b>: port and shipping security, which also happens to cover "
        "Blackwater's smuggling routes.",
        "<b>BSI Risk</b>: corporate investigations and political risk consulting.",
    ]),
    P("BSI Ownership", h2),
    table([
        ["Owner", "Stake", "Value"],
        ["Marc-Anthony Bullock", "58%", "$754B"],
        ["Management &amp; employees", "20%", "$260B"],
        ["The Donohue Company (strategic stake, 2012)", "12%", "$156B"],
        ["Institutional private investors", "10%", "$130B"],
        ["<b>TOTAL</b>", "<b>100%</b>", "<b>$1.3T</b>"],
    ], [3.5 * inch, 1.0 * inch, 2.0 * inch]),
    Spacer(1, 6),
    P("How the Syndicate hides inside BSI", h2),
    *bullets([
        "BSI's security contracts give Blackwater access to ports, stadiums, and "
        "government buildings.",
        "BSI Cyber monitors every threat to the Syndicate, including police databases.",
        "The name is the danger: Jeremy Jackson finds “Blackwater” in T-Bone's "
        "phone and starts looking at BSI (Eps #0036, #0066, #0109).",
        "Publicly, Marc says BSI was named after the black water of the Chattahoochee "
        "where his great-grandfather taught him to fish. That part is true.",
    ]),
    *scene("IN THE ARCHITECT'S OWN WORDS", [
        ("MARC-ANTHONY", ("to the Table, gentle", "We're not the good guys. Let's never "
                          "lie about that. We're just the guys who make sure the bad "
                          "ones are scared of something.")),
    ]),
]

build(OUT, story, "Beyond the Crest — Blackwater",
      "BEYOND THE CREST — Blackwater — Writers' Room EYES ONLY")
