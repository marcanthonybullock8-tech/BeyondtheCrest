"""Builds docs/02_Beyond_the_Crest_Character_Bible.pdf"""
import datetime as dt

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Spacer, KeepTogether

from cast import PARTY, MARC_PLATFORM, MARC_LONG_TERM
from btc_pdf import (P, h1, h2, body, italic, answer, bullets, table, scene,
                     age_on, long_date, build, cover, PREMIERE)

OUT = "docs/02_Beyond_the_Crest_Character_Bible.pdf"
D = dt.date

# ---------------------------------------------------------------------------
# CHARACTER DATA
# "given" = facts supplied by the showrunner (locked).
# Everything else is writers' room creation built on top of those facts.
# ---------------------------------------------------------------------------
CHARACTERS = [
    # ------------------------------ DONOHUE ------------------------------
    dict(
        family="THE DONOHUE FAMILY",
        name="VICTOR DONOHUE", born=D(1946, 5, 30), looks="early 60s",
        title="Chairman, The Donohue Company (2006–present) • Former CEO "
              "(1976–2006) • Retired actor, singer, director &amp; producer • EGOT",
        ties="Youngest son of Alexander &amp; Simone Donohue • Husband of Joan "
             "(m. Sat, June 14, 1969) • Father of Jasmine, Natasha &amp; Alvin • "
             "Younger brother of Theodore",
        who="The King of Belmont Crest. Victor is velvet over steel: a warm baritone laugh, "
            "a perfectly knotted tie, and a memory that never forgets a debt or a slight. He "
            "is beloved in public and feared in private. He has buried rivals in boardrooms "
            "for fifty years without raising his voice, and the one time he did raise it, a "
            "network changed hands by Monday.",
        back=[
            "Born in Atlanta while his father was turning <i>The Atlanta Beacon</i>, a "
            "Black newspaper, into a media house. Raised between the newsroom, the radio "
            "booth, and the family's first soundstage.",
            "Became a matinee idol in the 1960s through Donohue Pictures, then a Broadway "
            "leading man who could sing the rafters down. He isn't a professional singer, "
            "but his Grammy for a Broadway cast album completed the EGOT.",
            "Married Joan Mercer, his co-star, on Saturday, June 14, 1969. It is still the "
            "most photographed wedding in Donohue history.",
            "On Monday, January 5, 1976, his father made him CEO over his older brother "
            "Theodore. Theodore has never forgiven either of them.",
            "Over thirty years as CEO he built The Donohue Company into the largest media "
            "and entertainment conglomerate on Earth. He became Chairman after Alexander "
            "died on Monday, January 9, 2006, and handed the CEO chair to Natasha.",
            "Personally named his grandson Marc-Anthony as heir apparent. That decision "
            "split the third generation in two.",
        ],
        secrets=[
            "Knows more about everyone's sins than anyone alive, and keeps the files.",
            "The 1976 succession wasn't only merit. What Alexander knew about Theodore that "
            "day is a buried family secret.",
        ],
        voice=("VICTOR", ("", "I don't make threats, son. Threats are for men who might "
                              "not follow through.")),
    ),
    dict(
        name="JOAN DONOHUE (née MERCER)", born=D(1948, 4, 17), looks="mid-50s",
        title="Philanthropist • Chair, The Donohue Foundation • Retired actress, "
              "singer, director &amp; producer • EGOT",
        ties="Wife of Victor (m. 1969) • Mother of Jasmine, Natasha &amp; Alvin",
        who="The Queen Mother. Joan is grace, discipline, and a gaze that can end a "
            "conversation. She runs the Donohue Foundation, which spares no expense, "
            "the way a general runs a campaign. Nothing happens at Summit House without "
            "her knowing, and most of it happens because she decided it would.",
        back=[
            "Born in Macon, Georgia, the daughter of a Baptist choir director and a "
            "schoolteacher. She came to Atlanta at 17 with one suitcase and a voice.",
            "Discovered at a Donohue Pictures open call. Became Hollywood's first Black "
            "leading lady to headline a studio musical, and later directed and produced.",
            "Completed her EGOT with a Tony for a Broadway revival. She retired at the top "
            "of her game to devote herself to the Foundation.",
            "Holds the family together through every scandal. She is the only person Victor "
            "has never lied to, as far as she knows.",
        ],
        secrets=[
            "Keeps a private ledger of every grandchild's secrets. She suspects things about "
            "Marc-Anthony she has never said aloud.",
        ],
        voice=("JOAN", ("smiling, pouring tea", "Baby, I was ruining people's lives in "
                        "heels before your mama was born. Sit down.")),
    ),
    dict(
        name="ALVIN DONOHUE", born=D(1980, 10, 8), looks="early 30s",
        title="Entertainment power player • Political fixer • Party boy • "
              "Underworld-connected",
        ties="Youngest son of Victor &amp; Joan • Brother of Jasmine &amp; Natasha • "
             "Uncle to the third generation",
        who="The Donohue wild card. Alvin is the life of every party from Buckhead to Monaco, "
            "and he can close a deal, a campaign fundraiser, or a back-room arrangement "
            "before last call. He's charming, reckless, and much smarter than the tabloids "
            "think. He is deeply connected in entertainment, in Georgia politics, and in "
            "Atlanta's underworld.",
        back=[
            "The “surprise” baby, born ten years after Jasmine. Spoiled by Joan, "
            "underestimated by Victor.",
            "Ran Donohue Records' A&amp;R and nightlife ventures in his 20s. Built a web of "
            "clubs, promoters, and political donors that makes him the family's unofficial "
            "fixer.",
            "Has a string of relationships across three continents and famously never uses "
            "protection. Even Alvin doesn't know how many children he has, if any.",
        ],
        secrets=[
            "His underworld associates are rivals of The Blackwater Syndicate. He has no idea "
            "his nephew runs it.",
            "Every paternity claim that surfaces is a story engine. Any child of Alvin's is "
            "Donohue blood, with a potential claim on the trust.",
        ],
        voice=("ALVIN", ("raising a glass", "I'm not the black sheep of this family. I'm "
                         "the only one who admits he's in the pasture.")),
    ),
    dict(
        name="THEODORE DONOHUE", born=D(1944, 7, 31), looks="early 60s",
        title="Retired attorney • Former Fulton County District Attorney (1981–1996)",
        ties="Eldest son of Alexander &amp; Simone • Older brother of Victor • "
             "Great-uncle to the third generation",
        who="The Eldest Son Who Was Passed Over. Theodore is courtly and brilliant, with a "
            "prosecutor's instinct for weakness and a lifetime of favors owed to him in every "
            "courthouse in Georgia. He's corrupt to the bone and patient as a glacier.",
        back=[
            "Groomed as Alexander's heir, then passed over for Victor on January 5, 1976. He "
            "took the insult to the law instead.",
            "As Fulton County DA for fifteen years, he built a machine of judges, cops, and "
            "politicians who still owe him.",
            "Retired from private practice in 2015 but never retired from power.",
        ],
        secrets=[
            "Sees himself in Martin, the eldest grandson of the eldest child, passed over for "
            "the golden boy. He is quietly backing Martin's war for the throne.",
            "Holds the key to why Alexander chose Victor in 1976.",
        ],
        voice=("THEODORE", ("", "History has a way of repeating itself, nephew. I intend "
                            "to see that this time it gets the ending right.")),
    ),
    # ------------------------------ OLSON ------------------------------
    dict(
        family="THE OLSON FAMILY",
        name="CONGRESSWOMAN JASMINE OLSON (née DONOHUE)", born=D(1970, 3, 23),
        looks="about 40",
        title="U.S. Representative for Georgia (1997–present)",
        ties="Eldest child of Victor &amp; Joan • Wife of Dr. Peter Olson (m. Sat, "
             "June 16, 1990) • Mother of Martin &amp; Mallory",
        who="The Firstborn. Jasmine won her seat at 26 and has held it for nearly thirty "
            "years. She is a legislative powerhouse who can whip votes, kill bills, and make "
            "cabinet secretaries sweat on C-SPAN. Deep down she believes the Donohue crown "
            "should have run through her, the eldest, and through her son.",
        back=[
            "Spelman College, then Georgetown Law. Married Peter, her college sweetheart, at "
            "20. Martin was born the next spring.",
            "Suffered years of heartbreak trying to have a second child before Mallory, her "
            "miracle, arrived in 1995.",
            "Elected in November 1996 and sworn into Congress in January 1997. She has never "
            "lost a race.",
        ],
        secrets=[
            "Supports Martin's claim to the throne more than she admits to her father.",
            "Arianna Cummings's possible 2028 presidential run could collide with Jasmine's "
            "own ambitions.",
        ],
        voice=("JASMINE", ("", "I have been first in this family since the day I was born. "
                           "I don't intend to start finishing second now.")),
    ),
    dict(
        name="DR. PETER OLSON", born=D(1969, 11, 13), looks="early 40s",
        title="Chief of Plastic Surgery, Atlanta Metropolitan Medical Center • Founder, "
              "Olson Facial Plastic &amp; ENT Institute",
        ties="Husband of Jasmine (m. 1990) • Father of Martin &amp; Mallory",
        who="The Surgeon. He has steady hands, an ego to match, and a client list that could "
            "topple Hollywood if his files ever leaked. Peter is insanely wealthy in his own "
            "right, but he married into royalty and feels it every Sunday dinner.",
        back=[
            "Morehouse, then Johns Hopkins Medicine. Double-boarded in facial plastics and "
            "otolaryngology.",
            "Built the most exclusive private surgical practice in the Southeast. His "
            "patients include senators, stars, and people who officially never had work done.",
        ],
        secrets=[
            "His practice's confidential records are a gold mine every schemer in town wants.",
            "Dotes on Mallory, but his relationship with Martin is colder than anyone knows.",
        ],
        voice=("PETER", ("", "Everybody in Atlanta has a face they show the world. I just "
                         "know what's underneath it.")),
    ),
    dict(
        name="MARTIN OLSON", born=D(1991, 5, 15), looks="late 20s",
        title="President, Donohue Broadcasting Group • Self-declared rightful heir",
        ties="Eldest child of Jasmine &amp; Peter • Older brother of Mallory • "
             "Cousin and sworn enemy of Marc-Anthony",
        who="The Rival. Martin is the eldest grandson of the eldest child, and he never lets "
            "anyone forget it. He's polished, ice-cold, relentlessly ambitious, and "
            "astronomically deadly. He is also secretly trained in close combat and marksmanship, "
            "and rumor has it that two business rivals who crossed him simply stopped existing. "
            "He has never been charged with anything.",
        back=[
            "Harvard, then Wharton MBA. Rose fast inside The Donohue Company and now runs its "
            "broadcast network empire.",
            "Christmas Day, 2004, at Summit House: Victor raised a toast to Marc-Anthony as "
            "“the future of this family.” That night Martin, 13, shoved Marc, 12, "
            "down the grand staircase and broke his arm. It was ruled an accident. It wasn't.",
            "Has spent twenty years building allies, dossiers, and quiet leverage for the day "
            "he takes the crown.",
        ],
        secrets=[
            "Allied with Great-Uncle Theodore, and increasingly with Uncle Alvin.",
            "Obsessed with finding the one thing that can destroy Marc-Anthony. If he ever "
            "discovers Blackwater, the family goes to war.",
        ],
        voice=("MARTIN", ("", "Birth order is the only law this family ever respected. "
                          "I'm just here to enforce it.")),
    ),
    dict(
        name="MALLORY OLSON", born=D(1995, 6, 5), looks="early 20s",
        title="Office Manager, Olson Facial Plastic &amp; ENT Institute • "
              "Entrepreneur-in-waiting",
        ties="Youngest child of Jasmine &amp; Peter • Younger sister of Martin • "
             "Cousin and future business partner of Grace",
        who="The Miracle Child. Mallory is brilliant, business-savvy, spoiled, and a "
            "certified daddy's girl. She runs her father's multimillion-dollar practice like "
            "a Swiss watch and is ready to prove she's more than Peter Olson's princess. She is "
            "a virgin by choice and by standard: nobody has ever been good enough.",
        back=[
            "Born after years of loss, and treated like a treasure ever since.",
            "Emory undergrad, then Goizueta MBA. Took over her father's office at 24 and "
            "doubled its revenue.",
            "Planning to launch HEIRLOOM, a luxury beauty &amp; wellness brand, with her cousin Grace on June 5, 2026.",
        ],
        secrets=[
            "Caught between her brother's war and her love for her Bullock cousins.",
            "Her business will collide head-on with Smilley Beauty, and with Esther Smilley.",
        ],
        voice=("MALLORY", ("", "I'm not spoiled. I'm appropriately appreciated.")),
    ),
    # ------------------------------ BULLOCK ------------------------------
    dict(
        family="THE BULLOCK FAMILY",
        name="ROBERT BULLOCK", born=D(1969, 2, 10), looks="early 40s",
        title="Founder &amp; Managing Partner, Bullock &amp; Associates, LLP (1995–present) "
              "• Criminal defense &amp; entertainment attorney",
        ties="Husband of Natasha (m. Sat, June 22, 1991) • Father of Elxa, Marc-Anthony "
             "&amp; Grace • Son-in-law of Victor &amp; Joan",
        who="The Shark. Robert gets the guilty acquitted and the famous richer, and he bills "
            "for both. He's astronomically corrupt, astronomically ruthless, and so charming "
            "that juries thank him on the way out. He is the only man in Atlanta who has "
            "stared down Victor Donohue and kept his job.",
        back=[
            "Raised in southwest Atlanta by a single mother who cleaned offices on Peachtree. "
            "Clark Atlanta University, then Howard Law, on scholarship and spite.",
            "Met Natasha when she was 18 and he was 20, a broke Clark Atlanta sophomore with "
            "a mouth on him. The Donohues were scandalized that their princess chose a "
            "nobody from the Westside. Elxa was born in August 1990, and he married Natasha in June 1991 "
            "while she was pregnant with Marc-Anthony. Victor still calls it “the "
            "hostile takeover.”",
            "Opened Bullock &amp; Associates on Wednesday, March 1, 1995. Today it is the "
            "most feared defense and entertainment firm in America.",
        ],
        secrets=[
            "Has quietly represented people connected to Blackwater without knowing who's at "
            "the top.",
            "Knows where some of Theodore's bodies are buried, literally and figuratively.",
        ],
        voice=("ROBERT", ("", "Innocent costs extra.")),
    ),
    dict(
        name="NATASHA BULLOCK (née DONOHUE)", born=D(1971, 6, 2), looks="late 30s",
        title="CEO, The Donohue Company (2006–present) • Actress, singer &amp; producer "
              "• One award short of an EGOT (missing the Oscar)",
        ties="Middle child of Victor &amp; Joan • Wife of Robert (m. 1991) • "
             "Mother of Elxa, Marc-Anthony &amp; Grace",
        who="The Queen Regent. Natasha is a movie star who became the most powerful CEO in "
            "the world, and she never stopped performing. She's ruthless, dangerous, and "
            "gleefully willing to bend any rule that stands between her family and what it "
            "deserves. Marc-Anthony got his rule-bending from her, and she's proud of it.",
        back=[
            "Child star turned leading lady. Won the Emmy, Grammy, and Tony, and has three "
            "Oscar nominations and no Oscar.",
            "Chose Robert over her father's wishes, and has spent 35 years proving she was "
            "right.",
            "Named CEO in January 2006 after Alexander's death. She has since tripled the "
            "company's value.",
        ],
        secrets=[
            "Suspects Marc-Anthony has a second life. She has chosen not to ask.",
            "Is grooming Marc to succeed her, which makes her Jasmine's rival as well as "
            "her sister.",
        ],
        voice=("NATASHA", ("", "Rules are just suggestions written by people who were "
                           "scared of me.")),
    ),
    dict(
        name="CHIEF ELXA JACKSON (née BULLOCK)", born=D(1990, 8, 29), looks="mid-20s",
        title="Chief of Police, Atlanta Police Department (appointed Tue, September 2, 2025) "
              "• Former Lieutenant, Homicide",
        ties="Eldest child of Robert &amp; Natasha • Older sister of Marc-Anthony &amp; "
             "Grace • Wife of Det. Jeremy Jackson (m. Sat, June 15, 2024)",
        who="The Top Cop. Elxa is the eldest grandchild, and she walked away from the "
            "Donohue throne to carry a badge. She's formidable, fearless, and about 25% by "
            "the book and 75% not. She closes cases her way and dares anyone to prove she "
            "cut a corner. She's more like her little brother than she'll ever admit.",
        back=[
            "Born before her parents married, which the Donohues still don't discuss at "
            "dinner.",
            "Spelman, then Georgia State (criminal justice). Joined APD at 22. Made homicide "
            "detective at 27 and lieutenant at 31, with the highest clearance rate in the "
            "department's history.",
            "Became Atlanta's youngest-ever Chief of Police at 35.",
            "Wants children badly. Every time she brings it up, Jeremy finds a reason not to "
            "talk about it.",
        ],
        secrets=[
            "As a homicide lieutenant she worked cases that left a mysterious pattern "
            "she privately called “the ghost network.” She has no idea it's her "
            "brother's Blackwater Syndicate.",
        ],
        voice=("ELXA", ("", "I follow the rules. I just read them very, very creatively.")),
    ),
    dict(
        name="MARC-ANTHONY BULLOCK", born=D(1992, 1, 5), looks="mid-20s",
        title="Actor, singer, screenwriter, director &amp; producer • One award short of "
              "an EGOT (missing the Tony) • Billionaire Heir &amp; Primary Heir Apparent "
              "of the Donohue Family • <b>SECRET</b> Founder &amp; Boss, The Blackwater "
              "Syndicate (2010–present)",
        ties="Only son of Robert &amp; Natasha • Younger brother of Elxa, older brother of "
             "Grace • Grandson &amp; Golden Boy of Victor &amp; Joan • Godfather "
             "&amp; guardian of Lyric Solace Baker • Unknowing father of Emma &amp; "
             "Victoria Smilley • Destined soulmate: Esther Smilley",
        who="The Golden Boy. Marc-Anthony is the sweetest, kindest, most loving, compassionate, "
            "innocent, and pure man in the world: the man who remembers the valet's kids' "
            "birthdays and cries at dog-food commercials. He's outgoing and magnetic, lights "
            "up every room and camera, and is gut-bustingly, unhinged, unfiltered-offensive "
            "funny. His reported IQ is 250. Hurt someone he loves, though, and the sweetest man "
            "in the world becomes the most dangerous one. He's a certified crash-out, "
            "Harry Potter and Percy Jackson times 2000. When a rule is unjust, unfair, or "
            "just plain stupid, he bends it, breaks it, or quietly rewrites it. "
            "<b>Personal net worth: over $990 billion, rising every single day.</b>",
        back=[
            "Born Sunday, January 5, 1992, sixteen years to the day after his grandfather "
            "became CEO. Joan called it a sign. <b>The series premieres on his 34th "
            "birthday.</b>",
            "Made his screen debut at 6 in a Donohue Pictures family film. Skipped grades, "
            "graduated the Belmont Academy at 14, and finished Yale (film &amp; theater, "
            "economics) at 17.",
            "Christmas 2004: Victor toasted him as “the future of this family.” That "
            "night Martin pushed him down the stairs. Marc has never forgotten.",
            "Summer 2010: a predatory developer and a ring of crooked officials destroyed "
            "Amond's family's business, and the courts shrugged. Marc, 18, took them apart "
            "in 90 days using money, intelligence, and pressure. On Saturday, September 18, "
            "2010, he founded <b>The Blackwater Syndicate</b>. It grew into a 100% criminal "
            "organization, a true mafia with a code, and the largest criminal organization "
            "in the world. On October 3, 2011, he founded its legitimate twin, <b>Blackwater "
            "Security International (BSI)</b>. See Document 05.",
            "Saturday, September 3, 2011: at a Labor Day weekend party at a Lake Lanier "
            "estate, a very drunk 19-year-old Marc spent the night with a girl in a gold "
            "dress. He never learned her name and barely remembers the night. It was Esther "
            "Smilley.",
            "Awards: Emmy (Sun, Sept 18, 2016, Lead Actor, Limited Series); Tony "
            "nomination (Sun, June 10, 2018, lost); Grammy (Sun, Feb 10, 2019, Musical "
            "Theater Album for that same Broadway revival); Oscar (Sun, Mar 12, 2023, "
            "Best Original Screenplay, plus a Best Actor nomination). The Tony is the "
            "only thing between him and an EGOT.",
            "Friday, February 12, 2021: a sealed Fulton County family court order gave him "
            "temporary custody of his goddaughter Lyric. Five years later, he still has no "
            "explanation, and he isn't complaining.",
            "Built his personal fortune with early bets in tech, streaming, and AI, his trust, "
            "and Blackwater's reach. On paper, he's worth more than most nations.",
        ],
        dream="His number-one, ultimate dream is family: a big, gigantic family. Kids are "
              "non-negotiable. He believes in generational wealth. Kids adore him and he adores "
              "them. The cruelest irony in Belmont Crest is that two of the girls who "
              "raid his kitchen every weekend are his own daughters, and he has no idea.",
        secrets=[
            "<b>Blackwater.</b> Only the Table (his inner council, including Amond as "
            "underboss), Arianna (who keeps plausible deniability), and Grace (who'd hide a "
            "body for him) know. His sister the Chief of Police does not.",
            "<b>Emma &amp; Victoria.</b> He has ZERO idea he is their father.",
            "<b>The White House.</b> He secretly plans to run for President in 2028. He "
            "hasn't told anyone, not Amond, not Grace, and not Arianna, who is weighing a "
            "run of her own.",
        ],
        politics=True,
        voice=("MARC-ANTHONY", ("warm smile, eyes gone cold", "I love everybody, man. "
                                "That's the problem. You touched somebody I love.")),
    ),
    dict(
        name="GRACE BULLOCK", born=D(1994, 4, 12), looks="early 20s",
        title="Actress &amp; singer (Emmy &amp; Tony winner) • Entrepreneur-in-waiting",
        ties="Youngest child of Robert &amp; Natasha • Younger sister of Elxa &amp; "
             "Marc-Anthony • Cousin and future business partner of Mallory",
        who="The Baby Sister and Ride-or-Die. Grace is gorgeous, gifted, and fiercely loyal. "
            "She's the actress directors fight over and the sister who would hide a body "
            "for her brother without asking whose it was. She and Marc have been joined at "
            "the hip since she could walk.",
        back=[
            "Broadway at 19. Won the Tony at 23 and a Primetime Emmy at 27.",
            "Launching HEIRLOOM, a luxury beauty &amp; wellness brand, with Mallory. It's her first "
            "venture outside the family business.",
        ],
        secrets=[
            "One of three people who know about Blackwater. She has already helped her "
            "brother at least once in ways her sister the Chief can never find out about.",
        ],
        voice=("GRACE", ("", "Whatever it is, I don't want to know. Where's the shovel?")),
    ),
    # ------------------------------ OTHERS ------------------------------
    dict(
        family="THE CIRCLE",
        name="AMOND BAKER", born=D(1992, 2, 10), looks="mid-20s",
        title="Businessman on the rise • Marc-Anthony's best friend, brother &amp; right "
              "hand • <b>SECRET</b> Underboss, The Blackwater Syndicate",
        ties="Son of an upper-middle-class Belmont Crest family • Father of Lyric Solace "
             "Baker • On-and-off love of Harmony Divine • Shares a birthday with "
             "Robert Bullock",
        who="The Brother. Amond is loyal to the marrow and hungry to the bone. He wants what "
            "the Donohues have: respect, power, and the kind of money that makes rules "
            "optional. He's willing to become ruthless, dangerous, and corrupt to get it. His "
            "weakness is Harmony. He is genuinely, madly, deeply in love with a woman who "
            "breaks up with him every other season.",
        back=[
            "Best friends with Marc since kindergarten at the Belmont Academy.",
            "Watched his family nearly lose everything in 2010, and watched Marc save them. "
            "He has been Marc's right hand ever since.",
            "Became a father at 20 when Lyric was born. Since February 2021 his daughter has "
            "lived with Marc under a sealed court order, and Amond has never said why.",
        ],
        secrets=[
            "Knows more about why Marc got custody of Lyric than he admits.",
            "His ambition is starting to outgrow second place.",
        ],
        voice=("AMOND", ("", "I'd take a bullet for him. I just want to own the building "
                         "it happens in.")),
    ),
    dict(
        name="ARIANNA CUMMINGS", born=D(1992, 10, 25), looks="mid-20s",
        title="Attorney General of Georgia (appointed Mon, March 17, 2025) • Former "
              "Fulton County District Attorney (2021–2025) • Possible 2028 "
              "presidential candidate",
        ties="Daughter of an upper-class Belmont Crest family • Marc-Anthony's best "
             "friend, sister &amp; right hand",
        who="The Prosecutor. Arianna is a political phenom, the youngest DA in Fulton County "
            "history and now the state's top law enforcement officer. She has a spotless "
            "public record, a camera-ready smile, and a spine of titanium. She is "
            "seriously weighing a run for president in 2028. She'd be 36 on Inauguration "
            "Day, constitutionally eligible.",
        back=[
            "Grew up three houses down from the Bullocks. She, Marc, and Amond were the "
            "Belmont Crest Three.",
            "Harvard Law at 22. Elected DA at 28. Appointed Attorney General at 32 when the "
            "sitting AG resigned in scandal.",
        ],
        secrets=[
            "Has skeletons in her closet that Marc helped her bury. The truth is sealed in "
            "the writers' room for a future arc.",
            "Knows Blackwater exists and chooses not to know details. That's plausible "
            "deniability, and it's also a time bomb for 2028.",
        ],
        voice=("ARIANNA", ("", "I'm the law in Georgia, Marc. So whatever you're about "
                           "to tell me, don't.")),
    ),
    dict(
        name="ESTHER SMILLEY", born=D(1992, 9, 20), looks="early 20s",
        title="Billionaire Heiress • President &amp; COO and designated heir, Smilley "
              "Corporation",
        ties="Youngest of three children of the Smilley family • Mother of Emma &amp; "
             "Victoria • Best friend and sister of Harmony Divine • Destined "
             "soulmate: Marc-Anthony Bullock",
        who="The Ice Queen. Widely called the most beautiful woman in the world, all "
            "natural, and 1000% ruthless and corrupt. Esther helps run Smilley Corporation, "
            "a consumer products, retail, and lifestyle empire, with surgical cruelty. Her "
            "grandfather Gus chose her, the baby, as heir over her older siblings, and she "
            "has been at war with them ever since.",
        back=[
            "Born in Manhattan. Raised in Buckhead's Tuxedo Park after the family moved to "
            "Atlanta in 1996. The Smilleys are new-ish money who resent Donohue old money.",
            "Met Harmony in 6th grade at the Westbrook Academy in 2003, when Harmony was the "
            "scholarship kid. They have been sisters ever since.",
            "Saturday, September 3, 2011: the Lake Lanier party. Drunk, 18, in a gold dress, "
            "she spent the night with Marc-Anthony Bullock. Twins, Emma and Victoria, were "
            "born Thursday, May 10, 2012.",
            "She chose to keep it secret. The official story is IVF with an anonymous sperm "
            "donor. It is a thin story for a 19-year-old heiress, and her siblings have "
            "never fully bought it.",
            "Has spent fourteen years avoiding Marc-Anthony. She skipped Lyric's christening "
            "and has turned down every gala he attends. All of Atlanta assumes she just "
            "can't stand him.",
        ],
        secrets=[
            "If her siblings prove the twins are Donohue blood, they will use it to strip "
            "her of the Smilley inheritance.",
            "Forbids the twins from working with Marc for one reason: up close, they look "
            "exactly like him.",
        ],
        voice=("ESTHER", ("", "I don't hate Marc-Anthony Bullock. Hate requires "
                          "proximity.")),
    ),
    dict(
        name="HARMONY DIVINE", born=D(1992, 6, 19), looks="mid-20s",
        title="Aspiring filmmaker, screenwriter &amp; director",
        ties="Daughter of a middle-class Atlanta family • Esther's best friend and "
             "sister • Mother of Lyric • On-and-off love of Amond Baker",
        who="The Dreamer Nobody Believes In. Harmony has the scripts, the vision, and the "
            "fire, and every door in town slams in her face. Her best friend is a "
            "billionaire, and her daughter's father's best friend is Hollywood royalty, but "
            "she refuses to be anybody's charity case. Her pride keeps her poor and her "
            "heart keeps her circling back to Amond. The toxicity in their on-and-off love "
            "comes mostly from her end.",
        back=[
            "Born on Juneteenth to a mail carrier and a nurse in southwest Atlanta. Scholarship "
            "kid at Westbrook Academy, where she met Esther.",
            "Had Lyric at 19 and dropped out of film school.",
            "In February 2021, under the sealed order, her daughter went to live with "
            "Marc-Anthony. She has never publicly said why.",
        ],
        secrets=[
            "Figured out years ago that the twins are Marc-Anthony's. She has never told "
            "Esther she knows.",
            "Secretly writes Atlanta's most-read gossip blog, <i>The Tea Kettle ATL</i>.",
        ],
        voice=("HARMONY", ("", "Everybody in this town wants to discover talent. Nobody "
                           "wants to fund it.")),
    ),
    dict(
        name="DETECTIVE JEREMY JACKSON", born=D(1990, 12, 2), looks="late 20s",
        title="Senior Detective, APD Homicide",
        ties="Son of former APD Chief Walter Jackson • Husband of Chief Elxa Jackson "
             "(m. 2024)",
        who="The Boy Scout. Jeremy does everything 100% by the book. He's an honest cop, "
            "the son of a legend, and married to a woman who is his boss, his opposite, and "
            "the love of his life. Every time Elxa brings up children, he changes the "
            "subject.",
        back=[
            "Grew up in the shadow of his father, Chief Walter Jackson, and chose to be "
            "flawless rather than famous.",
            "Married Elxa on Saturday, June 15, 2024. Since September 2025 he reports up the "
            "chain to his own wife, a conflict-of-interest story waiting to happen.",
        ],
        secrets=[
            "The real reason he avoids the children conversation is sealed in the writers' "
            "room.",
            "Has quietly opened a file on an untraceable network behind a string of "
            "“justice” cases. He's hunting Blackwater, and his brother-in-law.",
        ],
        voice=("JEREMY", ("", "The book exists for a reason, Elxa. Somebody has to read it.")),
    ),
    # ------------------------------ CHILDREN ------------------------------
    dict(
        family="THE CHILDREN",
        name="EMMA SMILLEY", born=D(2012, 5, 10), looks="13",
        title="8th grader, Westbrook Academy • Aspiring actress, singer &amp; producer",
        ties="Elder twin daughter of Esther Smilley and (secretly) Marc-Anthony Bullock "
             "• Twin sister of Victoria • Best friend of Lyric",
        who="The Elder Twin. Emma is respectful, responsible, organized, and fiercely "
            "talented, and she's a 1000% daddy's girl who doesn't know who her daddy is. "
            "Her talent, timing, charisma, and even her laugh are pure Marc-Anthony. Her "
            "favorite actor is Marc-Anthony Bullock, and her dream is for him to mentor "
            "and manage her. Her mother 100% forbids it and won't say why.",
        back=[
            "Raised as a Smilley on the IVF story. Through Lyric she became a fixture at "
            "“Uncle Marc's” house, and he spoils her and Victoria endlessly.",
            "Still knows the true meaning of hard work. She practices, rehearses, and "
            "plans.",
        ],
        secrets=["Keeps a notebook of every way she's “just like” Marc-Anthony."],
        voice=("EMMA", ("", "Mom says no. She just never says why. So I'm going to find "
                        "out.")),
    ),
    dict(
        name="VICTORIA SMILLEY", born=D(2012, 5, 10), looks="13",
        title="8th grader, Westbrook Academy • Aspiring actress, singer &amp; director",
        ties="Younger twin daughter of Esther Smilley and (secretly) Marc-Anthony Bullock "
             "• Twin sister of Emma • Best friend of Lyric",
        who="The Wild Child, contained. Victoria is respectful and responsible, but only just. "
            "She's bold, hilarious, unfiltered, and allergic to the word “no,” "
            "which is pure Marc-Anthony. She's a 1000% daddy's girl who wants her favorite "
            "actor to mentor and manage her. Her mother's ban only makes her want it more.",
        back=[
            "The twin who talks her way into trouble and out of it in the same sentence.",
            "Sneaks over to Marc's with Lyric more often than Esther knows.",
        ],
        secrets=["She has already noticed that she and Emma look more like Uncle Marc than "
                 "their own mother."],
        voice=("VICTORIA", ("", "Technically Mom said don't <i>work</i> with him. She "
                            "never said don't <i>visit</i>.")),
    ),
    dict(
        name="LYRIC SOLACE BAKER", born=D(2012, 4, 20), looks="13",
        title="Working actress (2022–present) • 8th grader, Westbrook Academy",
        ties="Daughter of Amond Baker &amp; Harmony Divine • Goddaughter and ward of "
             "Marc-Anthony (custody since Feb 12, 2021) • Best friend of Emma &amp; "
             "Victoria",
        who="The Angel. Lyric is a literal sweetheart: kind, gifted, gentle, and wise beyond "
            "13. She's been a working actress since 2022 under the mentorship of her "
            "godfather, and she is the reason the Smilley twins keep ending up at Marc's.",
        back=[
            "Moved in with her godfather at 8 under the sealed custody order.",
            "Booked her first professional role in the spring of 2022; principal "
            "photography began Monday, June 6, 2022.",
        ],
        secrets=["Might know more about why she lives with Uncle Marc than any adult "
                 "realizes."],
        voice=("LYRIC", ("", "Uncle Marc says family is who shows up. He always shows up.")),
    ),
]

