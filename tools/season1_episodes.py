"""Beyond the Crest, Season 1 episode guide data (Episodes #0001-#0170).

Each entry: (event, story_date_note, synopsis, cast_codes)
  event            True for standalone-leaning event episodes (the 10%)
  story_date_note  None when the story date is the air date
Air dates are assigned from the broadcast calendar in season1_calendar().
"""
import datetime as dt

DARK_DAYS = {
    dt.date(2026, 3, 19): "Pre-empted: NCAA Tournament",
    dt.date(2026, 3, 20): "Pre-empted: NCAA Tournament",
    dt.date(2026, 4, 3): "Pre-empted: network special",
    dt.date(2026, 5, 25): "Encore: Memorial Day",
    dt.date(2026, 7, 3): "Encore: Independence Day (observed)",
}


def season1_calendar():
    days, d = [], dt.date(2026, 1, 5)
    while d <= dt.date(2026, 9, 4):
        if d.weekday() < 5 and d not in DARK_DAYS:
            days.append(d)
        d += dt.timedelta(days=1)
    return days


EPISODES = [
    # ---------- WEEK 1 ----------
    (True, None,
     "6:10 AM: a body surfaces in the Chattahoochee by the Paces Ferry Road bridge; "
     "Det. Jeremy Jackson catches it as his wife, Chief Elxa Jackson, arrives. 8:00 PM: "
     "Marc-Anthony's 34th birthday gala at Summit House. Victor unveils the Succession "
     "Covenant and names Marc President &amp; COO of The Donohue Company, effective "
     "immediately. Martin's champagne glass shatters in his hand. Across the ridge, Esther "
     "watches the livestream in the dark. Final beat: Harmony, alone at her laptop, hits "
     "“publish” as <i>The Tea Kettle ATL</i>.",
     "MA VD JD NB RB JO PO EL JJ GR MO ML AM AR ES HD LY RD WO TB"),
    (False, None,
     "The victim is Terrence “T-Bone” Gaines. His burner holds one contact: "
     "“ARCHITECT.” Jasmine storms into Victor's study over the Covenant. At "
     "Westbrook, the twins spot the open casting call for Marc's movie musical "
     "<i>Crowns</i>. Emma: “Mom will never allow it.” Victoria: “Mom won't "
     "know.”",
     "JJ EL RD JO VD JD EM VI LY ES MO NB PO TR"),
    (False, None,
     "Smilley Plaza: Leonard reveals that the Crown License, the Donohue deal behind 41% "
     "of Smilley revenue, expires August 31. Donohue won't auto-renew, and Marc will run "
     "the talks. Gus names Esther lead negotiator. She goes pale. Flashback: at 2:00 AM on "
     "January 4, Peter stitches Martin's split knuckles and asks no questions.",
     "LE GS LO CE NA CA DS DO ES PO MO JO DE"),
    (False, None,
     "Marc's first day as President: he charms 4,000 employees and fires a VP for mocking "
     "an intern. Kane briefs him in the car: T-Bone was Blackwater, and he'd been selling "
     "secrets. To whom? Marc's smile vanishes. Amond: “Jeremy's on it.”",
     "MA KM AM NB EH NS GR PR MO EL"),
    (False, None,
     "At the Club, Arianna tells Marc and Amond she'll form a 2028 exploratory committee "
     "after the midterms. Journee Holloway pitches “Who Is Arianna Cummings?” "
     "Friday hook: Jeremy traces ARCHITECT's burner to a cell tower inside Belmont "
     "Crest.",
     "AR MA AM JH JJ EL MF RD HD GR"),
    # ---------- WEEK 2 ----------
    (False, None,
     "Esther dodges the first negotiation and sends Camille and Dorian instead. Marc: "
     "“Tell Ms. Smilley I don't negotiate with understudies.” Grace and Mallory "
     "toast HEIRLOOM, their beauty brand launching June 5.",
     "ES CA DO MA NB GR ML CE LE EH PO"),
    (False, None,
     "Elxa asks Jeremy to keep the Belmont Crest tower ping quiet: “Those are my "
     "neighbors. My family.” Jeremy logs it anyway. Victoria forges Esther's "
     "signature on the <i>Crowns</i> consent form, and Emma films the audition in their "
     "closet.",
     "EL JJ WJ VI EM LY TR RD ES CE"),
    (False, None,
     "Over bourbon, Martin offers Amond the presidency of Donohue Records “when I'm "
     "heir.” Amond laughs it off, then can't sleep. Harmony's film <i>Cascade</i> "
     "gets its 41st rejection. Kettle posts: “Which new COO fired a VP before "
     "lunch?”",
     "MO AM HD BK MA GR CD LD"),
    (False, None,
     "Victor gives Marc the key to Alexander's 1939 printing press. Joan warns him: "
     "“Your cousin wants to feel the crown's weight on your neck.” Natasha and "
     "Jasmine's war goes public at the Foundation board.",
     "VD JD MA NB JO PR WO RB PO ML"),
    (False, None,
     "Leonard orders Esther to meet Marc face to face or lose the lead. Friday hook: Marc "
     "opens the <i>Crowns</i> audition tapes and freezes on two girls who move, sing, and "
     "laugh exactly like him.",
     "LE ES GS CE MA LY PW EM VI NA CA"),
    # ---------- WEEK 3 ----------
    (True, "MLK Day flashback to Sat, May 17, 1958",
     "“1958.” Alexander and Simone buy the ridge through a white lawyer, Harlan "
     "Whitfield. Thirteen-year-old Theodore and eleven-year-old Victor watch the first gate "
     "go up, and Otis Smilley is fired from the Beacon while his son Gus watches. In the "
     "present, Joan reads Simone's diary to Lyric and the twins.",
     "JD LY EM VI YA YS YV YT YG OS HW WO"),
    (False, None,
     "State Sen. Marcus Pryor launches the first primary challenge to Jasmine in 29 years. "
     "Marc calls the twins back for a second audition. Victoria panics, because Mom still "
     "doesn't know.",
     "MP JO PO ML MA EM VI LY MO BK"),
    (False, None,
     "The callback at Donohue Pictures: Marc and the twins improvise a scene that leaves "
     "the casting room in tears. Kettle posts a blurry photo: “Golden Boy's mystery "
     "minis?” Esther sees it.",
     "MA EM VI LY GR ES HD AM PW"),
    (False, None,
     "Esther storms Westbrook, where Dr. Albright confirms the forgery. Esther pulls the "
     "girls, until Leonard sees the leverage: Smilley girls in a Donohue film during the "
     "negotiations. Journee publishes Part 1 of her Arianna series.",
     "ES AB EM VI LE CE JH AR GS EV"),
    (False, None,
     "Jeremy arrests Deuce Whitaker for the Gaines murder after an eyewitness places him "
     "at the river. Friday hook: Robert Bullock walks into APD. “I represent Mr. "
     "Whitaker.” Elxa: “Daddy?”",
     "JJ RD DX EL RB KM MA WJ"),
    # ---------- WEEK 4 ----------
    (False, None,
     "Marc orders Blackwater to protect Deuce and find T-Bone's real killer. Robert and "
     "Elxa's family dinner goes nuclear, and Natasha mediates holding a steak knife.",
     "MA EH KM AM RB EL NB GR JJ NS"),
    (False, None,
     "Esther and Marc get trapped in a stalled Donohue Tower elevator. He doesn't know "
     "who she is, and she won't tell him. After 47 minutes of sparks, she walks out without "
     "giving her name.",
     "MA ES GR CA NB KM"),
    (False, None,
     "Marc asks Nova to find the woman from the elevator. Nova: “That was Esther "
     "Smilley.” Marc laughs until he cries. Esther tells Harmony nothing, but Harmony "
     "sees her hands shaking.",
     "MA NS ES HD AM KM LY"),
    (False, None,
     "Mallory meets a charming designer at a fashion showcase who conveniently leaves out "
     "his last name. Martin buys T-Bone's old storage unit through a shell company.",
     "ML DS GR MO BK DE"),
    (False, None,
     "Arianna warns Marc that Journee is asking about 2021. Friday hook: Julian Cummings, "
     "three years sober, sees Journee's byline next to a photo of her father.",
     "AR MA JU JH HC EC AM"),
    # ---------- WEEK 5 ----------
    (False, None,
     "Westbrook's Black History Month “Roots Project”: Mr. Lane assigns "
     "Smilley-sponsored RootsKit DNA tests. Trey brags about his great-grandfather. Lyric "
     "and the twins spit into their tubes.",
     "EV EM VI LY TR JC NA AB ES"),
    (False, None,
     "At the Smilley board meeting, Nathaniel pushes to sue Donohue and Esther shuts him "
     "down. Camille smiles at her brother, and an alliance is born. Victor to Marc: "
     "“Smilleys bite when they're cornered.”",
     "NA ES CA DO LE GS VD MA NB CE"),
    (False, None,
     "Jasmine traces Pryor's super PAC money to a Delaware shell. Peter tries to tell her "
     "he's worried about Martin, and she refuses to hear it.",
     "JO PO MO MP ML"),
    (False, None,
     "Marc officially casts Emma, Victoria, and Lyric in <i>Crowns</i>. Joan invites the "
     "twins to tea at Summit House, and Esther declines on their behalf.",
     "MA EM VI LY JD ES PW GR"),
    (False, None,
     "Amond and Harmony are back on, until she catches him at Martin's club. Friday hook: "
     "a text reaches Martin from a blocked number: “THE OLD MAN SAYS: "
     "PATIENCE.”",
     "AM HD MO BK MF MA"),
    # ---------- WEEK 6 ----------
    (False, None,
     "The morning after the Super Bowl, Robert bets Gerald Baker a Bentley at the Club. "
     "At Deuce's bond hearing, Judge Okoye denies bail.",
     "RB GB MF DX JK JJ EL AM MA"),
    (False, None,
     "Double birthday: Robert turns 57 and Amond turns 34. Marc gives Amond a Rolls-Royce. "
     "Martin sends Amond a Donohue Records key card.",
     "RB AM MA NB GR EL HD MO YB GB JJ"),
    (False, None,
     "At a grief support group, Journee meets a gentle man named Julian who doesn't "
     "mention his last name is Cummings.",
     "JH JU AR EC HC"),
    (False, None,
     "Mallory learns her designer is Desmond Smilley. “You're a <i>what</i>?” "
     "Desmond: “Same thing you are. Somebody's grandbaby.”",
     "ML DS GR DE PO"),
    (False, None,
     "The official negotiation: Esther finally sits across from Marc. “We've "
     "met.” “We haven't.” Friday hook: she slides over a counteroffer, and "
     "her perfume stops Marc cold. A memory flashes: a gold dress, Lake Lanier.",
     "MA ES NB LE CA DO EH KM"),
    # ---------- WEEK 7 ----------
    (True, "Sat, Feb 14",
     "The Belmont Crest Valentine's Ball. Esther comes as Harmony's plus-one, and Lucinda "
     "tries to eject a Smilley before Joan overrules her. Marc and Esther's dance ends in "
     "an insult and a slap.",
     "MA ES HD AM JD VD NB RB GR AR LG MF ML DS EL JJ"),
    (False, None,
     "The slap goes viral. Kettle: “Crest Crashers.” Leonard is thrilled and "
     "Natasha isn't. Elxa asks Jeremy about kids, and he says “after the Gaines "
     "case.”",
     "ES MA LE NB EL JJ HD CE GR"),
    (False, None,
     "Journee finds that the DA's office closed her father's 2021 hit-and-run file in "
     "eleven days. At 2:00 AM, Arianna calls Marc.",
     "JH AR MA HC JU"),
    (False, None,
     "In New York, Marc starts rehearsals for the Broadway revival of <i>Sweet "
     "Chariot</i>, the role his grandfather originated in 1972. Co-star Nia Vaughn flirts "
     "and Grace rolls her eyes.",
     "MA SC NV GR IV VD KM"),
    (False, None,
     "Martin's storage unit yields T-Bone's second phone. Friday hook: a voice memo. "
     "T-Bone: “The Architect lives on the ridge.” Martin smiles.",
     "MO BK JO"),
    # ---------- WEEK 8 ----------
    (False, None,
     "Jeremy subpoenas BSI's records. Gen. Whitmore stonewalls, and Elxa quietly stalls "
     "the subpoena “pending review.”",
     "JJ CW EL RD EH MA"),
    (False, None,
     "The RootsKit samples reach the lab. Nathaniel gets automatic alerts on every "
     "family-linked account, the twins' included.",
     "NA MQ TR RT CA"),
    (False, None,
     "Amond meets Martin in secret. Martin offers him the world for one name: who Marc "
     "really is. Amond walks out. Or does he?",
     "AM MO BK MF"),
    (False, None,
     "Victor coaches Marc over FaceTime. Joan finds a 1966 love letter tucked in an old "
     "Broadway program, signed “Gus.”",
     "VD JD MA WO PR NB"),
    (False, None,
     "Jasmine confronts Leonard at a fundraiser. Friday hook: “Your father took "
     "everything from mine,” Leonard says. “I'm taking your seat.”",
     "JO LE PO CE MP ML"),
    # ---------- WEEK 9 ----------
    (False, None,
     "<i>Sweet Chariot</i> previews open on Broadway. Marc brings Lyric and, with "
     "Harmony's help, the twins. Esther thinks they're on a school trip.",
     "MA LY EM VI HD SC NV GR IV KM"),
    (False, None,
     "Esther finds out and flies to New York. At the stage door, she and Marc have their "
     "biggest fight yet, followed by their first real laugh.",
     "ES MA EM VI LY HD GR"),
    (False, None,
     "At Deuce's preliminary hearing, Robert shreds Jeremy's chain of custody. Elxa "
     "watches her father beat her husband.",
     "RB JJ EL DX JK RD WJ"),
    (False, None,
     "Grace and Kane share a late-night kiss in a BSI garage. They agree it never "
     "happened.",
     "GR KM MA NS"),
    (False, None,
     "Julian and Journee's first date. Friday hook: Arianna sees them together.",
     "JU JH AR MA"),
    # ---------- WEEK 10 ----------
    (False, None,
     "Arianna begs Julian to end it, and he refuses. Marc to Arianna: “Tell the "
     "truth before someone else does.”",
     "AR JU MA HC EC"),
    (False, None,
     "Natasha's Oscar campaign peaks. Jasmine publicly skips her sister's pre-Oscar "
     "party.",
     "NB JO RB VD JD GR BK PO MO"),
    (False, None,
     "HEIRLOOM's formula samples vanish from the lab. Mallory suspects Desmond.",
     "ML GR DS CA DE"),
    (False, None,
     "Second round of talks: Esther outmaneuvers Marc and he loves every second. Victoria "
     "spies from the conference room door.",
     "MA ES VI EM NB CA LY"),
    (False, None,
     "The Donohues fly to Los Angeles. Friday hook: the night before the Oscars, Martin "
     "plants a story accusing Natasha's director of bribery.",
     "NB MO BK RB VD JD MA GR"),
    # ---------- WEEK 11 ----------
    (True, "Sun, Mar 15",
     "The Academy Awards. Natasha wins Best Actress and completes her EGOT. Victor weeps. "
     "At the after-party, Marc crashes out on the reporter who asked his mother about the "
     "bribery smear.",
     "NB VD JD RB MA GR EL JO PO BK MO ES KM"),
    (False, None,
     "Headlines: “EGOT QUEEN” and “GOLDEN BOY GONE WILD.” Marc's "
     "apology video somehow makes it funnier. Martin fumes.",
     "MA NB MO GR PR JD AM HD"),
    (False, None,
     "The RootsKit results post. Victoria reads hers first. Relative match: Grace Bullock, "
     "“close family: aunt or half-sibling.”",
     "VI EM LY TR"),
    # ---------- WEEK 12 ----------
    (False, None,
     "Jasmine's 56th birthday: Pryor debates her on DBC. She wins, but his "
     "“Donohue dynasty” jab lands. The twins work it out: Grace's brother is "
     "Marc.",
     "JO PO ML MP BK EM VI LY MO"),
    (False, None,
     "“Operation Daddy” begins. Lyric steals a hair from Marc's brush.",
     "LY EM VI PW MA AM"),
    (False, None,
     "Nathaniel sees the internal flag: Esther's twins match Grace Bullock. He sits in the "
     "dark and laughs.",
     "NA MQ CA RT"),
    (True, None,
     "Opening night of <i>Sweet Chariot</i> on Broadway. Raves. Esther sits in the last "
     "row, and Marc spots her from the stage.",
     "MA ES GR NB VD JD SC NV IV HD AM RB"),
    (False, None,
     "Nathaniel and Martin meet, and “the Spare Alliance” is born. Friday "
     "hook: Nathaniel shows Martin the DNA match. Martin: “Merry Christmas.”",
     "NA MO CA DO BK"),
    # ---------- WEEK 13 ----------
    (False, None,
     "Elxa finds payments from BSI-linked shells to Bullock &amp; Associates, and starts "
     "to suspect her own father is “The Architect.”",
     "EL RB RD JJ NB"),
    (False, "Flashback to Sun, Jan 4, 11:40 PM",
     "The audience learns the truth: under the Paces Ferry Road bridge, Martin Olson kills "
     "T-Bone Gaines with his bare hands. Back in the present, he sends Peter a fruit "
     "basket.",
     "MO TB PO JO"),
    (False, None,
     "Kettle's April Fools post backfires into a real tip about Pryor's affair. Jasmine "
     "files it away.",
     "HD JO MP AM PO"),
    (False, None,
     "The twins mail Marc's hair to RootsKit under a fake name. Emma: “What if we're "
     "wrong?” Victoria: “We're never wrong. Genetically.”",
     "EM VI LY TR JC"),
    # ---------- WEEK 14 ----------
    (True, "Sun, Apr 5",
     "Easter at Summit House: Joan's egg hunt, Victor's sunrise toast, and a Jasmine–Natasha "
     "truce that lasts nine minutes.",
     "VD JD NB RB JO PO MA EL JJ GR MO ML LY WO"),
    (False, None,
     "Peter confronts Martin about the knuckles. Martin: “You stitched them, Dad. "
     "That makes you part of it.”",
     "PO MO ML JO"),
    (False, None,
     "The negotiation moves to a private dinner. Nobody eats.",
     "MA ES NS KM HD"),
    (False, None,
     "Jeremy's theory: BSI is a front for the ghost network. Elxa: “That's my "
     "brother's company.”",
     "JJ EL RD FB MA"),
    (False, None,
     "FBI Special Agent in Charge Nadia Brooks offers Jeremy a joint task force. Friday "
     "hook: he says yes without telling Elxa.",
     "JJ FB RD WJ"),
    # ---------- WEEK 15 ----------
    (False, "Sun, Apr 12",
     "Grace's 32nd birthday on a yacht on Lake Lanier. Kane in a tux, and Marc notices.",
     "GR KM MA ML AM AR HD NB RB EL"),
    (False, None,
     "Camille frames Desmond for stealing HEIRLOOM's formulas, and Mallory ends it with "
     "him.",
     "CA DS ML GR DE LE"),
    (False, None,
     "Journee's Part 3 names the prosecutor who closed the 2021 file. Arianna's poll "
     "numbers wobble.",
     "JH AR JU MA HC"),
    (False, None,
     "Harmony's film finally gets funded, by a mysterious investor: Nathaniel Smilley.",
     "HD NA AM ES CD LD"),
    (False, None,
     "Jeremy finally tells Elxa why he won't talk about kids. His mother died of "
     "Huntington's disease and he has a 50% chance of carrying it. He's never been tested. "
     "Friday hook: “And I never will be.”",
     "JJ EL WJ"),
    # ---------- WEEK 16 ----------
    (False, None,
     "Lyric's 14th birthday at Marc's. The twins give Marc a framed photo of the three of "
     "them, captioned “Family.”",
     "LY EM VI MA AM HD PW GR TR JC"),
    (False, None,
     "Elxa begs Jeremy to get tested. Walter to his son: “Your mother would've "
     "wanted grandbabies.”",
     "EL JJ WJ GR"),
    (False, None,
     "The second RootsKit result arrives: parent/child match, 99.98%. The twins scream "
     "into their pillows.",
     "EM VI LY"),
    (False, None,
     "Nathaniel makes Harmony's funding conditional on her sharing Esther's secrets. "
     "Harmony refuses.",
     "NA HD ES AM"),
    (False, None,
     "Marc overrules Amond at a meeting of the Blackwater Table. Friday hook: Amond calls "
     "Martin.",
     "MA AM EH KM NS QM IV CB CO LF"),
    # ---------- WEEK 17 ----------
    (False, None,
     "Arianna asks Marc to make Journee “go away.” Marc: “No. She's the "
     "only innocent person in this.”",
     "AR MA JH JU"),
    (False, None,
     "Joan confronts Gus at a charity auction. Loretta watches them with the eyes of a "
     "woman who has always known.",
     "JD GS LO LG VD CE PR"),
    (False, None,
     "The Smilleys apply to the Belmont Crest Country Club, 64 years after Otis was turned "
     "away. Lucinda sets the vote for July 24.",
     "GS LE LO CE LG JD VD ES"),
    (False, None,
     "Robert discovers the eyewitness who put Deuce at the river was paid, through a "
     "shell. Jeremy is stunned.",
     "RB DX JJ RD EL"),
    (False, None,
     "Victoria confronts Esther: “Who's our father?” Esther: “No "
     "one.” Friday hook: Victoria: “Wrong answer.”",
     "VI EM ES CE"),
    # ---------- WEEK 18 ----------
    (False, None,
     "The negotiations collapse with 119 days to go, and the media war begins.",
     "MA ES NB LE CA DO BK"),
    (False, None,
     "Tony nominations: <i>Sweet Chariot</i> earns 11, including Best Leading Actor in a "
     "Musical for Marc. EGOT watch begins.",
     "MA NB VD JD GR NV SC RB"),
    (False, None,
     "ALVIN DONOHUE COMES HOME. A helicopter lands on the Summit House lawn at dawn. "
     "“Did somebody say party?” Joan cries. Victor doesn't.",
     "AL VD JD NB JO MA GR EL CL WO"),
    (False, None,
     "Alvin charms the whole family, then meets Vincent Morrow in a Buford Highway karaoke "
     "bar.",
     "AL VM MA AM KM"),
    (False, None,
     "Alvin tells Jasmine he can fix her primary. Friday hook: Martin and Alvin shake "
     "hands.",
     "AL JO MO PO"),
    # ---------- WEEK 19 ----------
    (True, "Sun, May 10",
     "Mother's Day and the twins' 14th birthday in Tuxedo Park. The twins have invited "
     "“Uncle Marc,” and he arrives with Lyric and a 14-foot cake. Esther and Marc "
     "face off in the garden and almost kiss.",
     "EM VI ES MA LY CE LE GS LO HD TR NA MQ"),
    (False, None,
     "Kettle posts the garden photos. Gus sees Marc with his great-granddaughters and "
     "smashes a glass.",
     "GS ES LE HD CA LO"),
    (False, None,
     "Elxa finds a Blackwater ledger page listing “R.B. — retainer.” She's "
     "sure it means her father.",
     "EL RB NB RD"),
    (False, None,
     "Elxa destroys the ledger page. It's the first time she has ever destroyed "
     "evidence.",
     "EL JJ RD WJ"),
    (False, None,
     "Martin hires Brielle to dig into the twins' birth records. Friday hook: Esther's IVF "
     "clinic has no record of her.",
     "MO BK ES NA"),
    # ---------- WEEK 20 ----------
    (False, None,
     "Primary eve: Alvin delivers Pryor's secrets, courtesy of Morrow.",
     "AL JO VM MP PO"),
    (False, None,
     "Georgia primary night: Jasmine 48.6%, Pryor 44.1%. She's forced into a June 16 "
     "runoff.",
     "JO PO ML MO MP AL VD NB BK"),
    (False, None,
     "Zion Reed, 21, walks into Alvin's club: “I think you're my father.”",
     "ZR AL CL MF"),
    (True, None,
     "8th-grade promotion at Westbrook. The twins' seating chart puts Marc and Esther side "
     "by side.",
     "EM VI LY TR JC AB EV MA ES AM HD NA MQ"),
    (False, None,
     "Victor tells Joan he'll name his successor as Chairman at his 80th. Friday hook: "
     "Joan: “Then I need to tell you about Gus.” Victor: “After the "
     "party.”",
     "VD JD WO PR"),
    # ---------- WEEK 21 ----------
    (False, None,
     "Deuce's trial is set for July. Robert asks Marc for BSI security footage, and "
     "father helps son without either knowing it.",
     "RB MA DX KM EL"),
    (False, None,
     "Over late-night waffles, Esther and Marc accidentally reach a breakthrough on the "
     "deal.",
     "MA ES KM"),
    (True, None,
     "Episode #0100, the eve of Victor's 80th. Every storyline converges at the Summit "
     "House rehearsal dinner, and Martin gives a toast that sounds like a threat.",
     "VD JD NB RB JO PO MA EL JJ GR MO ML AL AM AR LY WO PR"),
    (True, "Sat, May 30",
     "Victor Donohue's 80th birthday gala. He begins his announcement, “My successor "
     "as Chairman will be—” and collapses.",
     "VD JD NB RB JO PO MA EL JJ GR MO ML AL AM AR HD LY EC WO PR LG"),
    # ---------- WEEK 22 ----------
    (False, None,
     "Atlanta Metropolitan Medical Center: Dr. Evelyn Cummings operates on Victor while "
     "alliances in the waiting room shift by the hour.",
     "VD JD NB JO RB PO MA EL GR MO ML AL EC AR"),
    (False, None,
     "Natasha spends her 55th birthday in a hospital hallway. Victor pulls through. His "
     "first words: “Where's my announcement?”",
     "NB VD JD RB MA EL GR EC JO"),
    (False, None,
     "Alvin and Jasmine plot to challenge the Crown Voting Trust while Victor recovers.",
     "AL JO MO PO"),
    (False, None,
     "Esther visits Victor's hospital room alone. He knows exactly who she is: “Your "
     "girls have my grandson's eyes.”",
     "ES VD JD"),
    (True, None,
     "HEIRLOOM launches on Mallory's 31st birthday, and Smilley Beauty drops an identical "
     "line the same hour. Friday hook: Mallory sees Desmond on Smilley's launch "
     "livestream.",
     "ML GR DS CA NB PO JO BK DE"),
    # ---------- WEEK 23 ----------
    (True, "Sun, Jun 7",
     "The Tony Awards. Marc wins Best Leading Actor in a Musical and completes his EGOT at "
     "34. Victor watches from his hospital bed. Esther watches alone in Tuxedo Park, "
     "crying.",
     "MA GR NB RB VD JD LY EM VI ES NV SC IV AM"),
    (False, None,
     "EGOT headlines everywhere. Marc dedicates his Tony “to the family I'm going to "
     "have.” The twins look at each other.",
     "MA EM VI LY BK GR"),
    (False, None,
     "Jeremy's task force raids a BSI warehouse and finds it empty. Blackwater knew. "
     "Jeremy suspects the leak is his wife.",
     "JJ FB RD EL KM NS"),
    (False, None,
     "Peter runs Zion's DNA test: Alvin is his father. Alvin panics, then buys him a "
     "Lamborghini.",
     "ZR AL PO CL JD"),
    (False, None,
     "The FIFA World Cup kicks off, with BSI running security for Atlanta's matches. "
     "Friday hook: Morrow tells Alvin he wants the stadium security plans.",
     "MA CW KM VM AL NS"),
    # ---------- WEEK 24 ----------
    (False, None,
     "Runoff eve: Kettle breaks the story of Pryor's affair.",
     "HD JO MP AL AM"),
    (False, None,
     "Runoff: Jasmine wins 57 to 43. After her victory speech, Alvin whispers, “You "
     "owe Morrow now.”",
     "JO PO ML MO AL VM MP"),
    (False, None,
     "Desmond proves Camille framed him and quits Smilley Beauty. Mallory: “Prove "
     "it again. Slowly.”",
     "DS ML CA DE GR"),
    (False, None,
     "Amond buys an engagement ring, and Grace catches him.",
     "AM GR MA"),
    (True, None,
     "The Juneteenth Jubilee at the Club, on Harmony's 34th birthday. Amond proposes on "
     "the 18th green. She says yes, then vanishes.",
     "AM HD MA GR AR ES LY JD VD LG MF CD LD GB YB"),
    # ---------- WEEK 25 ----------
    (False, "Sun, Jun 21 (Father's Day)",
     "An anonymous card arrives at Marc's gate: “Happy Father's Day. From your "
     "daughters.” Marc laughs it off as a prank, then can't stop rereading it.",
     "MA PW LY AM RB"),
    (False, None,
     "<i>Crowns</i> starts filming in Atlanta. Esther sets up a chaise on set and doesn't "
     "leave.",
     "MA ES EM VI LY GR"),
    (False, None,
     "Harmony comes back. She ran because she's the Kettle and was terrified of being "
     "found out. The audience knows; Amond doesn't.",
     "HD AM CD LD"),
    (False, None,
     "Martin gets the forensic file proving Esther's IVF story is a fiction. He tells "
     "Nathaniel: “We wait for the Council.”",
     "MO NA BK"),
    (False, None,
     "Victor comes home to Summit House. Friday hook: Joan: “Now I tell you about "
     "Gus.”",
     "VD JD WO NB MA"),
    # ---------- WEEK 26 ----------
    (False, None,
     "Joan tells Victor about her 1966 romance with Gus in New York, and that Gus "
     "proposed. Victor: “And you said?” Joan: “Not yet.”",
     "VD JD"),
    (False, None,
     "Victor summons Gus to Summit House: two men in their eighties and a sixty-year "
     "grudge.",
     "VD GS JD LO WO"),
    (False, None,
     "The raid leak fractures Elxa and Jeremy's marriage.",
     "EL JJ WJ"),
    (False, None,
     "Grace and Kane: “nothing happened” happens again.",
     "GR KM"),
    # ---------- WEEK 27 ----------
    (True, "Sat, Jul 4",
     "Fourth of July fireworks over Belmont Crest's 18th fairway. Marc and Esther kiss, "
     "and Emma and Victoria see it.",
     "MA ES EM VI LY JD VD NB RB GR AM HD AR LG MF"),
    (False, None,
     "The twins debate telling Marc and Lyric says wait. Esther confesses the kiss to "
     "Harmony, who almost confesses what she knows.",
     "EM VI LY ES HD"),
    (False, None,
     "Deuce's trial begins. Jeremy testifies and Robert eviscerates him.",
     "RB JJ DX JK RD EL"),
    (False, None,
     "Julian tells Journee he loves her. Arianna launches her exploratory committee early "
     "to get ahead of the story.",
     "JU JH AR MA"),
    (False, None,
     "Alvin steals the stadium security plan from Marc's office. Friday hook: Nova sees him "
     "on camera.",
     "AL NS MA KM"),
    # ---------- WEEK 28 ----------
    (False, None,
     "Marc learns his uncle is feeding Morrow. He chooses to protect Alvin and set a "
     "trap.",
     "MA NS KM AM EH"),
    (False, None,
     "Semifinal eve. Jeremy's task force watches BSI.",
     "JJ FB MA CW RD EL"),
    (True, None,
     "The World Cup semifinal in Atlanta. Morrow's men move, and Blackwater stops them in "
     "the tunnels without anyone in the stands knowing. Jeremy finds zip-tied men and a "
     "black calling card.",
     "MA KM AM NS VM CW JJ EL FB AL GR LY EM VI"),
    (False, None,
     "Headlines hail the “BSI heroes.” Morrow knows it was Blackwater, and "
     "that Alvin was the bait.",
     "VM AL MA BK"),
    (False, None,
     "Robert calls a surprise witness. Friday hook: it's T-Bone's girlfriend, and she "
     "swears “the Architect” didn't kill him.",
     "RB DX JJ JK EL"),
    # ---------- WEEK 29 ----------
    (False, None,
     "Martin panics as the trial edges toward him.",
     "MO BK PO"),
    (False, None,
     "Peter tells Jasmine about Martin's knuckles. Jasmine: “You will never say that "
     "again.”",
     "PO JO ML"),
    (False, None,
     "Esther and Marc spend the night together at his lake house.",
     "MA ES"),
    (True, "Flashback to 1966",
     "“1966.” Young Joan stars on Broadway, young Gus proposes, and young "
     "Victor takes the midnight train to New York.",
     "JD GS YJ YG YV"),
    (False, None,
     "The Club votes on the Smilley application and it ties. Joan casts the deciding vote: "
     "yes. Victor walks out.",
     "JD VD LG GS LO LE CE ES NB RB"),
    # ---------- WEEK 30 ----------
    (False, None,
     "Gus sits in the Club lounge, 64 years late. Loretta: “Was it worth it?”",
     "GS LO JD MF"),
    (False, None,
     "Harmony's film <i>Cascade</i> starts shooting. Nathaniel names his price: Esther's "
     "secrets.",
     "HD NA ES AM"),
    (False, None,
     "Closing arguments in the Whitaker trial.",
     "RB JJ DX JK EL"),
    (False, None,
     "Arianna's aides find Julian's old car in a Blackwater-owned garage. Arianna realizes "
     "Marc still has the evidence.",
     "AR MA JU"),
    (False, None,
     "Verdict: NOT GUILTY. Friday hook: Robert looks at the man paying his fees and sees "
     "his son's bodyguard.",
     "RB DX JJ EL JK KM MA"),
    # ---------- WEEK 31 ----------
    (False, None,
     "Robert follows the money.",
     "RB CB MA"),
    (False, None,
     "Robert confronts Marc: “You're the Architect.” Marc: “Daddy, I'm an "
     "actor.” Robert: “Then act surprised when I say I'm proud of you.”",
     "RB MA NB"),
    (False, None,
     "Elxa and Jeremy separate.",
     "EL JJ WJ GR"),
    (False, None,
     "First day of 9th grade at Westbrook Upper School. Trey kisses Lyric, and Victoria "
     "punches Trey.",
     "EM VI LY TR JC AB ES MA NA"),
    (False, None,
     "<i>Crowns</i> wraps. Friday hook: Marc tells Esther he wants a family, with her.",
     "MA ES EM VI LY GR"),
    # ---------- WEEK 32 ----------
    (False, None,
     "Esther almost tells him. Instead: “Give me until Labor Day.”",
     "MA ES HD"),
    (False, None,
     "Kettle posts a blind item: “Which heiress's 'donor' twins look like a certain "
     "EGOT winner?” Harmony didn't post it. Her account was hacked.",
     "HD ES MO NS"),
    (False, None,
     "Esther traces the Kettle account to Harmony, and a 23-year friendship ends.",
     "ES HD AM"),
    (False, None,
     "Marc laughs off the blind item in public. In private, he asks Nova to find the "
     "hacker.",
     "MA NS AM"),
    (False, None,
     "Jeremy takes the Huntington's test. Friday hook: results in three weeks.",
     "JJ WJ RD"),
    # ---------- WEEK 33 ----------
    (False, None,
     "Nova traces the Kettle hack to Martin. Marc: “Of course.”",
     "MA NS KM AM"),
    (False, None,
     "Jasmine and Natasha have the sister fight thirty-five years in the making.",
     "JO NB VD JD"),
    (False, None,
     "Victor forgives Joan. Joan: “There's one more thing. About 1976.”",
     "VD JD"),
    (False, None,
     "Mallory tells Desmond she's ready, and together they decide to wait for their "
     "wedding night.",
     "ML DS GR"),
    (False, None,
     "Final terms of the Crown License. Friday hook: Marc offers Smilley a deal too "
     "generous to be business.",
     "MA ES NB LE CA DO"),
    # ---------- WEEK 34 ----------
    (False, None,
     "Esther realizes he's doing it for her.",
     "ES MA HD"),
    (False, None,
     "Journee finds Julian's name in her father's case file.",
     "JH JU AR"),
    (False, None,
     "The Smilley Family Council convenes. Nathaniel presents the RootsKit results.",
     "GS LO LE CE NA CA DO ES DE DS"),
    (False, None,
     "Gus invokes the Allegiance Clause.",
     "GS ES LE CE NA CA LO"),
    (False, None,
     "Esther is suspended as heir unless a DNA test clears her by Labor Day. Friday hook: "
     "“Then I'll tell him myself.”",
     "ES GS LE HD EM VI"),
    # ---------- WEEK 35 ----------
    (False, "Opens Sat, Aug 29 (Elxa's 36th)",
     "Elxa's 36th birthday. At 11:59 PM on August 31, Marc and Esther sign the Crown "
     "License.",
     "MA ES NB LE CA EL JJ GR"),
    (False, None,
     "The old man arrives: Theodore Donohue, 82, back in Atlanta. Martin: “Welcome "
     "home, Uncle Theodore.”",
     "TD MO JO BK"),
    (False, None,
     "Theodore's family descends on Atlanta: Lorraine, Xander, Celestine, Theo III, "
     "Sienna, and August. Victor: “He's here.”",
     "TD LC XD CP T3 SD AP VD JD MO"),
    (False, None,
     "Julian confesses to Journee.",
     "JU JH AR TD"),
    (True, "Fri, Sep 4, Lake Lanier",
     "SEASON FINALE. Labor Day weekend on Lake Lanier, fifteen years after the night. The "
     "twins tell Marc he's their father. Elxa sees Marc with Kane and finally understands. "
     "At Summit House, Theodore: “Hello, little brother.” Jeremy's test results "
     "sit unopened. A gunshot echoes across the lake.",
     "MA ES EM VI LY EL JJ KM GR AM HD AR TD VD JD NB RB MO NA"),
]

