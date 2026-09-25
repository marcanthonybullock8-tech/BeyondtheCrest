"""Builds docs/08_Season_1_Storylines.pdf"""
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer, KeepTogether

from btc_pdf import P, h1, h2, body, italic, answer, bullets, table, build, cover

OUT = "docs/08_Season_1_Storylines.pdf"

story = cover("Season 1 Storylines — Document 08", [
    "<b>170 episodes</b> • Monday, January 5 – Friday, September 4, 2026",
    "<b>Tagline:</b> <i>Every crown has a price. Every secret has an heir.</i>",
])
story.append(PageBreak())

story += [
    P("The Shape of Season 1", h1),
    P("Season 1 runs from Marc-Anthony's 34th birthday to Labor Day weekend on Lake "
      "Lanier, exactly fifteen years after the night he doesn't remember. The spine is "
      "one ticking clock, the Crown License deadline of 11:59 PM on August 31, and one "
      "secret: Marc-Anthony has two daughters he's never been told about.", answer),
    table([
        ["Movement", "Episodes", "Air dates", "What happens"],
        ["I. The Covenant", "#0001–#0030", "Jan 5 – Feb 13",
         "The birthday, the body in the river, the Crown License, the auditions, the "
         "elevator"],
        ["II. Roots", "#0031–#0062", "Feb 16 – Apr 2",
         "Valentine's slap, Broadway, the Oscars, the DNA results, the Spare Alliance"],
        ["III. Blood Tests", "#0063–#0101", "Apr 6 – May 29",
         "Huntington's, Alvin's return, Mother's Day, the primary, Victor's 80th"],
        ["IV. The EGOT Summer", "#0102–#0135", "Jun 1 – Jul 17",
         "Victor's surgery, the Tonys, Juneteenth, the kiss, the World Cup"],
        ["V. Verdicts", "#0136–#0165", "Jul 20 – Aug 28",
         "The Club vote, the trial verdict, the Kettle unmasked, the Allegiance Clause"],
        ["VI. Labor Day", "#0166–#0170", "Aug 31 – Sep 4",
         "The deal, Theodore's arrival, the finale on Lake Lanier"],
    ], [1.4 * inch, 1.0 * inch, 1.2 * inch, 2.9 * inch]),
    Spacer(1, 6),
    P("Tentpoles and event episodes (the 10%)", h2),
    P("#0001 Birthday Gala • #0011 “1958” flashback • #0031 Valentine's "
      "Ball • #0051 The Oscars • #0057 Broadway Opening Night • #0063 Easter "
      "• #0088 Mother's Day / Twins' 14th • #0096 8th-Grade Promotion • "
      "#0100 Milestone • #0101 Victor's 80th • #0106 HEIRLOOM Launch • #0107 "
      "The Tonys • #0116 Juneteenth Jubilee • #0126 Fourth of July • #0133 "
      "World Cup Semifinal • #0139 “1966” flashback • #0170 Finale. "
      "That's 17 of 170, exactly 10%."),
    PageBreak(),
]