# ---------------------------------------------------------------------------
story = cover("Character Bible — Document 02", [
    "<b>Ages locked as of the premiere:</b> Monday, January 5, 2026",
    "<b>Primary settings:</b> Belmont Crest &amp; Atlanta, Georgia",
    "<b>Ensemble:</b> All characters in this document are African American",
])
story.append(PageBreak())

# ---------------- SETTING ----------------
story += [P("The World of the Show", h1),
          P("Belmont Crest", h2),
          P("A private, gated community of 1,240 wooded acres on a ridge above the "
            "Chattahoochee River at Atlanta's northwestern edge, inside the city limits. "
            "The main gate is at <b>1958 Belmont Crest Parkway NW, Atlanta, GA 30327</b>, "
            "about 8 miles from downtown, with Buckhead's Tuxedo Park just across the ridge. "
            "Alexander and Simone Donohue founded it on Saturday, May 17, 1958, when no "
            "Black family could buy land there, so they bought it through a white front. "
            "Today "
            "it is the most exclusive address in the South, home to the Donohues, the "
            "Bullocks, the Olsons, the Bakers, and the Cummingses. At the very top of the "
            "ridge sits <b>Summit House</b>, Victor and Joan's estate. Everything else in "
            "Belmont Crest lives <i>beyond the crest</i>. It also has its own country club, "
            "founded in 1961. See Document 04."),
          P("The Donohue Company", h2),
          P("The largest multinational mass media and entertainment conglomerate on Earth. "
            "Alexander Donohue founded it on Monday, April 3, 1939, as <i>The Atlanta "
            "Beacon</i>, a Black newspaper. It grew into radio, “race films,” "
            "records, television, and eventually everything: Donohue Pictures, Donohue "
            "Broadcasting Group, Donohue Records, Donohue Publishing, Donohue streaming, "
            "theme parks, and live events. Headquartered at Donohue Tower in Midtown "
            "Atlanta. <b>Company valuation: $10 trillion. Family fortune: over $2.5 "
            "trillion.</b> See Document 03. The Donohues are the largest, "
            "most successful, powerful, influential, respected, beloved, charitable, and "
            "wealthiest family in the world."),
          table([
              ["Era", "Leadership"],
              ["1939 – 1976", "Alexander Donohue, Founder &amp; CEO"],
              ["1976 – 2006", "Alexander, Chairman • Victor, CEO"],
              ["2006 – present", "Victor, Chairman • Natasha, CEO • "
                                      "Marc-Anthony, Primary Heir Apparent"],
          ], [1.6 * inch, 4.9 * inch]),
          Spacer(1, 6),
          P("Family founders (deceased)", h2),
          *bullets([
              f"<b>Alexander Donohue</b> ({long_date(D(1916, 3, 3))} – "
              f"{long_date(D(2006, 1, 9))}; died at 89). Founder of The Donohue Company "
              "and co-founder of Belmont Crest.",
              f"<b>Simone Donohue (née Batiste)</b> ({long_date(D(1920, 9, 12))} – "
              f"{long_date(D(2014, 11, 22))}; died at 94). A New Orleans-born jazz singer "
              "who bankrolled the first printing press, co-founded Belmont Crest, and was "
              "the family's first matriarch.",
          ]),
          P("Aging note: “Black don't crack”", h2),
          P("Every character's <b>age</b> is exact to their birthday. Every character's "
            "<b>look</b> is much younger. The “Looks” field below is the on-screen "
            "casting guide."),
          PageBreak()]

