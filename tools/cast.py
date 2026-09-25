"""Master cast registry for Beyond the Crest.

Every character has a short code used by the episode guide, so appearance
counts are computed from the episodes themselves and never drift.
"""
import datetime as dt

D = dt.date

CORE = "Core / Contract Cast"
FEATURED = "Featured Contract Cast"
RECURRING = "Recurring"
SUPPORTING = "Supporting"
DAY = "Day Players"
GUEST = "Guest Stars"
CATEGORIES = [CORE, FEATURED, RECURRING, SUPPORTING, DAY, GUEST]

# code: (name, born, died, category, group, role)
CAST = {
    # ---------------- CORE / CONTRACT ----------------
    "VD": ("Victor Donohue", D(1946, 5, 30), None, CORE, "Donohue",
           "Chairman, The Donohue Company"),
    "JD": ("Joan Donohue", D(1948, 4, 17), None, CORE, "Donohue",
           "Philanthropist; Chair, The Donohue Foundation"),
    "NB": ("Natasha Bullock", D(1971, 6, 2), None, CORE, "Bullock",
           "CEO, The Donohue Company"),
    "JO": ("Jasmine Olson", D(1970, 3, 23), None, CORE, "Olson",
           "U.S. Representative for Georgia"),
    "AL": ("Alvin Donohue", D(1980, 10, 8), None, CORE, "Donohue",
           "Party boy, fixer, underworld-connected (joins at Ep #0085)"),
    "RB": ("Robert Bullock", D(1969, 2, 10), None, CORE, "Bullock",
           "Founder, Bullock & Associates, LLP"),
    "PO": ("Dr. Peter Olson", D(1969, 11, 13), None, CORE, "Olson",
           "Chief of Plastic Surgery"),
    "MA": ("Marc-Anthony Bullock", D(1992, 1, 5), None, CORE, "Bullock",
           "Heir Apparent; President & COO; SECRET Boss of Blackwater"),
    "EL": ("Elxa Jackson", D(1990, 8, 29), None, CORE, "Bullock",
           "Chief of Police, APD"),
    "GR": ("Grace Bullock", D(1994, 4, 12), None, CORE, "Bullock",
           "Actress & singer; co-founder, HEIRLOOM"),
    "MO": ("Martin Olson", D(1991, 5, 15), None, CORE, "Olson",
           "President, Donohue Broadcasting Group"),
    "ML": ("Mallory Olson", D(1995, 6, 5), None, CORE, "Olson",
           "Office manager; co-founder, HEIRLOOM"),
    "ES": ("Esther Smilley", D(1992, 9, 20), None, CORE, "Smilley",
           "President & COO, Smilley Corporation; designated heir"),
    "AM": ("Amond Baker", D(1992, 2, 10), None, CORE, "The Circle",
           "Marc's best friend; SECRET Underboss, Blackwater"),
    "AR": ("Arianna Cummings", D(1992, 10, 25), None, CORE, "The Circle",
           "Attorney General of Georgia"),
    "HD": ("Harmony Divine", D(1992, 6, 19), None, CORE, "The Circle",
           "Aspiring filmmaker; SECRETLY “The Tea Kettle ATL”"),
    "JJ": ("Det. Jeremy Jackson", D(1990, 12, 2), None, CORE, "APD",
           "Senior Detective, APD Homicide"),
    "EM": ("Emma Smilley", D(2012, 5, 10), None, CORE, "Smilley",
           "Elder twin; Marc's secret daughter"),
    "VI": ("Victoria Smilley", D(2012, 5, 10), None, CORE, "Smilley",
           "Younger twin; Marc's secret daughter"),
    "LY": ("Lyric Solace Baker", D(2012, 4, 20), None, CORE, "The Circle",
           "Working actress; Marc's goddaughter & ward"),

    # ---------------- FEATURED CONTRACT ----------------
    "GS": ("Augustus “Gus” Smilley", D(1943, 3, 8), None, FEATURED,
           "Smilley", "Founder & Chairman Emeritus, Smilley Corporation"),
    "LE": ("Leonard Smilley", D(1964, 10, 11), None, FEATURED, "Smilley",
           "Chairman & CEO, Smilley Corporation"),
    "CE": ("Celeste Smilley", D(1966, 2, 22), None, FEATURED, "Smilley",
           "Chair, Smilley Family Foundation"),
    "NA": ("Nathaniel Smilley", D(1985, 3, 14), None, FEATURED, "Smilley",
           "EVP; President, Smilley Consumer & Digital (born Leonard Nathaniel Smilley Jr.)"),
    "CA": ("Camille Smilley-Ward", D(1988, 11, 2), None, FEATURED, "Smilley",
           "CFO, Smilley Corporation"),
    "DS": ("Desmond Smilley", D(1994, 12, 12), None, FEATURED, "Smilley",
           "Creative Director, Smilley Beauty"),
    "KM": ("Kane Mitchell", D(1990, 11, 17), None, FEATURED, "Blackwater",
           "Marc's bodyguard; Blackwater enforcer"),
    "JH": ("Journee Holloway", D(1993, 11, 5), None, FEATURED, "Media",
           "Investigative reporter, The Peach Ledger"),
    "JU": ("Julian Cummings", D(1997, 2, 6), None, FEATURED, "The Circle",
           "Arianna's younger brother, three years sober"),

    # ---------------- RECURRING ----------------
    "LO": ("Loretta Smilley", D(1945, 7, 21), None, RECURRING, "Smilley",
           "Co-founder, Smilley Corporation; matriarch"),
    "DE": ("Delphine Smilley", D(1968, 5, 2), None, RECURRING, "Smilley",
           "President, Smilley Home; Gus's daughter"),
    "MQ": ("Monique Smilley", D(1987, 9, 30), None, RECURRING, "Smilley",
           "Nathaniel's wife; former Donohue Records singer"),
    "DO": ("Dorian Ward", D(1983, 7, 9), None, RECURRING, "Smilley",
           "Chief Strategy Officer, Smilley; Camille's husband"),
    "TR": ("Leonard “Trey” Smilley III", D(2012, 1, 22), None,
           RECURRING, "Smilley", "Son of Nathaniel (Leonard Jr.); Westbrook classmate"),
    "EH": ("Ezekiel “Zeke” Hart", D(1958, 4, 4), None, RECURRING,
           "Blackwater", "Consigliere; BSI General Counsel"),
    "NS": ("Nova Sinclair", D(1996, 1, 29), None, RECURRING, "Blackwater",
           "Blackwater intelligence chief; BSI CTO"),
    "DX": ("Darnell “Deuce” Whitaker", D(1987, 6, 12), None,
           RECURRING, "Blackwater", "Atlanta Captain; accused of murder"),
    "WJ": ("Walter Jackson", D(1956, 1, 18), None, RECURRING, "APD",
           "Former APD Chief; Jeremy's father"),
    "RD": ("Det. Rosa Delgado", D(1988, 4, 7), None, RECURRING, "APD",
           "Jeremy's partner, APD Homicide"),
    "FB": ("SAC Nadia Brooks", D(1985, 8, 8), None, RECURRING, "Law",
           "FBI Special Agent in Charge, Atlanta"),
    "BK": ("Brielle Knox", D(1990, 3, 9), None, RECURRING, "Media",
           "Host, “Hollywood Heat”; Martin's girlfriend"),
    "CH": ("State Rep. Cordell Haynes", D(1976, 8, 3), None, RECURRING, "Politics",
           "Arianna's primary challenger for Attorney General"),
    "MP": ("State Sen. Marcus Pryor", D(1980, 1, 11), None, RECURRING,
           "Politics", "Jasmine's primary challenger"),
    "LG": ("Lucinda Graves", D(1952, 1, 27), None, RECURRING, "Belmont Crest",
           "Chair, Country Club Membership Committee"),
    "WO": ("Winston Oduya", D(1950, 10, 1), None, RECURRING, "Belmont Crest",
           "Majordomo of Summit House"),
    "PR": ("Priya Raman", D(1991, 4, 14), None, RECURRING, "Donohue",
           "Joan's chief of staff, Donohue Foundation"),
    "PW": ("Pearl Whitfield", D(1954, 12, 24), None, RECURRING,
           "Belmont Crest", "Marc's house manager; Lyric's “Mama Pearl”"),
    "MF": ("Malik Freeman", D(1995, 8, 21), None, RECURRING, "Belmont Crest",
           "Head bartender, Belmont Crest Country Club"),
    "VM": ("Vincent Morrow", D(1966, 2, 3), None, RECURRING, "Underworld",
           "Boss, The Morrow Organization"),
    "ZR": ("Zion Reed", D(2005, 2, 14), None, RECURRING, "Donohue",
           "Morehouse student; Alvin's son"),
    "EC": ("Dr. Evelyn Cummings", D(1958, 6, 28), None, RECURRING,
           "The Circle", "Cardiothoracic surgeon; Arianna's mother"),
    "EV": ("Everett Lane", D(1985, 2, 20), None, RECURRING, "Westbrook",
           "Westbrook drama & history teacher"),
    "CW": ("Gen. (Ret.) Calvin Whitmore", D(1961, 9, 9), None, RECURRING,
           "BSI", "CEO, Blackwater Security International"),
    "NV": ("Nia Vaughn", D(1995, 10, 19), None, RECURRING, "Broadway",
           "Marc's Sweet Chariot co-star"),
    "SC": ("Sebastian Crowe", D(1975, 7, 7), None, RECURRING, "Broadway",
           "Director, Sweet Chariot revival"),
    "JK": ("Judge Miriam Okoye", D(1965, 3, 30), None, RECURRING, "Law",
           "Fulton County Superior Court judge"),

    # ---------------- SUPPORTING ----------------
    "GB": ("Gerald Baker", D(1962, 5, 5), None, SUPPORTING, "The Circle",
           "Amond's father; Baker & Sons Contracting"),
    "YB": ("Yvonne Baker", D(1964, 8, 30), None, SUPPORTING, "The Circle",
           "Amond's mother"),
    "HC": ("Judge Harold Cummings", D(1955, 9, 2), None, SUPPORTING,
           "The Circle", "Retired judge; Arianna's father"),
    "CD": ("Curtis Divine", D(1963, 3, 16), None, SUPPORTING, "The Circle",
           "Harmony's father; retired mail carrier"),
    "LD": ("Lorna Divine", D(1965, 11, 11), None, SUPPORTING, "The Circle",
           "Harmony's mother; ER nurse"),
    "AB": ("Dr. Constance Albright", D(1968, 9, 15), None, SUPPORTING,
           "Westbrook", "Head of School, Westbrook Academy"),
    "JC": ("Jaden Cole", D(2012, 7, 19), None, SUPPORTING, "Westbrook",
           "Westbrook classmate"),
    "CL": ("Coco Laurent", D(1996, 5, 16), None, SUPPORTING, "Donohue",
           "Alvin's girlfriend, Paris"),
    "QM": ("Tasha “Queenie” Monroe", D(1986, 10, 3), None,
           SUPPORTING, "Blackwater", "West Coast Captain"),
    "IV": ("Idris Vance", D(1981, 5, 25), None, SUPPORTING, "Blackwater",
           "East Coast Captain"),
    "CO": ("Chidi Okafor", D(1979, 8, 18), None, SUPPORTING, "Blackwater",
           "Africa Captain (Lagos)"),
    "LF": ("Lorenzo Ferraro", D(1975, 1, 14), None, SUPPORTING, "Blackwater",
           "Europe Captain (Milan)"),
    "CB": ("Cyrus Bell", D(1979, 12, 1), None, SUPPORTING, "Blackwater",
           "“The Banker”"),
    "RT": ("Darius Ng", D(1994, 6, 9), None, SUPPORTING, "Smilley",
           "RootsKit lab director"),

    # ---------------- DAY PLAYERS ----------------
    "TB": ("Terrence “T-Bone” Gaines", D(1984, 3, 2),
           D(2026, 1, 4), DAY, "Blackwater", "Murdered Blackwater traitor"),
    "BH": ("Beverly \u201cBev\u201d Holland", D(1965, 7, 12), None, RECURRING, "Politics",
           "Jasmine's chief of staff since 1997"),
    "FL": ("Dr. Frances Lowe", D(1963, 5, 21), None, DAY, "Law",
           "Fulton County Medical Examiner"),
    "DM": ("Officer Devon Marsh", D(1999, 10, 4), None, DAY, "APD",
           "APD digital forensics technician"),
    "OS": ("Otis Smilley (1958)", D(1919, 11, 3), D(1988, 2, 9), DAY,
           "Smilley", "Gus's father; Beacon press foreman"),
    "HW": ("Harlan Whitfield (1958)", D(1911, 4, 22), D(1979, 6, 30), DAY,
           "Belmont Crest", "White attorney who fronted the 1958 land purchase"),

    # ---------------- GUEST STARS ----------------
    "YA": ("Young Alexander Donohue (1958)", D(1916, 3, 3), D(2006, 1, 9),
           GUEST, "Flashback", "Founder, age 41 in 1958"),
    "YS": ("Young Simone Donohue (1958)", D(1920, 9, 12), D(2014, 11, 22),
           GUEST, "Flashback", "Co-founder of Belmont Crest, age 37 in 1958"),
    "YV": ("Young Victor Donohue (1958 / 1966)", D(1946, 5, 30), None, GUEST,
           "Flashback", "Ages 11 and 20"),
    "YT": ("Young Theodore Donohue (1958)", D(1944, 7, 31), None, GUEST,
           "Flashback", "Age 13"),
    "YJ": ("Young Joan Mercer (1966)", D(1948, 4, 17), None, GUEST,
           "Flashback", "Age 18, Broadway ingenue"),
    "YG": ("Young Gus Smilley (1958 / 1966)", D(1943, 3, 8), None, GUEST,
           "Flashback", "Ages 15 and 23"),
    "TD": ("Theodore Donohue", D(1944, 7, 31), None, GUEST, "Theodore Branch",
           "Former DA; arrives Ep #0167; Core in Season 2"),
    "LC": ("Lorraine Donohue", D(1949, 11, 19), None, GUEST, "Theodore Branch",
           "Theodore's wife; Core in Season 2"),
    "XD": ("Alexander “Xander” Donohue II", D(1972, 8, 14), None,
           GUEST, "Theodore Branch", "Theodore's son; hedge-fund king; Core in S2"),
    "CP": ("Judge Celestine Donohue-Price", D(1976, 2, 27), None, GUEST,
           "Theodore Branch", "Theodore's daughter; federal appellate judge; Core in S2"),
    "T3": ("Theodore “Theo” Donohue III", D(1997, 6, 3), None, GUEST,
           "Theodore Branch", "Xander's son; Core in S2"),
    "SD": ("Sienna Donohue", D(2001, 12, 9), None, GUEST, "Theodore Branch",
           "Xander's daughter; influencer; Core in S2"),
    "AP": ("August Price", D(2012, 3, 11), None, GUEST, "Theodore Branch",
           "Celestine's son; joins Westbrook in S2"),
}