ARCS = [
    ("1. The Crown License",
     "Marc-Anthony vs. Esther Smilley: the negotiation that decides whether Smilley "
     "Corporation survives.",
     "Marc, Esther, Natasha, Leonard, Gus, Camille, Dorian",
     ["Leonard reveals that 41% of Smilley revenue hangs on a deal expiring Aug 31, and "
      "Esther is named lead negotiator (#0003).",
      "Esther dodges Marc for six weeks, including the anonymous elevator (#0017), before "
      "they finally face off (#0030).",
      "The talks collapse (#0083), come back over late-night waffles (#0099), and turn "
      "personal (#0138).",
      "Marc offers a deal too generous to be business (#0160). They sign at 11:59 PM on "
      "Aug 31 (#0166)."],
     "It's the first daytime love story whose love scenes are term sheets. Every "
     "romantic beat is also a corporate move worth billions.",
     "Signed, and both families furious that it was fair."),
    ("2. Roots",
     "Three 13-year-olds use a school heritage project and a Smilley DNA kit to "
     "discover that their “donor” father is the movie star they idolize.",
     "Emma, Victoria, Lyric, Esther, Marc, Nathaniel, Trey",
     ["Westbrook's Black History Month Roots Project assigns RootsKit tests (#0021).",
      "The results match the twins to Grace Bullock: aunt or half-sibling (#0053).",
      "“Operation Daddy”: Lyric steals a hair (#0055), the twins mail it in "
      "(#0062), and the result is a 99.98% parent/child match (#0075).",
      "The anonymous Father's Day card (#0117). The twins watch Marc and Esther kiss "
      "(#0126).",
      "They tell him themselves in the finale (#0170)."],
     "The children solve the paternity mystery before any adult does, using a product "
     "made by their own mother's company. They run the investigation, they choose the "
     "reveal, and they deliver it.",
     "Marc knows. Esther's secret is over."),
    ("3. The Spare Alliance",
     "The eldest grandson of each dynasty, both passed over for a younger heir, team up "
     "to destroy their golden cousins.",
     "Martin, Nathaniel, Camille, Dorian, Brielle",
     ["Nathaniel and Camille bond over losing to Esther (#0022).",
      "Nathaniel sees the RootsKit flag (#0056) and takes it to Martin (#0058).",
      "Martin's investigator proves the IVF story is fake (#0092, #0120).",
      "Martin hacks the Kettle account to post the blind item (#0152). Nathaniel takes "
      "it to the Smilley Family Council (#0163)."],
     "A cross-dynasty villain team whose motive is the same wound twice: being born "
     "first and chosen second.",
     "Nova traces the hack to Martin (#0156). Marc now knows who his enemy is."),
    ("4. Who Killed T-Bone Gaines?",
     "A murder in the Chattahoochee pits husband against wife, father against daughter, "
     "and cousin against cousin.",
     "Jeremy, Elxa, Robert, Deuce, Martin, Marc, Kane, Rosa",
     ["The body surfaces (#0001) with “ARCHITECT” in the burner (#0002).",
      "Jeremy arrests Deuce, and Robert takes the case (#0015).",
      "The audience learns Martin did it (#0060). Peter stitched his knuckles (#0003, "
      "#0064).",
      "The trial (#0128–#0145). T-Bone's girlfriend swears the Architect is innocent "
      "(#0135). NOT GUILTY (#0145)."],
     "A murder mystery where the audience knows the killer halfway through, and the "
     "suspense is which family member will find out, and what they'll do.",
     "Deuce is free. The killer is untouched. Robert now knows who pays his bills."),
    ("5. The Succession Covenant",
     "Victor names Marc heir apparent and promises to name his next Chairman on his 80th "
     "birthday.",
     "Victor, Joan, Natasha, Jasmine, Martin, Marc, Alvin",
     ["The Covenant (#0001). Jasmine storms Victor's study (#0002).",
      "Victor gives Marc the key to the 1939 press (#0009).",
      "The 80th birthday gala: “My successor as Chairman will be—” and "
      "Victor collapses (#0101).",
      "Surgery (#0102). Alvin and Jasmine move on the Crown Voting Trust while Victor is "
      "down (#0104)."],
     "The whole season's power struggle hangs on one unfinished sentence.",
     "Still unspoken. Theodore arrives to claim that the 1976 succession was never "
     "valid."),
    ("6. The EGOT Year",
     "Mother and son chase the last awards they're missing in the same season.",
     "Natasha, Marc, Victor, Joan, Grace, Nia, Sebastian",
     ["Martin smears Natasha's director on Oscar eve (#0050). Natasha wins Best Actress "
      "and completes her EGOT (#0051), and Marc crashes out on a reporter.",
      "Marc stars in the <i>Sweet Chariot</i> revival, the role Victor originated in "
      "1972 (#0034, #0041, #0057).",
      "Eleven Tony nominations (#0084). Marc wins and completes his EGOT at 34 (#0107), "
      "dedicating it “to the family I'm going to have” (#0108)."],
     "Nobody is nerfed: in one season, the family goes from two EGOTs to four.",
     "Four EGOTs under one roof: Victor, Joan, Natasha, and Marc."),
    ("7. The Chief and the Boy Scout",
     "The Chief of Police protects the man she thinks is guilty, her father, while her "
     "by-the-book husband hides a genetic secret.",
     "Elxa, Jeremy, Walter, Robert, Rosa, Nadia Brooks",
     ["Elxa suspects Robert is the Architect (#0059) and destroys a ledger page to "
      "protect him (#0090–#0091).",
      "Jeremy's truth: his mother died of Huntington's and he has a 50% chance (#0072).",
      "The FBI task force (#0067). The empty warehouse raid (#0109). The marriage "
      "fractures (#0124) and they separate (#0148).",
      "Jeremy finally takes the test (#0155). Elxa sees Marc with Kane and understands "
      "(#0170)."],
     "A daytime heroine who is the city's top cop, protecting the wrong suspect for the "
     "right reason, while the truth is her baby brother.",
     "The results envelope sits unopened. Elxa knows it's Marc."),
    ("8. Madam President?",
     "The Attorney General's 2028 dream versus the reporter whose father her brother "
     "killed.",
     "Arianna, Julian, Journee, Marc, Harold &amp; Evelyn Cummings",
     ["Arianna announces her plans (#0005). Journee starts digging (#0014).",
      "Journee meets Julian at a grief group (#0028). They fall in love (#0045, #0129).",
      "Arianna asks Marc to make Journee go away, and he refuses (#0078).",
      "Arianna learns Marc still has the car (#0144). Journee finds Julian's name "
      "(#0162), and Julian confesses (#0169)."],
     "A love story between a grieving daughter and the man who killed her father, played "
     "entirely in daylight.",
     "Journee knows. Arianna's campaign, and her secret, are on a fuse."),
    ("9. The Tea Kettle",
     "The broke filmmaker nobody takes seriously is secretly the most-read gossip blogger "
     "in Atlanta.",
     "Harmony, Esther, Amond, Nathaniel, Martin",
     ["The audience learns Harmony is Kettle in the final beat of #0001.",
      "Her posts drive the plot: the slap (#0032), the garden photos (#0089), Pryor's "
      "affair (#0112).",
      "Nathaniel funds her film to use her (#0071, #0142).",
      "Martin hacks her account to post the twins blind item (#0152). Esther unmasks her "
      "and a 23-year friendship ends (#0153)."],
     "The narrator of the show's own gossip is a character inside it, and the in-universe "
     "social media is a weapon.",
     "Harmony has lost her best friend, and she knows about the twins."),
    ("10. HEIRLOOM",
     "Grace and Mallory's beauty brand goes to war with Smilley Beauty, and Mallory falls "
     "for the enemy's grandson.",
     "Grace, Mallory, Desmond, Camille, Delphine",
     ["HEIRLOOM is announced (#0006). Mallory meets Desmond (#0019) and learns he's a "
      "Smilley (#0029).",
      "Camille frames Desmond (#0069). The copycat launch on Mallory's birthday (#0106).",
      "Desmond clears his name and quits (#0114). Mallory decides to wait for her "
      "wedding night (#0159)."],
     "A romance where the 31-year-old virgin heiress is in full control of her story, "
     "set against real corporate espionage.",
     "HEIRLOOM survives, and Mallory and Desmond are official."),
    ("11. The Primary",
     "Jasmine faces her first real challenge in 29 years, secretly bankrolled by the "
     "Smilleys.",
     "Jasmine, Peter, Pryor, Leonard, Alvin, Morrow",
     ["Pryor announces (#0012). The money traces back to Leonard (#0023, #0040).",
      "Alvin buys Pryor's secrets from Morrow (#0093). The primary goes to a runoff "
      "(#0094).",
      "Kettle breaks the affair story (#0112). Jasmine wins the runoff (#0113), and now "
      "owes Morrow."],
     "A congresswoman who wins by accepting a debt to the mob her nephew is at war with.",
     "Jasmine wins, but she owes Morrow."),
    ("12. The Vote",
     "Sixty-four years after Simone Donohue rejected his father, Gus Smilley applies to "
     "the Club.",
     "Gus, Loretta, Joan, Victor, Lucinda",
     ["Joan finds Gus's 1966 letter (#0039) and confronts him (#0079). The application "
      "(#0080).",
      "Joan confesses the romance (#0122), and Victor summons Gus (#0123).",
      "The “1966” flashback (#0139). The vote ties, and Joan breaks it: yes "
      "(#0140).",
      "Victor forgives her. “There's one more thing. About 1976” (#0158)."],
     "A love triangle between people in their late seventies and eighties, told with the "
     "same heat as the young leads.",
     "The Smilleys are inside the gates. Joan has one more secret."),
    ("13. The Wild Card Returns",
     "Alvin comes home at the halfway point, and brings the underworld with him.",
     "Alvin, Zion, Coco, Morrow, Marc, Jasmine",
     ["The helicopter on the lawn (#0085). The karaoke-bar meeting with Morrow (#0086).",
      "Zion Reed: “I think you're my father” (#0095). DNA confirmed (#0110).",
      "Alvin steals the World Cup security plan (#0130). Marc sets a trap (#0131). "
      "Blackwater stops the attack (#0133)."],
     "The family's party boy is the mob's inside man, and his nephew is the mob he's "
     "betraying.",
     "Alvin has a son, a debt, and a very bad feeling."),
    ("14. The Architect's Father",
     "Robert Bullock realizes his son runs the Syndicate he's been defending.",
     "Robert, Marc, Natasha, Kane, Cyrus",
     ["Robert takes Deuce's case (#0015) and asks Marc for BSI footage (#0098).",
      "The verdict, and Kane in the gallery (#0145). Robert follows the money (#0146).",
      "“Then act surprised when I tell you I'm proud of you” (#0147)."],
     "The father-son scene of the year is a confession with no confession in it.",
     "Robert knows and is protecting him."),
    ("15. The Old Man",
     "Martin's mysterious backer is revealed in the final week: Theodore Donohue, "
     "coming home.",
     "Theodore, Lorraine, Xander, Celestine, Theo III, Sienna, August, Martin, Victor",
     ["“THE OLD MAN SAYS: PATIENCE” (#0025).",
      "Theodore arrives (#0167) and his family follows (#0168).",
      "At Summit House: “Hello, little brother” (#0170)."],
     "The season-long off-screen villain turns out to be family, and joins the cast "
     "the moment the audience learns who he is.",
     "Season 2 belongs to him."),
]
for title, logline, players, beats, fresh, status in ARCS:
    story.append(KeepTogether([P(title, h2), P(f"<i>{logline}</i>"),
                               P(f"<b>Players:</b> {players}")]))
    story += bullets(beats)
    story += [P(f"<b>Why it's never been done in daytime:</b> {fresh}"),
              P(f"<b>Status at the finale:</b> {status}"),
              Spacer(1, 6)]