# ---------------- AGE LEDGER ----------------
rows = [["Character", "Born", "Age on 1/5/2026", "Looks", "Next Birthday (turns)"]]
for c in CHARACTERS:
    b = c["born"]
    nxt = D(2026, b.month, b.day)
    if nxt < PREMIERE:
        nxt = D(2027, b.month, b.day)
    turns = age_on(b, nxt)
    nm = c["name"].split(" (")[0].title().replace("Of", "of")
    rows.append([nm, f"{b:%a %b} {b.day}, {b.year}", str(age_on(b)), c["looks"],
                 f"{nxt:%a %b} {nxt.day}, {nxt.year} ({turns})"])
story += [P("Master Age Ledger", h1),
          P("Ages as of the premiere, <b>Monday, January 5, 2026</b>. Marc-Anthony turns 34 "
            "on premiere day.", body),
          table(rows, [1.95 * inch, 1.2 * inch, 0.85 * inch, 0.8 * inch, 1.7 * inch]),
          PageBreak()]

# ---------------- CHARACTER PROFILES ----------------
CODES = dict(zip((c["name"] for c in CHARACTERS),
                 ["VD", "JD", "AL", "TD", "JO", "PO", "MO", "ML", "RB", "NB", "EL", "MA",
                  "GR", "AM", "AR", "ES", "HD", "JJ", "EM", "VI", "LY"]))
