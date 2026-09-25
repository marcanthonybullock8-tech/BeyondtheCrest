"""Builds docs/10_Supporting_Characters.pdf"""
from collections import Counter

from reportlab.platypus import PageBreak, KeepTogether, Spacer

from btc_pdf import P, h1, h2, italic, bullets, scene, age_on, long_date, build, cover
from cast import CAST
from season1_episodes import EPISODES, full_cast

OUT = "docs/10_Supporting_Characters.pdf"

counts, first = Counter(), {}
for n in range(1, len(EPISODES) + 1):
    for c in full_cast(n):
        counts[c] += 1
        first.setdefault(c, n)

# (section, intro, [(code, who, [backstory], (speaker, (paren, line)))])
SECTIONS = [
    ("The Blackwater Syndicate &amp; BSI",
     "Full organization history in Document 05.",
     [
         ("EH", "The Consigliere. Zeke is soft-spoken, silver-bearded, and the most "
          "dangerous lawyer in America. He's the only man alive who calls Marc-Anthony "
          "“son” and gets away with it.",
          ["Retired Army intelligence colonel and former federal prosecutor.",
           "Coached Marc's mock-trial team at the Belmont Academy. Became consigliere in "
           "2011 and BSI General Counsel the same year.",
           "Widowed. Plays chess against himself every night at 11:00 PM."],
          ("ZEKE", ("", "The law is a tool, son. So is a hammer. Neither one cares who's "
                        "holding it."))),
         ("KM", "The Enforcer. Kane is 6'5\", silent, and loyal past the point of "
          "reason. He's Marc's shadow in public and his sword in private, and he's "
          "hopelessly in love with Grace Bullock.",
          ["Grew up in Bankhead. Founding member of Blackwater with Marc and Amond on "
           "September 18, 2010.",
           "Heads Marc's personal security under BSI Executive Protection.",
           "He and Grace keep agreeing “nothing happened” (Eps #0044, #0125)."],
          ("KANE", ("", "I don't talk much. I don't need to."))),
         ("NS", "The Intelligence Chief. Nova is a hacker genius with purple braids and "
          "zero patience for anyone slower than her, which is everyone except Marc.",
          ["At 16 she broke into BSI's servers for fun. Marc hired her instead of "
           "reporting her (2012).",
           "Publicly BSI's CTO; privately she sees everything Blackwater needs to see.",
           "Traces the Kettle hack to Martin (Ep #0156)."],
          ("NOVA", ("", "Nothing's deleted. It's just waiting for me."))),
         ("DX", "The Atlanta Captain. Deuce owns the hottest nightclub on the Westside "
          "and runs Blackwater's home turf. He's charged with a murder he didn't commit.",
          ["Swore to Blackwater at the 2013 “Peace of Peachtree.”",
           "Arrested for T-Bone Gaines's murder (Ep #0015). Robert Bullock defends him.",
           "Found NOT GUILTY (Ep #0145)."],
          ("DEUCE", ("", "I've done a lot of things. Not that one."))),
         ("CB", "The Banker. Cyrus moves Blackwater's money across five continents and "
          "never raises his voice or his heart rate.",
          ["Former Wall Street private banker who got tired of laundering money for "
           "worse men.", "Robert follows his trail straight to Marc (Ep #0146)."],
          ("CYRUS", ("", "Money doesn't have a conscience. That's why they hired "
                         "me."))),
         ("QM", "The West Coast Captain. Queenie finances half of Hollywood's indie "
          "films and runs Blackwater from Malibu to Seattle.",
          ["Former stunt driver. Joined the Table in 2015."],
          ("QUEENIE", ("", "Hollywood runs on dreams. I run on collateral."))),
         ("IV", "The East Coast Captain. Idris is a New York real estate developer who "
          "owns the building across from every Broadway theater Marc has ever "
          "played.",
          ["Joined the Table in 2015. Watches over Marc during the <i>Sweet Chariot</i> "
           "run."],
          ("IDRIS", ("", "New York doesn't sleep. Neither do I."))),
         ("CO", "The Africa Captain. Chidi is a Lagos shipping magnate who controls "
          "West Africa's ports for Blackwater.",
          ["Joined the Table in 2020. Attends Table meetings by secure video."],
          ("CHIDI", ("", "Every ship that docks in Lagos says good morning to me."))),
         ("LF", "The Europe Captain. Lorenzo is a Milanese hotelier and the Table's "
          "only non-Black member, fiercely loyal to the Architect.",
          ["Joined the Table in 2020 after Marc saved his family's hotels from a rival "
           "syndicate."],
          ("LORENZO", ("", "In Milan we have a word for men like the Architect. We "
                           "don't say it out loud."))),
         ("CW", "The Clean Face. General Whitmore is BSI's CEO, a decorated four-star "
          "officer who believes BSI is exactly what it says it is.",
          ["Retired from the Army in 2016 and joined BSI in 2017.",
           "Has no knowledge of the Syndicate. Stonewalls Jeremy's subpoena on "
           "principle (Ep #0036)."],
          ("GENERAL WHITMORE", ("", "This company protects presidents, Detective. "
                                    "Get a warrant."))),
         ("TB", "The Traitor. T-Bone was an Atlanta lieutenant who started selling "
          "Blackwater's secrets in 2024. He's seen alive only in flashback.",
          ["Sold his intel to Martin Olson.",
           "Killed by Martin under the Paces Ferry Road bridge at 11:40 PM on Sunday, "
           "January 4, 2026, age 41 (Ep #0060)."],
          ("T-BONE", ("", "The Architect lives on the ridge. That's worth more than "
                          "you're paying."))),
     ]),
    ("Law Enforcement &amp; the Courts", None, [
        ("WJ", "The Legend. Walter is Jeremy's father and Atlanta's Chief of Police from "
         "2011 to 2019. He's beloved, gruff, and quietly heartbroken.",
         ["His wife Diane died of Huntington's disease in 2018.",
          "Wants grandchildren badly, and pushes Jeremy to get tested (Ep #0074)."],
         ("WALTER", ("", "I buried your mother. I'm not burying the idea of "
                         "grandbabies with her."))),
        ("RD", "The Partner. Rosa is Jeremy's partner in Homicide: sharp, funny, and "
         "Puerto Rican from the Bronx. She's the only person who can tell Jeremy he's "
         "wrong.",
         ["Transferred from NYPD to APD in 2019.",
          "Starts to suspect the Chief is protecting someone."],
         ("ROSA", ("", "By the book is great, Jackson. Somebody just ripped out a "
                       "chapter."))),
        ("FB", "The Fed. Nadia runs the FBI's Atlanta field office and has spent seven "
         "years hunting “Organization X.”",
         ["Opens a joint task force with Jeremy (Ep #0067). Raids the empty BSI warehouse "
          "(Ep #0109)."],
         ("NADIA", ("", "Nobody's this clean, Detective. Nobody."))),
        ("JK", "The Judge. Judge Okoye presides over the Whitaker trial. She's "
         "incorruptible, which makes her a problem for everyone.",
         ["Nigerian-American, Emory Law. On the bench since 2008.",
          "Denies Deuce bail (Ep #0026). Presides over the trial and the verdict "
          "(Ep #0145)."],
         ("JUDGE OKOYE", ("", "Mr. Bullock, this is a courtroom, not a Broadway stage. "
                              "Your son has that covered."))),
    ]),
    ("Politics &amp; Media", None, [
        ("JH", "The Reporter. Journee is an investigative reporter at <i>The Peach "
         "Ledger</i>, an independent Atlanta outlet. She's relentless, warm, and "
         "grieving.",
         ["Her father, Raymond Holloway, was killed in a hit-and-run on Saturday, "
          "October 16, 2021. The DA's office closed the case in eleven days.",
          "An anonymous scholarship paid off her student loans in 2022. She never knew it "
          "came from Blackwater.",
          "Falls in love with Julian Cummings, the man who killed her father "
          "(Eps #0045–#0169)."],
         ("JOURNEE", ("", "Somebody in this city knows who killed my father. I'm just "
                          "going to keep asking until they get tired of lying."))),
        ("BK", "The Host. Brielle hosts <i>Hollywood Heat</i> on DBC. She's glamorous, "
         "ambitious, and Martin's girlfriend and hired gun.",
         ["Digs into the twins' birth records for Martin (Ep #0092)."],
         ("BRIELLE", ("", "I don't report the news, baby. I schedule it."))),
        ("MP", "The Challenger. Marcus Pryor is a charismatic state senator who "
         "challenges Jasmine in the primary. He's secretly bankrolled by Leonard Smilley.",
         ["Forces Jasmine into a runoff (Ep #0094). His affair is exposed by Kettle "
          "(Ep #0112). Loses the runoff (Ep #0113)."],
         ("PRYOR", ("", "Dynasties are just monarchies with better publicists."))),
    ]),
    ("The Circle's Families", None, [
        ("JU", "The Brother. Julian is Arianna's younger brother. He's gentle, funny, "
         "three years sober, and carrying the worst secret in Atlanta.",
         ["At 24, drunk, he hit and killed Raymond Holloway on October 16, 2021. "
          "Blackwater made the car and the evidence disappear.",
          "Meets Journee at a grief group (Ep #0028). Confesses to her (Ep #0169)."],
         ("JULIAN", ("", "I didn't come to that group to grieve. I came to "
                         "apologize. I just never found the words."))),
        ("EC", "The Surgeon. Dr. Evelyn Cummings is Arianna's mother and Atlanta's best "
         "cardiothoracic surgeon.",
         ["Operates on Victor after his collapse (Ep #0102).",
          "Knows her daughter is hiding something and is afraid to ask what."],
         ("EVELYN", ("", "I can fix a broken heart. I just can't fix my "
                         "children's."))),
        ("HC", "The Judge. Harold Cummings is Arianna's father, a retired Superior Court "
         "judge who taught her the law and doesn't know how far she's bent it.",
         ["Sat on the bench from 1990 to 2020."],
         ("HAROLD", ("", "I raised a prosecutor. I pray I didn't raise a "
                         "politician."))),
        ("GB", "The Builder. Gerald is Amond's father, owner of Baker &amp; Sons "
         "Contracting. He nearly lost everything in 2010.",
         ["Has no idea what Marc did to save his business, or what it started."],
         ("GERALD", ("", "That boy Marc is family. I'd bet a Bentley on it. I "
                         "have."))),
        ("YB", "The Mother. Yvonne is Amond's mother, a retired Spelman professor and "
         "the Belmont Crest neighbor everyone confesses to.",
         ["Wants Amond to marry Harmony, and doesn't trust her an inch."],
         ("YVONNE", ("", "Baby, love is patient. Harmony is not."))),
        ("CD", "The Father. Curtis Divine is Harmony's father, a retired mail carrier "
         "from southwest Atlanta and her biggest fan.",
         ["Has watched every one of her short films more than twenty times."],
         ("CURTIS", ("", "They don't see it yet. They will."))),
        ("LD", "The Mother. Lorna Divine is Harmony's mother, an ER nurse at Grady who "
         "has seen everything and is impressed by nothing.",
         ["Still hasn't forgiven Harmony for letting Lyric live in Belmont Crest."],
         ("LORNA", ("", "My grandbaby lives behind a gate. I raised mine behind a "
                        "prayer."))),
    ]),
    ("Belmont Crest", "Setting details in Document 04.", [
        ("LG", "The Gatekeeper. Lucinda is chair of the Country Club Membership "
         "Committee and has blackballed more people than anyone alive.",
         ["Widow of a bank president. A member since 1972.",
          "Tries to eject Esther from the Valentine's Ball (Ep #0031). Runs the Smilley "
          "vote (Ep #0140)."],
         ("LUCINDA", ("", "Membership is not a right, darling. It's a verdict."))),
        ("WO", "The Majordomo. Winston has run Summit House since 1985. He's "
         "British-Nigerian, impeccable, and a vault of family secrets.",
         ["Knows where Joan hid Gus's letters, and never says a word."],
         ("WINSTON", ("", "In this house, sir, the walls don't have ears. I "
                          "do."))),
        ("MF", "The Bartender. Malik runs the bar at the Country Club and The Vault, the "
         "private room where Atlanta's deals get made.",
         ["Hears everything and has never repeated a word. Yet."],
         ("MALIK", ("", "What's said in The Vault stays in The Vault. Until the price "
                        "is right."))),
        ("PW", "The House Manager. Mama Pearl runs Marc's estate and has raised Lyric "
         "since 2021. She's the only person Marc is afraid of.",
         ["Former cook at Summit House for 30 years. Joan “loaned” her to Marc.",
          "Has noticed that the twins eat exactly like Marc."],
         ("PEARL", ("", "Those Smilley girls hold a fork just like you, baby. Just "
                        "saying."))),
        ("PR", "The Chief of Staff. Priya runs the Donohue Foundation's day-to-day for "
         "Joan: brilliant, unflappable, Indian-American, and fiercely loyal.",
         ["Harvard Kennedy School. With the Foundation since 2016."],
         ("PRIYA", ("", "Mrs. Donohue doesn't do small. Neither do I."))),
    ]),
    ("Westbrook Academy", "The private school in Buckhead that the kids attend.", [
        ("AB", "The Head of School. Dr. Albright runs Westbrook with charm and an iron "
         "spine.", ["Catches Victoria's forged consent form (Ep #0014)."],
         ("DR. ALBRIGHT", ("", "Forgery, Miss Smilley, is not an extracurricular."))),
        ("EV", "The Teacher. Mr. Lane teaches drama and history. He's the teacher every "
         "kid remembers.",
         ["Assigns the Black History Month Roots Project that exposes the twins' "
          "paternity (Ep #0021)."],
         ("MR. LANE", ("", "Know your roots, people. Your roots always know you."))),
        ("JC", "The Classmate. Jaden is the twins' and Lyric's classmate and a class "
         "clown. His father is an APD deputy chief who arrives in Season 2.",
         ["Promoted with the class (Ep #0096). Starts 9th grade with them (Ep #0149)."],
         ("JADEN", ("", "Wait, y'all's Uncle Marc is <i>Marc-Anthony Bullock</i>?"))),
    ]),
    ("Broadway", None, [
        ("SC", "The Director. Sebastian is a British stage director, a Tony winner, and "
         "a tyrant, who stages the <i>Sweet Chariot</i> revival.",
         ["Directed Marc's 2018 Broadway revival too, the one that lost the Tony."],
         ("SEBASTIAN", ("", "Your grandfather sang it to the rafters, Marc. I need you "
                            "to sing it to the basement."))),
        ("NV", "The Co-Star. Nia is a Broadway star playing opposite Marc. She's "
         "gorgeous, gifted, and openly after him.",
         ["Nominated for a Tony alongside Marc (Ep #0084)."],
         ("NIA", ("", "Eight shows a week with Marc-Anthony Bullock? Somebody pinch "
                      "me. Actually, let him."))),
    ]),
    ("Alvin's World", "Arrives with Alvin at the halfway point.", [
        ("ZR", "The Son. Zion is a Morehouse junior who walks into Alvin's club and "
         "says he's his son. He's right.",
         ["Raised by his mother, Keisha Reed, an Atlanta hairstylist Alvin met in 2004.",
          "Paternity confirmed by Peter (Ep #0110). As Alvin's biological child, he's a "
          "Dynasty Trust beneficiary."],
         ("ZION", ("", "I don't want your money. I want your last name. Okay, maybe a "
                       "little of the money."))),
        ("CL", "The Girlfriend. Coco is a French-Senegalese model and gallerist from "
         "Paris, and far smarter than Alvin's other girlfriends.",
         ["Flew in with Alvin (Ep #0085). Sizing up the Donohues for her own reasons."],
         ("COCO", ("", "In Paris we have old money. In Atlanta you have "
                       "<i>loud</i> money. I like it."))),
        ("VM", "The Rival. Morrow is the boss of the Morrow Organization, an "
         "Irish-American mob that lost Atlanta's ports to Blackwater in 2017.",
         ["Uses Alvin to reach the World Cup security plans (Eps #0111–#0133).",
          "Jasmine owes him after the runoff (Ep #0113)."],
         ("MORROW", ("", "Somebody took my city. I'd like to meet him."))),
    ]),
    ("Smilley Corporation Staff", "The Smilley family itself is profiled in Document 06.", [
        ("RT", "The Lab Director. Darius runs the RootsKit lab. He's precise, "
         "principled, and Chinese-American.",
         ["Processes the Westbrook Roots Project kits (Ep #0037).",
          "Is uneasy about Nathaniel's “family alerts” on customer data."],
         ("DARIUS", ("", "DNA doesn't lie. The people reading it do."))),
    ]),
    ("The Theodore Branch", "Arrive in the final episodes of Season 1 (#0167–#0170) "
     "and join the Core cast in Season 2. Theodore himself is profiled in Document 02.", [
        ("LC", "The Wife. Lorraine is a New Orleans Creole from the Castille family: "
         "elegant, sharp, and every bit Joan's equal.",
         ["Married Theodore in 1969. Has spent the last decade with him in New "
          "Orleans."],
         ("LORRAINE", ("", "We didn't come home, Joan. We came back."))),
        ("XD", "The Son. Xander, named for Alexander, runs Castille Capital, a New York "
         "hedge fund. He wants his father's crown restored.",
         ["Grew up hearing the story of 1976 every night."],
         ("XANDER", ("", "My grandfather's name is on the building. So is "
                         "mine."))),
        ("CP", "The Daughter. Judge Celestine is Theodore's daughter and a judge on the "
         "Fifth Circuit Court of Appeals in New Orleans.",
         ["Mother of August. Married to Marcus Price, a New Orleans surgeon."],
         ("JUDGE CELESTINE", ("", "I don't rule on family matters. I just remember "
                                  "them."))),
        ("T3", "The Grandson. Theo is Xander's son, a charming media-startup founder "
         "who wants to take on The Donohue Company from the outside.",
         ["Martin's natural ally, and his natural rival."],
         ("THEO", ("", "Cousin Marc has an EGOT. I have a plan."))),
        ("SD", "The Granddaughter. Sienna is Xander's daughter, an influencer with 40 "
         "million followers who records everything.",
         ["The family's walking camera, and Kettle's new competition."],
         ("SIENNA", ("", "If it's not posted, it didn't happen. And trust me, it's "
                         "happening."))),
        ("AP", "The Kid. August is Celestine's son, 13, a chess prodigy who joins "
         "Westbrook Academy in Season 2.",
         ["Born the same year as the twins and Lyric."],
         ("AUGUST", ("", "So which one of you is the heir? Asking for my "
                         "grandfather."))),
    ]),
    ("History (Flashback Episodes)", None, [
        ("OS", "Otis Smilley was the Beacon's press foreman, fired by Alexander in 1958 "
         "for stealing printing plates. He swore he was framed until the day he died.",
         ["Applied to Belmont Crest in 1962 and was turned away by Simone's vote.",
          "Died in 1988."],
         ("OTIS", ("", "I set every letter of that paper, Mr. Donohue. I never "
                       "stole a single one."))),
        ("HW", "Harlan Whitfield was the white Atlanta attorney who fronted the 1958 "
         "land purchase for the Donohues at great personal risk.",
         ["Lost half his clients over it. Died in 1979."],
         ("HARLAN", ("", "Deeds don't have a color, Alexander. People do."))),
    ]),
]