story += [
    PageBreak(),
    P("The Finale: Episode #0170, Friday, September 4, 2026", h1),
    P("Labor Day weekend on Lake Lanier, fifteen years to the weekend after Marc and "
      "Esther's night. Everything collides:"),
    *bullets([
        "The twins walk Marc to the end of the dock: “Happy Labor Day, Dad.”",
        "Marc turns to Esther: “Fourteen years.” The sweetest man in the world "
        "goes still.",
        "Elxa sees Kane hand Marc a black river stone, and every case she ever worked "
        "rearranges itself.",
        "At Summit House, Theodore sets down his cane: “Hello, little brother.”",
        "Jeremy's Huntington's results sit unopened on the dashboard of his car.",
        "A gunshot echoes across the lake. Smash cut to black.",
    ]),
    P("In-universe headlines, Saturday, September 5, 2026", h2),
    *bullets([
        "<b>The Atlanta Beacon:</b> “SHOTS FIRED AT LANIER ESTATE DURING DONOHUE "
        "HOLIDAY PARTY”",
        "<b>The Peach Ledger:</b> “SOURCES: SMILLEY HEIR'S IVF TWINS ARE A "
        "DONOHUE MATTER”",
        "<b>Hollywood Heat:</b> “EGOT GOLDEN BOY'S LABOR DAY FROM HELL”",
        "<b>Social media:</b> #LanierShooting trends No. 1 worldwide by 1:00 AM.",
    ]),
]

build(OUT, story, "Beyond the Crest — Season 1 Storylines",
      "BEYOND THE CREST — Season 1 Storylines — Writers' Room Confidential")
