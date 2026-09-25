"""Builds docs/04_Belmont_Crest.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer

from btc_pdf import P, h1, h2, answer, bullets, table, long_date, build, cover

OUT = "docs/04_Belmont_Crest.pdf"
D = dt.date

story = cover("Belmont Crest — Document 04", [
    "<b>Founded:</b> " + long_date(D(1958, 5, 17)) + " by Alexander &amp; Simone Donohue",
    "<b>Main Gate:</b> 1958 Belmont Crest Parkway NW, Atlanta, Georgia 30327",
    "<b>Home of:</b> The Belmont Crest Country Club (est. 1961)",
])
story.append(PageBreak())

story += [
    P("Where It Is", h1),
    P("LOCATION: Belmont Crest is a private, gated community of 1,240 wooded acres on a "
      "ridge above the Chattahoochee River at Atlanta's northwestern edge. It sits inside "
      "the city limits in Fulton County, ZIP 30327, west of West Paces Ferry Road, with "
      "Buckhead's Tuxedo Park just to the east.", answer),
    table([
        ["Landmark", "Address"],
        ["Main Gate &amp; Gatehouse", "1958 Belmont Crest Parkway NW, Atlanta, GA 30327"],
        ["River Gate (service &amp; security)", "40 Riverbend Crest NW, Atlanta, GA 30327"],
        ["Summit House (Victor &amp; Joan)", "1 Summit Crest Drive NW, Atlanta, GA 30327"],
        ["Belmont Crest Country Club", "1961 Fairway Crest NW, Atlanta, GA 30327"],
        ["Marc-Anthony Bullock's estate", "7 Covenant Way NW, Atlanta, GA 30327"],
        ["The Bullock estate (Robert &amp; Natasha)", "22 Covenant Way NW, Atlanta, GA 30327"],
        ["The Cummings estate", "28 Covenant Way NW (three houses down from the Bullocks)"],
        ["The Olson estate", "41 Simone Circle NW, Atlanta, GA 30327"],
        ["The Baker home", "318 Magnolia Ridge NW, Atlanta, GA 30327"],
        ["The Belmont Academy (K–12)", "500 Academy Crest NW, Atlanta, GA 30327"],
        ["Chapel of the Crest", "12 Simone Circle NW, Atlanta, GA 30327"],
    ], [2.6 * inch, 3.9 * inch]),
    Spacer(1, 6),
    table([
        ["Distance / neighbor", "Detail"],
        ["Downtown Atlanta", "About 8 miles southeast (20 minutes without traffic, 50 with it)"],
        ["Donohue Tower (Midtown)", "About 6.5 miles"],
        ["Tuxedo Park, Buckhead (the Smilleys)", "Just across the ridge. The families can see "
                                                "each other's lights at night"],
        ["Westbrook Academy (Buckhead)", "About 3 miles"],
        ["Chattahoochee River", "Belmont Crest's western border. The body of T-Bone Gaines "
                                "surfaces downstream near the Paces Ferry Road bridge in Ep "
                                "#0001"],
        ["Hartsfield-Jackson Airport", "About 17 miles south"],
    ], [2.4 * inch, 4.1 * inch]),

    P("Belmont Crest Today (January 2026)", h1),
    *bullets([
        "<b>212 estates</b> on lots of 2 to 60 acres, about 1,100 residents. Homes rarely "
        "sell. When one does, the price starts around $40 million.",
        "<b>The most exclusive address in the South.</b> Residents include the Donohues, "
        "the Bullocks, the Olsons, the Cummingses, the Bakers, two NBA owners, three "
        "Grammy-winning producers, a Supreme Court of Georgia justice, and the owners of "
        "the South's largest Black-owned bank and construction firm.",
        "<b>Security</b> is run by Blackwater Security International: 140 officers, "
        "license-plate readers at both gates, and river patrols.",
        "<b>The Crest Covenant</b> governs everything. Every buyer must be approved by the "
        "Belmont Crest Association board of nine. The Donohue family holds two permanent "
        "seats, the “Founder's Seats,” and a veto over any sale within sight of "
        "Summit House.",
        "<b>Summit House</b> stands at the highest point of the ridge: 42,000 square feet "
        "of Georgian Revival, finished in 1960 and designed by the Black architect "
        "Eldridge Toussaint, with the famous grand staircase. Everything else in the "
        "community lies <i>beyond the crest</i>.",
    ]),
    PageBreak(),
    P("History of Belmont Crest", h1),
]

eras = [
    ("1956–1958: The Ridge", [
        "1956: Simone Donohue spots the ridge from a riverboat outing on the "
        "Chattahoochee. “That's where our grandchildren will live.” No Black "
        "family could buy land there.",
        "1957: Alexander forms the Crest Land Trust. A sympathetic white Atlanta attorney, "
        "Harlan Whitfield, buys 1,240 acres in eleven parcels as its front.",
        long_date(D(1958, 5, 17)) + ": the fourth anniversary of <i>Brown v. Board of "
        "Education</i>, a date Simone chose. The trust transfers the deed to Alexander "
        "and Simone Donohue, and the first stone gate goes up at dawn. Belmont Crest is "
        "founded. Theodore is 13, and Victor is 11.",
        "Summer 1958: Otis Smilley, the Beacon's press foreman, is fired after Alexander "
        "accuses him of selling the paper's printing plates. Otis swears he was framed. "
        "His 15-year-old son Gus never forgets.",
    ]),
    ("1958–1964: The Siege", [
        "1958–1959: White neighbors sue to void the sale. The Donohues win, because "
        "racial covenants had been unenforceable in court since 1948.",
        long_date(D(1959, 11, 21)) + ": A cross is burned at the gate. Alexander rebuilds "
        "it twice as high with a Beacon headline carved into the lintel: <i>“THE "
        "CREST WILL NOT BE MOVED.”</i>",
        "1960: Summit House is completed and the first twelve families move in: doctors, "
        "ministers, a bank president, a Morehouse dean, and two Donohue Records stars.",
        "1962: <b>Otis Smilley</b>, now running his own print shop, applies to buy a lot. "
        "The Association board deadlocks, and Simone casts the deciding vote: no. She "
        "never explains why. It is the founding wound of the Smilley–Donohue feud.",
    ]),
    ("1965–1999: The Golden Age", [
        "1965–1975: Belmont Crest becomes the quiet capital of Black Atlanta. Movement "
        "leaders strategize over dinner at the Club, and presidential candidates learn "
        "that the road to Georgia runs through Summit House.",
        "1969: Victor and Joan's wedding reception at the Club: 1,400 guests.",
        "1974: The Belmont Academy opens. Jasmine Donohue is in its first kindergarten "
        "class.",
        "1988: The community reaches its limit of 212 estates. The Association closes "
        "the ridge to further subdivision, forever.",
        "1996: The Smilleys move to Atlanta and buy in Tuxedo Park, across the ridge "
        "(see Document 06).",
    ]),
    ("2000–2026: The Third Generation", [
        "2006: Alexander dies and lies in repose at the Chapel of the Crest while 30,000 "
        "people file through the gates.",
        long_date(D(2014, 11, 22)) + ": Simone dies at 104, with the reason for her 1962 "
        "vote still sealed in her diary.",
        "2012: BSI takes over Belmont Crest security.",
        long_date(D(2026, 1, 5)) + ": Marc-Anthony's 34th birthday gala at Summit House. "
        "Series premiere.",
        long_date(D(2026, 7, 24)) + " (Ep #0140): The Club votes on the Smilley "
        "application, 64 years after Otis was turned away.",
    ]),
]
for era, items in eras:
    story.append(P(era, h2))
    story += bullets(items)

story += [
    PageBreak(),
    P("The Belmont Crest Country Club", h1),
    P("Founded " + long_date(D(1961, 6, 17)) + " at 1961 Fairway Crest NW. Alexander built "
      "it because Black golfers were still unwelcome at Atlanta's private clubs. It is "
      "now among the most exclusive clubs in America."),
    table([
        ["Feature", "Detail"],
        ["Membership", "600 families, by invitation only. Initiation fee $1.5 million. Annual "
                       "dues $120,000"],
        ["The Summit Course", "18-hole championship course along the river bluff. Its 18th "
                              "green overlooks the Chattahoochee"],
        ["The Simone Course", "9-hole short course and practice academy"],
        ["The Clubhouse", "38,000-sq-ft Georgian clubhouse with the Alexander Ballroom, the "
                          "Peacock Lounge, and the Terrace"],
        ["Also", "Tennis and pickleball center, equestrian stables and trails, spa, "
                 "marina on the river, and a private dining room called “The Vault”"],
        ["Membership Committee Chair", "Lucinda Graves, the gatekeeper of the gate"],
        ["Head Bartender", "Malik Freeman, who hears everything"],
    ], [1.9 * inch, 4.6 * inch]),
    P("Annual Traditions", h2),
    table([
        ["Event", "When (2026)", "Episode"],
        ["New Year's Day Brunch", "Thu, Jan 1", "Before the premiere"],
        ["Valentine's Ball", "Sat, Feb 14", "#0031"],
        ["Easter Sunrise Service &amp; Egg Hunt (at Summit House)", "Sun, Apr 5", "#0063"],
        ["Juneteenth Jubilee", "Fri, Jun 19", "#0116"],
        ["Fourth of July Fireworks on the 18th fairway", "Sat, Jul 4", "#0126"],
        ["The Smilley membership vote", "Fri, Jul 24", "#0140"],
        ["The Crest Classic golf tournament (Labor Day)", "Mon, Sep 7", "Season 2"],
        ["The Crest Cotillion (debutantes)", "December", "Season 2"],
    ], [3.3 * inch, 1.3 * inch, 1.9 * inch]),
    P("Club Rules That Become Story", h2),
    *bullets([
        "A new member needs two sponsors and a majority of the Membership Committee. The "
        "Founder's Seat holder, Joan Donohue, votes only to break a tie, which can happen "
        "when a member recuses.",
        "Any member can call for a “Revocation Hearing” against another member "
        "for conduct unbecoming.",
        "What's said in The Vault stays in The Vault. Malik Freeman has never broken that "
        "rule. Yet.",
    ]),
]

build(OUT, story, "Beyond the Crest — Belmont Crest",
      "BEYOND THE CREST — Belmont Crest — Writers' Room Confidential")