# Opening credits (Season 1). The four crowns get unique sequences;
# Alvin gets his own unique sequence starting with Ep #0085.
UNIQUE_SEQUENCES = ["VD", "JD", "NB", "JO"]
ALVIN_JOINS = 85

# Political party registration (as of Jan 5, 2026).
DEM, REP, IND = "Democrat", "Republican", "Independent"
MINOR = "Too young to vote"
PARTY = {
    # Donohue / Bullock / Olson
    "VD": REP, "JD": DEM, "NB": DEM, "JO": DEM, "AL": IND, "RB": IND, "PO": REP,
    "MA": "Democrat (with Republican values)", "EL": IND, "GR": DEM, "MO": REP,
    "ML": DEM, "JJ": REP,
    # The Circle
    "AM": REP, "AR": DEM, "HD": DEM, "JU": DEM, "EC": DEM, "HC": IND, "GB": REP,
    "YB": DEM, "CD": DEM, "LD": DEM,
    # Smilley
    "ES": REP, "GS": REP, "LO": DEM, "LE": REP, "CE": REP, "NA": REP, "CA": REP,
    "DO": REP, "DE": DEM, "DS": DEM, "MQ": IND, "RT": IND,
    # Kids
    "EM": MINOR, "VI": MINOR, "LY": MINOR, "TR": MINOR, "JC": MINOR, "AP": MINOR,
    # Blackwater / BSI
    "EH": REP, "KM": IND, "NS": "Not registered", "DX": DEM, "CB": IND, "QM": DEM,
    "IV": REP, "CO": "Not a U.S. citizen", "LF": "Not a U.S. citizen", "CW": REP,
    "TB": "Not registered",
    # Law, politics, media
    "WJ": IND, "RD": DEM, "FB": IND, "JK": IND, "MP": DEM, "CH": DEM, "JH": IND, "BK": REP,
    # Belmont Crest, Westbrook, Broadway, Alvin's world, underworld
    "LG": REP, "WO": "Not a U.S. citizen (British)", "MF": DEM, "PW": DEM, "PR": DEM,
    "AB": IND, "EV": DEM, "SC": "Not a U.S. citizen (British)", "NV": DEM,
    "ZR": DEM, "CL": "Not a U.S. citizen (French)", "VM": REP,
    # Theodore branch
    "TD": REP, "LC": REP, "XD": REP, "CP": IND, "T3": IND, "SD": IND,
    "FL": IND, "DM": DEM, "BH": DEM,
    # Historical (flashback)
    "OS": REP + " (the party of Lincoln, until 1964)", "HW": DEM,
}

# Marc-Anthony's political platform, as set by the showrunner. Locked canon:
# he will 100% accomplish every item, zero questions asked.
MARC_PLATFORM = [
    "Universal healthcare",
    "Universal education",
    "100% elimination of the national debt",
    "World peace",
    "Domestic peace",
    "100% elimination of inflation",
    "Making everything 100% astronomically affordable again",
    "Making the USA a dominant superpower once again",
    "Astronomically lowering taxes, and eventually eliminating them 100% (there are "
    "better ways for the country to make money)",
    "Making the country 100% clean in every way",
    "Immigration 100% legal and allowed: open borders, 100% all the way",
]
MARC_LONG_TERM = ("<b>The North American Union</b>: a political and economic union for "
                  "North America.")