assert len(CODES) == len(CHARACTERS)
for c in CHARACTERS:
    if "family" in c:
        story.append(P(c["family"], h1))
    head = [P(c["name"], h2),
            P(f"<b>Born:</b> {long_date(c['born'])} • <b>Age:</b> {age_on(c['born'])} "
              f"• <b>Looks:</b> {c['looks']}"),
            P(f"<b>Title:</b> {c['title']}"),
            P(f"<b>Ties:</b> {c['ties']}"),
            P(f"<b>Political party:</b> {PARTY[CODES[c['name']]]}"),
            P(c["who"])]
    story.append(KeepTogether(head))
    story.append(P("<b>Backstory</b>"))
    story += bullets(c["back"])
    if "dream" in c:
        story.append(P(f"<b>The Dream:</b> {c['dream']}"))
    if c.get("politics"):
        story.append(P("<b>Politics (SECRET 2028 PRESIDENTIAL AMBITION)</b>"))
        story.append(P("A Democrat with Republican values who believes in bipartisanship. "
                       "He secretly wants to run for President in the 2028 election; he'd "
                       "be 36 on Inauguration Day, January 20, 2029, so he's eligible. "
                       "The things he believes in and will 100% accomplish, zero questions "
                       "asked:"))
        story += bullets(MARC_PLATFORM)
        story.append(P(f"<b>Long-term goal:</b> {MARC_LONG_TERM}"))
    story.append(P("<b>Secrets &amp; Story Engines</b>"))
    story += bullets(c["secrets"])
    who, line = c["voice"]
    story += scene("IN THEIR OWN WORDS", [(who, line)])
    story.append(Spacer(1, 8))