assert len(EPISODES) == 170, len(EPISODES)

# ---------------------------------------------------------------------------
# RUNNERS: recurring household/storyline scenes that keep every contract
# player in rotation (a D-story beat, a scene at home, a phone call), on a
# fixed weekday cadence. (codes, weekdays Mon=0..Fri=4, first_ep, last_ep)
# Standalone flashback episodes carry no runners.
# ---------------------------------------------------------------------------
RUNNERS = [
    ("VD JD", (0, 3), 1, 170),        # Summit House
    ("NB RB", (1, 3), 1, 170),        # Bullock household / Donohue Tower
    ("JO PO ML", (2, 4), 1, 170),     # Olson household / campaign
    ("MO", (0, 2), 1, 170),           # Martin's schemes
    ("EL JJ", (1, 4), 1, 170),        # APD / the Jackson marriage
    ("MA", (1, 2), 1, 170),           # the Golden Boy
    ("GR", (2,), 1, 170),
    ("ES", (0, 3), 1, 170),
    ("AM HD", (1, 3), 1, 170),
    ("AR", (0, 4), 1, 170),
    ("EM VI LY", (1, 4), 1, 170),     # the kids
    ("AL", (0, 2, 4), 85, 170),       # Alvin joins at the halfway mark
    ("LE CE", (2,), 1, 170),          # Smilley Plaza / Tuxedo Park
    ("NA CA", (3,), 1, 170),          # the Spare Alliance
    ("GS", (4,), 1, 170),
    ("KM", (0,), 1, 170),
    ("JH JU", (3,), 14, 170),
    ("DS", (1,), 19, 170),
]
NO_RUNNERS = {11, 60, 139}


def full_cast(ep_no):
    """Headline cast plus scheduled runner scenes for episode ep_no (1-based)."""
    event, note, synopsis, codes = EPISODES[ep_no - 1]
    cast = codes.split()
    if ep_no in NO_RUNNERS:
        return cast
    wd = season1_calendar()[ep_no - 1].weekday()
    for group, days, first, last in RUNNERS:
        if wd in days and first <= ep_no <= last:
            cast += [c for c in group.split() if c not in cast]
    return cast