story = cover("Supporting Characters — Document 10", [
    "Every character created beyond the main cast and the Smilley family",
    "<b>Ages as of the premiere:</b> Monday, January 5, 2026",
])
story.append(PageBreak())
story += [P("How to Use This Document", h1),
          *bullets([
              "Document 02 profiles the main cast. Document 06 profiles the Smilley family. "
              "This document profiles everyone else.",
              "Each profile shows the character's contract category and Season 1 episode "
              "count, both taken from Document 07 and the episode guide.",
              "Flashback versions of main characters (young Victor, young Joan, and "
              "others) are listed in Document 07.",
          ])]

for title, intro, people in SECTIONS:
    story.append(P(title, h1))
    if intro:
        story.append(P(intro, italic))
    for code, who, back, voice in people:
        name, born, died, cat, group, role = CAST[code]
        life = (f"<b>Born:</b> {long_date(born)} • <b>Died:</b> {long_date(died)}"
                if died else
                f"<b>Born:</b> {long_date(born)} • <b>Age:</b> {age_on(born)}")
        eps = (f"{counts[code]} (first: #{first[code]:04d})" if code in first
               else "Season 2")
        story.append(KeepTogether([
            P(name.upper(), h2),
            P(life),
            P(f"<b>Role:</b> {role} • <b>Category:</b> {cat} • "
              f"<b>S1 episodes:</b> {eps}"),
            P(who),
        ]))
        story += bullets(back)
        story.append(KeepTogether(scene("IN THEIR OWN WORDS", [voice])))
        story.append(Spacer(1, 6))

build(OUT, story, "Beyond the Crest — Supporting Characters",
      "BEYOND THE CREST — Supporting Characters — Writers' Room Confidential")