# ---------------- TIMELINE ----------------
timeline = [
    ("Fri, Mar 3, 1916", "Alexander Donohue born, Auburn Avenue, Atlanta."),
    ("Sun, Sep 12, 1920", "Simone Batiste born, New Orleans."),
    ("Mon, Apr 3, 1939", "Alexander Donohue founds <i>The Atlanta Beacon</i>, the seed of "
                          "The Donohue Company."),
    ("Mon, Jul 31, 1944", "Theodore Donohue born."),
    ("Thu, May 30, 1946", "Victor Donohue born."),
    ("Sat, Apr 17, 1948", "Joan Mercer born, Macon, GA."),
    ("Sat, May 17, 1958", "Alexander &amp; Simone found Belmont Crest."),
    ("Sat, Jun 17, 1961", "Belmont Crest Country Club opens."),
    ("Mon, Feb 10, 1969", "Robert Bullock born."),
    ("Sat, Jun 14, 1969", "Victor marries Joan Mercer."),
    ("Thu, Nov 13, 1969", "Peter Olson born."),
    ("Mon, Mar 23, 1970", "Jasmine Donohue born."),
    ("Wed, Jun 2, 1971", "Natasha Donohue born."),
    ("Mon, Jan 5, 1976", "Victor named CEO over Theodore."),
    ("Wed, Oct 8, 1980", "Alvin Donohue born."),
    ("1981", "Theodore becomes Fulton County DA (serves through 1996)."),
    ("Sat, Jun 16, 1990", "Jasmine marries Peter Olson."),
    ("Wed, Aug 29, 1990", "Elxa Bullock born (before her parents marry)."),
    ("Sun, Dec 2, 1990", "Jeremy Jackson born."),
    ("Wed, May 15, 1991", "Martin Olson born."),
    ("Sat, Jun 22, 1991", "Natasha marries Robert Bullock."),
    ("Sun, Jan 5, 1992", "Marc-Anthony Bullock born."),
    ("Mon, Feb 10, 1992", "Amond Baker born."),
    ("Fri, Jun 19, 1992", "Harmony Divine born."),
    ("Sun, Sep 20, 1992", "Esther Smilley born."),
    ("Sun, Oct 25, 1992", "Arianna Cummings born."),
    ("Tue, Apr 12, 1994", "Grace Bullock born."),
    ("Wed, Mar 1, 1995", "Bullock &amp; Associates, LLP opens."),
    ("Mon, Jun 5, 1995", "Mallory Olson born, the “miracle child.”"),
    ("Jan 1997", "Jasmine sworn into Congress at 26."),
    ("1998", "Marc-Anthony's screen debut at 6."),
    ("2003", "Esther &amp; Harmony meet in 6th grade at Westbrook Academy."),
    ("Sat, Dec 25, 2004", "Victor toasts Marc as heir; Martin pushes Marc down the stairs."),
    ("Mon, Jan 9, 2006", "Alexander dies at 89. Victor becomes Chairman; Natasha becomes CEO."),
    ("2010 (summer)", "Baker family business destroyed; Marc takes the conspirators apart."),
    ("Sat, Sep 18, 2010", "Marc-Anthony, 18, founds The Blackwater Syndicate (SECRET)."),
    ("Sat, Sep 3, 2011", "Lake Lanier Labor Day party: Marc (19) &amp; Esther (18)."),
    ("Mon, Oct 3, 2011", "Marc-Anthony, 19, founds Blackwater Security International (BSI)."),
    ("Fri, Apr 20, 2012", "Lyric Solace Baker born; Marc named godfather."),
    ("Thu, May 10, 2012", "Emma &amp; Victoria Smilley born; IVF cover story begins."),
    ("Sat, Nov 22, 2014", "Simone Donohue dies at 94."),
    ("Sun, Sep 18, 2016", "Marc wins his Emmy."),
    ("Sun, Jun 10, 2018", "Marc nominated for a Tony; loses."),
    ("Sun, Feb 10, 2019", "Marc wins his Grammy (Amond's 27th birthday)."),
    ("Jan 2021", "Arianna sworn in as Fulton County DA."),
    ("Fri, Feb 12, 2021", "Sealed court order gives Marc temporary custody of Lyric."),
    ("Mon, Jun 6, 2022", "Lyric begins her first professional shoot."),
    ("Sun, Mar 12, 2023", "Marc wins his Oscar. One Tony short of an EGOT."),
    ("Sat, Jun 15, 2024", "Elxa marries Jeremy Jackson."),
    ("Mon, Mar 17, 2025", "Arianna appointed Georgia Attorney General."),
    ("Tue, Sep 2, 2025", "Elxa sworn in as APD Chief of Police."),
    ("<b>Mon, Jan 5, 2026</b>", "<b>SERIES PREMIERE, Episode #0001. Marc-Anthony's 34th "
                                "birthday.</b>"),
]
story += [PageBreak(), P("Master Backstory Timeline", h1),
          table([["Date", "Event"]] + [list(t) for t in timeline],
                [1.5 * inch, 5.0 * inch])]

