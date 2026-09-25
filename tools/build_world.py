"""Builds docs/11_World_Building.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from cast import CAST, PARTY, MARC_PLATFORM, MARC_LONG_TERM
from btc_pdf import (P, h1, h2, italic, answer, bullets, table, age_on, long_date, build,
                     cover)

OUT = "docs/11_World_Building.pdf"
D = dt.date

story = cover("World Building — Document 11", [
    "The world of <i>Beyond the Crest</i>, from 1939 to the premiere",
    "<b>Monday, January 5, 2026</b>",
])
story.append(PageBreak())

# ---------------- 1. RULES ----------------
story += [
    P("1. The Rules of This World", h1),
    P("<i>Beyond the Crest</i> takes place in our world with one great difference: in "
      "1939, a paperboy from Auburn Avenue named Alexander Donohue started a newspaper, "
      "and never stopped. Everything that grew from that decision is real in this "
      "universe. Everything else is the world as we know it.", answer),
    *bullets([
        "<b>Real places and institutions.</b> Atlanta, Georgia, the United States, "
        "Spelman, Morehouse, Grady, Lake Lanier, the Chattahoochee, the NYSE, the Oscars, "
        "the Tonys, the FIFA World Cup: all of it exists and works the way it does in "
        "real life.",
        "<b>Fictional people in power.</b> Every President, governor, mayor, police chief, "
        "judge, CEO, and billionaire seen or named on screen is fictional. Real public "
        "figures are never portrayed.",
        "<b>Real history, bent by the Donohues.</b> The big events of American history "
        "still happen: the war, the movement, the Olympics, the crash, the pandemic. The "
        "Donohues were in the room for many of them.",
        "<b>Real calendar.</b> Holidays, election days, and award shows land on their "
        "real 2026 dates.",
        "<b>Real parties.</b> Democrats and Republicans are named on screen. Every "
        "character's party is listed in Section 12.",
        "<b>In-universe media only.</b> Every article, broadcast, and post comes from "
        "outlets and platforms that exist inside this world (Section 6).",
    ]),

    # ---------------- 2. DONOHUE EFFECT ----------------
    P("2. The Donohue Effect: How This World Differs From Ours", h1),
    table([
        ["In our world", "In the world of Beyond the Crest"],
        ["The most valuable company is worth a few trillion dollars",
         "The Donohue Company is worth <b>$10 trillion</b>. No other company is worth even "
         "half as much"],
        ["Hollywood is in Los Angeles",
         "Atlanta is <b>the media capital of the world</b>. More film, TV, and music is "
         "made in metro Atlanta than in Los Angeles and New York combined"],
        ["The richest people are tech founders",
         "The richest person on Earth is a 34-year-old Black actor and heir: "
         "<b>Marc-Anthony Bullock</b>"],
        ["Black-owned media is a small share of the industry",
         "The largest media company on the planet has been Black-owned since 1939"],
        ["Organized crime is fragmented",
         "One syndicate, <b>Blackwater</b>, is larger than any criminal organization in "
         "history, and it pays rent for grandmothers"],
        ["Consumer brands advertise everywhere",
         "Almost no consumer brand can reach a mass audience without buying Donohue "
         "airtime. Smilley hates that more than anyone"],
        ["EGOTs are extremely rare",
         "One Atlanta family holds two of them at the premiere, and four by June 2026"],
    ], [2.4 * inch, 4.1 * inch]),
    PageBreak(),
]

# ---------------- 3. USA ----------------
story += [
    P("3. The United States, January 2026", h1),
    P("The Nation", h2),
    *bullets([
        "America is heading into its <b>250th birthday</b> on Saturday, July 4, 2026, "
        "the Semiquincentennial. The Donohue Company holds the broadcast rights to the "
        "national celebration (Ep #0126).",
        "The country is co-hosting the <b>2026 FIFA World Cup</b> (June 11 – July 19). "
        "Atlanta hosts eight matches, including a semifinal on Wednesday, July 15 "
        "(Ep #0133). BSI runs security for the Atlanta matches.",
        "Midterm elections are on <b>Tuesday, November 3, 2026</b>. Every House seat, "
        "including Jasmine Olson's, is on the ballot.",
        "The 2028 presidential race has quietly begun. Georgia Attorney General Arianna "
        "Cummings is one of the most talked-about possible candidates.",
    ]),
    P("Washington (all fictional)", h2),
    table([
        ["Office", "Holder", "Born / Age", "Notes"],
        ["President (R)", "Richard Aldridge", f"Mar 18, 1958 / {age_on(D(1958, 3, 18))}",
         "Former governor of Ohio. Inaugurated Jan 20, 2025. Courts Donohue money and "
         "fears Donohue cameras"],
        ["Vice President (R)", "Karen Molina", f"Sep 2, 1969 / {age_on(D(1969, 9, 2))}",
         "Former U.S. senator from Arizona. Already the front-runner for 2028, and "
         "watching Arianna closely"],
        ["U.S. Representative, Georgia (D)", "Jasmine Olson", "Mar 23, 1970 / 55",
         "In office since 1997. Senior member of the House Energy and Commerce Committee, "
         "which oversees the media industry her family dominates. Critics never stop "
         "pointing that out"],
    ], [1.3 * inch, 1.2 * inch, 1.1 * inch, 2.9 * inch]),
    P("The American Economy", h2),
    *bullets([
        "The stock market is near all-time highs, carried by media, AI, and "
        "entertainment. The Donohue Company alone is about one-sixth of the S&amp;P "
        "500's value.",
        "The real-world tech giants exist, but none is worth even half of The Donohue "
        "Company.",
        "<b>The most valuable companies in this story:</b> The Donohue Company "
        "($10.0 trillion, public), Smilley Corporation ($1.6 trillion, public), and "
        "Blackwater Security International ($1.3 trillion, private).",
    ]),
    P("The Crown Rich List, January 2026", h2),
    P("Published every January by <i>Crown</i> magazine, which the Donohues own. Rivals "
      "call it “the family newsletter.”", italic),
    table([
        ["Rank", "Name", "Net worth", "Source"],
        ["1", "Marc-Anthony Bullock", "$994B+", "BSI, The Donohue Company, investments"],
        ["2", "Victor Donohue", "~$680B", "The Donohue Company"],
        ["3", "Joan Donohue", "~$415B", "The Donohue Company, royalties"],
        ["4", "Natasha Bullock", "~$330B", "The Donohue Company"],
        ["5", "Jasmine &amp; Peter Olson", "~$345B combined", "The Donohue Company, "
                                                          "Olson Institute"],
        ["6", "Alvin Donohue", "~$200B", "The Donohue Company"],
        ["7", "Theodore Donohue family", "~$200B", "The Donohue Company"],
        ["8", "Augustus “Gus” Smilley", "~$152B", "Smilley Corporation"],
        ["9", "Leonard Smilley", "~$112B", "Smilley Corporation"],
        ["10", "Martin Olson", "~$104B", "The Donohue Company"],
    ], [0.5 * inch, 2.0 * inch, 1.3 * inch, 2.7 * inch]),
    P("Every name in the top ten is a Donohue or a Smilley. Gus Smilley "
      "has a framed copy of every list since 1996, each with the Donohue names blacked "
      "out.", italic),
    PageBreak(),
]

# ---------------- 4. GEORGIA ----------------
story += [
    P("4. Georgia", h1),
    table([
        ["Office", "Holder", "Notes"],
        ["Governor (D)", "William Hartley (b. Jun 6, 1962; 63)",
         "Serving his second and final term, so 2026 is an open-seat governor's race. "
         "Appointed Arianna Cummings Attorney General"],
        ["Attorney General (D)", "Arianna Cummings (b. Oct 25, 1992; 33)",
         "Appointed Mon, Mar 17, 2025, after Attorney General Bradley Keane resigned in a "
         "bribery scandal. Georgia elects its AG, so she must win in 2026: she beats State "
         "Rep. Cordell Haynes in the May 19 Democratic primary (Ep #0094) and faces "
         "Republican nominee Grant Hollister, a former U.S. Attorney, on November 3"],
        ["Fulton County District Attorney (D)", "Colette Barnes (b. Apr 30, 1979; 46)",
         "Arianna's former chief deputy, appointed interim DA in 2025. Loyal to Arianna, "
         "for now"],
    ], [1.6 * inch, 2.0 * inch, 2.9 * inch]),
    P("Georgia in 2026", h2),
    *bullets([
        "<b>Election calendar:</b> primary Tuesday, May 19 (Ep #0094); runoff Tuesday, "
        "June 16 (Ep #0113); general election Tuesday, November 3.",
        "<b>The open governor's race</b> is the biggest prize in the South, and every "
        "candidate wants a Donohue endorsement. Season 2 storyline.",
        "<b>The film industry:</b> Georgia's production boom began in the 1950s, when "
        "Donohue Pictures built its first soundstages. Today “the Peach State” "
        "is the world's busiest filming location.",
        "<b>Lake Lanier</b>, an hour north of Atlanta, is where the rich go for summer and "
        "for secrets. It's the setting of the 2011 night that started it all, and of the "
        "Season 1 finale.",
    ]),

    # ---------------- 5. ATLANTA ----------------
    P("5. Atlanta, “The Media Capital of the World”", h1),
    P("Metro population about 6.4 million. In this world Atlanta is where the world's "
      "stories get made. Tourists take the Donohue Studios tour the way they visit the "
      "Hollywood sign in ours."),
    table([
        ["City Office", "Holder", "Notes"],
        ["Mayor (D)", "Denise Whitlock (b. Dec 15, 1972; 53)",
         "Second term. A Belmont Crest outsider who resents the ridge and needs its "
         "money"],
        ["Chief of Police, APD", "Elxa Jackson (b. Aug 29, 1990; 35)",
         "Sworn in Tue, Sep 2, 2025. The youngest chief in the city's history"],
        ["Former Chief", "Walter Jackson (b. Jan 18, 1956; 69)", "Chief 2011–2019"],
    ], [1.5 * inch, 2.2 * inch, 2.8 * inch]),
    P("Map of the Story", h2),
    table([
        ["Place", "Where", "Why it matters"],
        ["Belmont Crest", "1958 Belmont Crest Pkwy NW (30327)", "Home of the Donohues. "
                                                              "See Document 04"],
        ["Tuxedo Park", "Buckhead, across the ridge", "Home of the Smilleys"],
        ["Donohue Tower", "1939 Peachtree St NE, Midtown", "108 stories, the tallest "
                                                          "building in the South"],
        ["Smilley Plaza", "3400 Peachtree Rd NE, Buckhead", "Built in 1996 so Gus could "
                                                           "see Donohue Tower from his desk"],
        ["BSI Tower", "2011 Northside Pkwy NW", "Blackwater's legitimate face"],
        ["Atlanta Metropolitan Medical Center", "Midtown", "Peter's hospital. Victor's "
                                                          "surgery (Ep #0102)"],
        ["Westbrook Academy", "Buckhead", "School of Emma, Victoria, Lyric, and Trey"],
        ["APD Headquarters", "Downtown", "Elxa's office and Jeremy's squad room"],
        ["Fulton County Courthouse", "Downtown", "The Whitaker trial"],
        ["The Beacon Museum", "190 Auburn Ave NE, Sweet Auburn", "Alexander's original "
                                                                "1939 press room"],
        ["<i>The Peach Ledger</i>", "Auburn Avenue", "Journee's newsroom, two blocks from "
                                                     "the Beacon Museum"],
        ["The Chancellor Club", "Midtown", "Martin's private club, where he makes his "
                                           "offers"],
        ["SOVEREIGN", "Buckhead Village", "Alvin's nightclub, opened May 2026"],
        ["The Well", "Westside", "Deuce Whitaker's nightclub and Blackwater's Atlanta "
                                 "base"],
        ["Lucky Seven Karaoke", "Buford Highway", "Vincent Morrow's back-room office"],
        ["Paces Ferry Road bridge", "Chattahoochee River", "Where T-Bone Gaines died"],
        ["The downtown stadium", "Downtown", "World Cup semifinal (Ep #0133)"],
    ], [1.8 * inch, 2.0 * inch, 2.7 * inch]),
    PageBreak(),
]

# ---------------- 6. MEDIA ----------------
story += [
    P("6. The Media Universe", h1),
    P("Every headline, broadcast, and post in the show comes from these outlets and "
      "platforms. Knowing who owns what tells you who's lying.", answer),
    P("Owned by The Donohue Company", h2),
    table([
        ["Outlet", "What it is"],
        ["<i>The Atlanta Beacon</i>", "The family's original 1939 paper; now the South's "
                                      "newspaper of record"],
        ["BNN (Beacon News Network)", "24-hour global news channel"],
        ["DBC", "National broadcast network. Home of <i>Hollywood Heat</i>, hosted by "
                "Brielle Knox"],
        ["The Crown Network", "Cable entertainment channel"],
        ["WDON-TV", "Atlanta's No. 1 local station"],
        ["<i>Crown</i> magazine", "Black lifestyle and society bible since 1947; "
                                  "publishes the Crown Rich List"],
        ["Donohue+", "Streaming service, 1.3 billion subscribers"],
    ], [2.2 * inch, 4.3 * inch]),
    P("Independent and Rival Outlets", h2),
    table([
        ["Outlet", "What it is"],
        ["<i>The Peach Ledger</i>", "Scrappy independent investigative outlet. Journee "
                                    "Holloway's home. No Donohue money, on principle"],
        ["<i>The Tea Kettle ATL</i>", "Anonymous gossip blog with the biggest audience in "
                                      "Atlanta. Secretly written by Harmony Divine"],
        ["<i>Marquee</i>", "The entertainment industry's trade paper, based in Los "
                           "Angeles: casting, box office, deals"],
        ["<i>The Capitol Wire</i>", "Washington politics outlet; covers Jasmine and the "
                                    "2028 field"],
        ["<i>Wall &amp; Broad</i>", "Financial daily; covers the Crown License war"],
        ["Channel 7 Atlanta", "The only local TV news outlet not owned by Donohue"],
    ], [2.2 * inch, 4.3 * inch]),
    P("Social Platforms", h2),
    table([
        ["Platform", "What it is", "Who uses it"],
        ["Chirp", "Short text posts and trending hashtags", "Everyone. Breaking news "
                                                           "breaks here first"],
        ["Glimpse", "Photos and 24-hour stories", "Grace, Sienna, Coco, the twins"],
        ["Loop", "Short vertical video", "The kids; Marc's unhinged comedy clips"],
        ["Pulse", "Live streaming", "Galas, verdicts, and anything that might go wrong"],
    ], [1.1 * inch, 2.5 * inch, 2.9 * inch]),
    P("The Donohue Company owns 30% of Loop. Smilley owns none of them, and pays all of "
      "them.", italic),

    # ---------------- 7. UNDERWORLD ----------------
    P("7. The Underworld and the Law", h1),
    *bullets([
        "<b>The Blackwater Syndicate</b> controls 43 countries and every major U.S. city "
        "(Document 05). To the street it's “the people from the river.” To APD "
        "it's “the ghost network.” To the FBI it's “Organization X.”",
        "<b>The Morrow Organization</b> is Vincent Morrow's Irish-American mob. It was "
        "pushed off Atlanta's ports in 2017 and has been starving for a way back ever "
        "since.",
        "<b>Independent crews</b> pay Blackwater's “tax” or leave town. "
        "Violence in Atlanta's hardest neighborhoods has fallen by half since the 2013 "
        "Peace of Peachtree, and nobody in City Hall can explain why.",
        "<b>The law:</b> APD under Chief Elxa Jackson; the Fulton County DA's office "
        "under interim DA Colette Barnes; the FBI Atlanta field office under Special "
        "Agent in Charge Nadia Brooks; and the Georgia Attorney General, Arianna "
        "Cummings, who knows more than any of them.",
    ]),

    # ---------------- 8. CULTURE ----------------
    P("8. Culture and Society", h1),
    *bullets([
        "<b>Black Atlanta's social calendar</b> runs through Belmont Crest: the Country "
        "Club's New Year's brunch, the Valentine's Ball, the Juneteenth Jubilee, Fourth of "
        "July fireworks, and the Crest Cotillion.",
        "<b>Joan vs. Celeste.</b> The Donohue Foundation Gala and the Smilley Family "
        "Foundation Ball fall on the same night every year, and Atlanta society picks a "
        "side.",
        "<b>HBCUs</b> are richer than ever: Donohue Hall at Spelman, the Alexander "
        "Donohue School of Journalism at Morehouse, and anonymous “Envelope” "
        "scholarships that nobody can trace.",
        "<b>Pop culture</b> belongs to Donohue: the <i>Crown Universe</i> superhero "
        "films, <i>Kingdom of Kora</i> games, Donohue Records' chart-toppers, and "
        "Donohue Worlds theme parks on four continents.",
        "<b>Belmont Crest vs. Tuxedo Park</b> is Atlanta's favorite rivalry. The kids "
        "call it “the Ridge versus the Park.”",
        "<b>The Envelope.</b> Every Friday, envelopes of cash appear in Atlanta's "
        "neighborhoods. Grandmothers light candles for whoever sends them.",
    ]),
    PageBreak(),
]

# ---------------- 9. TIMELINE ----------------
timeline = [
    ("1916", "Alexander Donohue born on Auburn Avenue (Fri, Mar 3)."),
    ("1920", "Simone Batiste born in New Orleans (Sun, Sep 12)."),
    ("1939", "<i>The Atlanta Beacon</i> publishes its first edition (Mon, Apr 3). The "
             "Donohue Company is born."),
    ("1941–1945", "America goes to war. The Beacon's war correspondents make it the "
                       "most trusted Black paper in the South."),
    ("1947", "<i>Crown</i> magazine launches."),
    ("1951", "WDON-AM puts Black voices on Atlanta radio."),
    ("1953", "Donohue Pictures founded; Georgia's first soundstages built."),
    ("1954", "<i>Brown v. Board of Education</i>."),
    ("1958", "Belmont Crest founded (Sat, May 17). Otis Smilley fired from the Beacon."),
    ("1961", "Belmont Crest Country Club and Donohue Records open."),
    ("1960s", "The civil rights movement. The Beacon covers it from inside; Alexander "
              "quietly pays for bail and bus fare. The FBI opens a file on him (1963)."),
    ("1962", "Simone's vote keeps the Smilleys out of Belmont Crest."),
    ("1964", "The Civil Rights Act becomes law."),
    ("1966", "Gus Smilley proposes to Joan Mercer in New York."),
    ("1969", "Victor marries Joan (Sat, Jun 14)."),
    ("1973", "Atlanta elects its first Black mayor. The Beacon's front page sells out "
             "three printings."),
    ("1974", "Smilley Corporation founded in Harlem (Mon, Sep 9)."),
    ("1976", "Victor named CEO over Theodore (Mon, Jan 5)."),
    ("1978", "The Donohue Company lists on the NYSE (Mon, Oct 16)."),
    ("1987", "Donohue swallows Paragon Pictures. Hollywood starts moving to Atlanta."),
    ("1990", "The first Crown License binds Smilley to Donohue."),
    ("1996", "Atlanta hosts the Summer Olympics, broadcast worldwide on DBC. The "
             "Smilleys move to Atlanta. Gus writes the Allegiance Clause."),
    ("2001", "BNN launches."),
    ("2006", "Alexander dies (Mon, Jan 9). Victor becomes Chairman and Natasha becomes "
             "CEO."),
    ("2008", "The financial crisis. Donohue buys distressed studios on three "
             "continents; Donohue Tower opens in Midtown."),
    ("2010", "The Blackwater Syndicate founded in secret (Sat, Sep 18)."),
    ("2011", "BSI founded (Mon, Oct 3). The Lake Lanier Labor Day party (Sat, Sep 3)."),
    ("2012", "Lyric Baker born (Apr 20). Emma and Victoria Smilley born (May 10)."),
    ("2013", "The Peace of Peachtree."),
    ("2014", "Simone Donohue dies at 94 (Sat, Nov 22)."),
    ("2016", "Donohue+ launches worldwide."),
    ("2017", "Blackwater takes Atlanta's ports from the Morrow Organization. RootsKit "
             "launches."),
    ("2019", "The Donohue Company passes $1 trillion."),
    ("2020", "The pandemic. Donohue+ passes 500 million subscribers."),
    ("2021", "Juneteenth becomes a federal holiday. Julian Cummings's hit-and-run "
             "(Sat, Oct 16). Marc gets custody of Lyric (Fri, Feb 12)."),
    ("2023", "Donohue passes $5 trillion. Marc wins his Oscar."),
    ("2024", "Richard Aldridge elected President. Elxa marries Jeremy (Sat, Jun 15)."),
    ("2025", "Aldridge inaugurated (Jan 20). Arianna appointed AG (Mar 17). Elxa sworn in "
             "as Chief (Sep 2). Donohue closes the year at $10 trillion (Dec 31)."),
    ("<b>2026</b>", "<b>Mon, Jan 5: Marc-Anthony's 34th birthday. The Succession "
                    "Covenant. A body in the river. Series premiere.</b>"),
]
story += [P("9. Timeline: The Country and the Crest, 1916–2026", h1),
          table([["Year", "Event"]] + [list(t) for t in timeline],
                [1.0 * inch, 5.5 * inch])]

# ---------------- 10. 2026 CALENDAR ----------------
cal2026 = [
    (D(2026, 1, 5), "Series premiere; Marc-Anthony's 34th birthday", "#0001"),
    (D(2026, 1, 19), "Martin Luther King Jr. Day", "#0011"),
    (D(2026, 2, 8), "The Super Bowl", "#0026 (morning after)"),
    (D(2026, 2, 14), "Belmont Crest Valentine's Ball", "#0031"),
    (D(2026, 3, 6), "Candidate qualifying closes; Haynes files against Arianna", "#0045"),
    (D(2026, 3, 15), "The Academy Awards", "#0051"),
    (D(2026, 4, 5), "Easter", "#0063"),
    (D(2026, 5, 10), "Mother's Day; the twins turn 14", "#0088"),
    (D(2026, 5, 19), "Georgia primary: Jasmine to a runoff; Arianna wins the AG nomination", "#0094"),
    (D(2026, 5, 30), "Victor's 80th birthday gala", "#0101"),
    (D(2026, 6, 7), "The Tony Awards", "#0107"),
    (D(2026, 6, 11), "FIFA World Cup begins", "#0111"),
    (D(2026, 6, 16), "Georgia primary runoff", "#0113"),
    (D(2026, 6, 19), "Juneteenth Jubilee; Harmony's 34th", "#0116"),
    (D(2026, 6, 21), "Father's Day", "#0117"),
    (D(2026, 7, 4), "America's 250th birthday", "#0126"),
    (D(2026, 7, 15), "World Cup semifinal in Atlanta", "#0133"),
    (D(2026, 7, 24), "The Club votes on the Smilleys", "#0140"),
    (D(2026, 8, 6), "First day of 9th grade at Westbrook", "#0149"),
    (D(2026, 8, 31), "The Crown License deadline, 11:59 PM", "#0166"),
    (D(2026, 9, 4), "Labor Day weekend on Lake Lanier; Season 1 finale", "#0170"),
    (D(2026, 11, 3), "Midterm elections", "Season 2"),
]
story += [P("10. The World's 2026 Calendar", h1),
          table([["Date", "Event", "Episode"]] +
                [[long_date(d), e, ep] for d, e, ep in cal2026],
                [2.1 * inch, 3.2 * inch, 1.2 * inch])]

# ---------------- 11. PREMIERE MORNING ----------------
story += [
    PageBreak(),
    P("11. What the World Is Reading: Monday, January 5, 2026, 7:00 AM", h1),
    P("The morning of the premiere, before the body surfaces and before the gala.",
      italic),
    table([
        ["Outlet", "Headline"],
        ["<i>The Atlanta Beacon</i>", "HAPPY 34TH, MARC-ANTHONY: GOLDEN BOY'S BIRTHDAY "
                                      "GALA TONIGHT AT SUMMIT HOUSE"],
        ["<i>Wall &amp; Broad</i>", "DONOHUE ENDS 2025 AT $10 TRILLION; ANALYSTS WATCH "
                                    "FOR SUCCESSION SIGNAL"],
        ["<i>Marquee</i>", "BULLOCK EYES <i>SWEET CHARIOT</i> REVIVAL: “THE TONY IS "
                           "THE LAST ONE”"],
        ["<i>The Capitol Wire</i>", "IS GEORGIA'S AG READY FOR 2028? CUMMINGS WON'T SAY "
                                    "NO"],
        ["<i>The Peach Ledger</i>", "SEVEN YEARS OF SILENCE: WHO FUNDS ATLANTA'S "
                                    "“GHOST NETWORK”?"],
        ["<i>The Tea Kettle ATL</i>", "BLIND ITEM: Which billionaire heiress has turned "
                                      "down every party the birthday boy has ever "
                                      "thrown?"],
    ], [1.8 * inch, 4.7 * inch]),
    Spacer(1, 6),
    P("Trending on Chirp, 7:00 AM", h2),
    *bullets([
        "<b>#HBDMarcAnthony</b> (2.1M posts): “The richest man alive still does his "
        "own stunts AND his own grocery shopping. Protect him at all costs.”",
        "<b>#DonohueTenTrillion</b> (640K posts)",
        "<b>#RidgeVsThePark</b> (88K posts): “Smilleys not invited to the gala "
        "AGAIN. Tuxedo Park in shambles.”",
    ]),
]

# ---------------- 12. POLITICS ----------------
GROUPS = [
    ("The Donohue Family", ["VD", "JD", "AL", "TD", "LC", "XD", "CP", "T3", "SD"]),
    ("The Bullocks", ["RB", "NB", "EL", "MA", "GR"]),
    ("The Olsons", ["JO", "PO", "MO", "ML"]),
    ("The Circle", ["AM", "AR", "HD", "JJ", "JU", "EC", "HC", "GB", "YB", "CD", "LD"]),
    ("The Smilley Family", ["GS", "LO", "LE", "CE", "DE", "NA", "MQ", "CA", "DO", "ES",
                            "DS"]),
    ("Blackwater &amp; BSI", ["EH", "KM", "NS", "DX", "CB", "QM", "IV", "CO", "LF", "CW"]),
    ("Law, Politics &amp; Media", ["WJ", "RD", "FB", "JK", "MP", "CH", "JH", "BK"]),
    ("Everyone Else", ["LG", "WO", "MF", "PW", "PR", "AB", "EV", "SC", "NV", "ZR", "CL",
                       "VM", "RT"]),
]
rows = [["Character", "Party"]]
for title, codes in GROUPS:
    rows.append([f"<b>{title}</b>", ""])
    rows += [[CAST[c][0], PARTY[c]] for c in codes]
story += [
    PageBreak(),
    P("12. Politics: Everyone's Party", h1),
    P("Registration as of Monday, January 5, 2026. The families are split down the middle, "
      "and so is Thanksgiving dinner. The kids (Emma, Victoria, Lyric, Trey, Jaden, and "
      "August) are too young to vote.", italic),
    table(rows, [3.3 * inch, 3.2 * inch]),
    Spacer(1, 6),
    P("Where the splits hurt", h2),
    *bullets([
        "<b>Summit House:</b> Victor is a lifelong business Republican; Joan is a lifelong "
        "Democrat. They've canceled out each other's vote in every election since 1969.",
        "<b>The Olsons:</b> Congresswoman Jasmine is a Democrat. Her husband Peter and "
        "her son Martin are Republicans who quietly write checks to her opponents' party.",
        "<b>The Jacksons:</b> the Chief is an Independent; her by-the-book husband is a "
        "Republican.",
        "<b>The Circle:</b> Amond (Republican) and Harmony (Democrat) fight about "
        "politics the way they fight about everything else.",
        "<b>The Smilleys</b> are a Republican house, except Loretta, Delphine, and "
        "Desmond. Leonard still funds Democrat Marcus Pryor's primary challenge to Jasmine, "
        "because hurting a Donohue beats party loyalty.",
    ]),

    P("13. Marc-Anthony's Secret Campaign", h1),
    P("Marc-Anthony Bullock is a Democrat with Republican values who believes in "
      "bipartisanship. He SECRETLY wants to run for President of the United States in "
      "2028. No one knows: not Amond, not Grace, not his parents, and not Arianna.",
      answer),
    table([
        ["Eligibility check", ""],
        ["Constitutional minimum age", "35"],
        ["Marc's age on Election Day, Tue, Nov 7, 2028",
         str(age_on(D(1992, 1, 5), D(2028, 11, 7)))],
        ["Marc's age on Inauguration Day, Sat, Jan 20, 2029",
         str(age_on(D(1992, 1, 5), D(2029, 1, 20))) + " (eligible)"],
    ], [4.0 * inch, 2.5 * inch]),
    P("What he believes in, and will 100% accomplish, zero questions asked", h2),
    *bullets(MARC_PLATFORM),
    P(f"<b>Long-term goal:</b> {MARC_LONG_TERM}"),
    P("More of his platform will be revealed as the story unfolds.", italic),
    P("The 2028 field (as of January 2026)", h2),
    table([
        ["Name", "Party", "Status"],
        ["Karen Molina", "Republican", "Sitting Vice President and the front-runner"],
        ["Arianna Cummings", "Democrat", "Publicly weighing a run; exploratory committee "
                                         "planned after the midterms (launched early, "
                                         "Ep #0129)"],
        ["Marc-Anthony Bullock", "Democrat (with Republican values)",
         "SECRET. Hasn't told a soul"],
    ], [1.6 * inch, 1.9 * inch, 3.0 * inch]),
    P("The collision course", h2),
    *bullets([
        "Marc and Arianna, best friends since childhood, are headed for the same "
        "Democratic primary, and neither knows it yet.",
        "Arianna's buried secrets are buried by Marc. His biggest secret, Blackwater, is "
        "the one thing that could end any campaign.",
        "Martin, a Republican, would do anything to stop his cousin from reaching the "
        "White House.",
    ]),
]

build(OUT, story, "Beyond the Crest — World Building",
      "BEYOND THE CREST — World Building — Writers' Room Confidential")