# ---------------- WHO KNOWS WHAT ----------------
story += [P("Secrets Ledger: Who Knows What (as of 1/5/2026)", h1),
          table([
              ["Secret", "Knows", "Does NOT know"],
              ["Marc-Anthony runs Blackwater", "Marc, the Table (incl. Amond), Arianna (no details), Grace",
               "Everyone else, including Elxa. Jeremy is hunting it. Natasha suspects."],
              ["Marc is Emma &amp; Victoria's father", "Esther",
               "Marc, the twins, the Smilleys, the Donohues. (Harmony and Loretta have figured it out and said nothing.)"],
              ["Why Marc has custody of Lyric", "Sealed; Amond &amp; Harmony know",
               "Marc, and everyone else"],
              ["Arianna's buried skeletons", "Arianna, Marc", "Everyone else"],
              ["Why Jeremy avoids the children talk", "Jeremy", "Elxa, everyone else"],
              ["Martin's staircase push (2004)", "Martin, Marc", "Officially an accident"],
          ], [2.0 * inch, 2.0 * inch, 2.5 * inch]),
          ]

# ---------------- CONTINUITY FIXES / OPEN QUESTIONS ----------------
story += [P("Continuity Fixes Applied", h1),
          *bullets([
              "Jeremy Jackson's marriage year was listed as 2004. Locked as <b>2024</b> to "
              "match Elxa's profile. In 2004 they were both 13.",
              "“Natasha Donahue” is spelled <b>Donohue</b> throughout.",
              "Mallory is the daughter of Peter and Jasmine <b>Olson</b> (née Donohue).",
              "Elxa was born August 1990 and her parents married June 1991. Confirmed by "
              "the showrunner: Elxa was born before the wedding, and it's a story point.",
          ]),
          P("Approved by the Showrunner", h1),
          *bullets([
              "<b>\u201cUncle Marc.\u201d</b> The twins know Marc through Lyric and he "
              "spoils them endlessly without knowing why he feels so connected to them.",
              "<b>Harmony knows about the twins</b>, and has never told Esther she knows.",
              "<b>The Smilley family</b> is fully built out in Document 06.",
              "<b>Grace &amp; Mallory's business</b> is HEIRLOOM, a luxury beauty &amp; "
              "wellness brand in direct competition with Smilley Beauty.",
              "<b>Lyric's custody.</b> The sealed order came out of a 2021 crisis that Amond "
              "and Harmony swore never to tell. The hidden layer underneath: Harmony wanted "
              "the twins near their real father. It stays sealed through Season 1 and is "
              "teased for Season 2.",
          ]),
          ]

build(OUT, story, "Beyond the Crest — Character Bible",
      "BEYOND THE CREST — Character Bible — Writers' Room Confidential")
