"""
ipl_data.py
IPL data through all seasons 2008-2025, plus IPL 2026 live data
(Updated: May 20, 2026 — after Match 64: RR vs LSG)
"""

# ── Active & historical teams ─────────────────────────────────────────────────
IPL_TEAMS: dict[str, dict] = {
    "Mumbai Indians":             {"short":"MI",   "color":"#004BA0","home":"Wankhede Stadium, Mumbai",                 "titles":5,"active":True},
    "Chennai Super Kings":        {"short":"CSK",  "color":"#F7C948","home":"MA Chidambaram Stadium, Chennai",          "titles":5,"active":True},
    "Kolkata Knight Riders":      {"short":"KKR",  "color":"#3A225D","home":"Eden Gardens, Kolkata",                    "titles":3,"active":True},
    "Royal Challengers Bengaluru":{"short":"RCB",  "color":"#D71920","home":"M. Chinnaswamy Stadium, Bengaluru",        "titles":1,"active":True},
    "Delhi Capitals":             {"short":"DC",   "color":"#0078BC","home":"Arun Jaitley Stadium, Delhi",              "titles":0,"active":True},
    "Sunrisers Hyderabad":        {"short":"SRH",  "color":"#F26522","home":"Rajiv Gandhi Intl. Stadium, Hyderabad",    "titles":1,"active":True},
    "Punjab Kings":               {"short":"PBKS", "color":"#ED1B24","home":"PCA Stadium, New Chandigarh",              "titles":0,"active":True},
    "Rajasthan Royals":           {"short":"RR",   "color":"#EA1A85","home":"Sawai Mansingh Stadium, Jaipur",           "titles":1,"active":True},
    "Lucknow Super Giants":       {"short":"LSG",  "color":"#A72056","home":"BRSABV Ekana Stadium, Lucknow",            "titles":0,"active":True},
    "Gujarat Titans":             {"short":"GT",   "color":"#1C3E6E","home":"Narendra Modi Stadium, Ahmedabad",         "titles":1,"active":True},
    "Deccan Chargers":            {"short":"DC2",  "color":"#F7941D","titles":1,"active":False},
    "Kochi Tuskers Kerala":       {"short":"KTK",  "color":"#F7941D","titles":0,"active":False},
    "Pune Warriors India":        {"short":"PWI",  "color":"#006CB7","titles":0,"active":False},
    "Rising Pune Supergiant":     {"short":"RPS",  "color":"#870f47","titles":0,"active":False},
    "Gujarat Lions":              {"short":"GL",   "color":"#E7501D","titles":0,"active":False},
}

# ── All season winners ────────────────────────────────────────────────────────
IPL_WINNERS: dict[int, str] = {
    2008:"Rajasthan Royals",    2009:"Deccan Chargers",
    2010:"Chennai Super Kings", 2011:"Chennai Super Kings",
    2012:"Kolkata Knight Riders",2013:"Mumbai Indians",
    2014:"Kolkata Knight Riders",2015:"Mumbai Indians",
    2016:"Sunrisers Hyderabad", 2017:"Mumbai Indians",
    2018:"Chennai Super Kings", 2019:"Mumbai Indians",
    2020:"Mumbai Indians",      2021:"Chennai Super Kings",
    2022:"Gujarat Titans",      2023:"Chennai Super Kings",
    2024:"Kolkata Knight Riders",2025:"Royal Challengers Bengaluru",
}

# ── Full season details ───────────────────────────────────────────────────────
IPL_SEASON_DETAILS: dict[int, dict] = {
    2008: {"winner":"Rajasthan Royals",            "runner_up":"Chennai Super Kings",        "margin":"3 wkts",   "captain":"Shane Warne",       "venue":"DY Patil Stadium, Mumbai"},
    2009: {"winner":"Deccan Chargers",             "runner_up":"Royal Challengers Bengaluru","margin":"6 runs",   "captain":"Adam Gilchrist",    "venue":"Wanderers, Johannesburg (SA)"},
    2010: {"winner":"Chennai Super Kings",         "runner_up":"Mumbai Indians",             "margin":"22 runs",  "captain":"MS Dhoni",          "venue":"DY Patil Stadium, Mumbai"},
    2011: {"winner":"Chennai Super Kings",         "runner_up":"Royal Challengers Bengaluru","margin":"58 runs",  "captain":"MS Dhoni",          "venue":"MA Chidambaram, Chennai"},
    2012: {"winner":"Kolkata Knight Riders",       "runner_up":"Chennai Super Kings",        "margin":"5 wkts",   "captain":"Gautam Gambhir",    "venue":"MA Chidambaram, Chennai"},
    2013: {"winner":"Mumbai Indians",              "runner_up":"Chennai Super Kings",        "margin":"23 runs",  "captain":"Rohit Sharma",      "venue":"Eden Gardens, Kolkata"},
    2014: {"winner":"Kolkata Knight Riders",       "runner_up":"Kings XI Punjab",            "margin":"3 wkts",   "captain":"Gautam Gambhir",    "venue":"Chinnaswamy, Bengaluru"},
    2015: {"winner":"Mumbai Indians",              "runner_up":"Chennai Super Kings",        "margin":"41 runs",  "captain":"Rohit Sharma",      "venue":"Eden Gardens, Kolkata"},
    2016: {"winner":"Sunrisers Hyderabad",         "runner_up":"Royal Challengers Bengaluru","margin":"8 runs",   "captain":"David Warner",      "venue":"Chinnaswamy, Bengaluru"},
    2017: {"winner":"Mumbai Indians",              "runner_up":"Rising Pune Supergiant",     "margin":"1 run",    "captain":"Rohit Sharma",      "venue":"Rajiv Gandhi Stadium, Hyderabad"},
    2018: {"winner":"Chennai Super Kings",         "runner_up":"Sunrisers Hyderabad",        "margin":"8 wkts",   "captain":"MS Dhoni",          "venue":"Wankhede, Mumbai"},
    2019: {"winner":"Mumbai Indians",              "runner_up":"Chennai Super Kings",        "margin":"1 run",    "captain":"Rohit Sharma",      "venue":"Rajiv Gandhi Stadium, Hyderabad"},
    2020: {"winner":"Mumbai Indians",              "runner_up":"Delhi Capitals",             "margin":"5 wkts",   "captain":"Rohit Sharma",      "venue":"Dubai Intl. Stadium (UAE)"},
    2021: {"winner":"Chennai Super Kings",         "runner_up":"Kolkata Knight Riders",      "margin":"27 runs",  "captain":"MS Dhoni",          "venue":"Dubai Intl. Stadium (UAE)"},
    2022: {"winner":"Gujarat Titans",             "runner_up":"Rajasthan Royals",           "margin":"7 wkts",   "captain":"Hardik Pandya",     "venue":"Narendra Modi Stadium, Ahmedabad"},
    2023: {"winner":"Chennai Super Kings",         "runner_up":"Gujarat Titans",             "margin":"5 wkts",   "captain":"MS Dhoni",          "venue":"Narendra Modi Stadium, Ahmedabad"},
    2024: {"winner":"Kolkata Knight Riders",       "runner_up":"Sunrisers Hyderabad",        "margin":"8 wkts",   "captain":"Shreyas Iyer",      "venue":"MA Chidambaram, Chennai",  "potm":"Mitchell Starc","player_of_tournament":"Sunil Narine"},
    2025: {"winner":"Royal Challengers Bengaluru", "runner_up":"Punjab Kings",               "margin":"6 runs",   "captain":"Rajat Patidar",     "venue":"Narendra Modi Stadium, Ahmedabad","potm":"Krunal Pandya","player_of_tournament":"Suryakumar Yadav (MI)"},
}

# ── Orange Cap history ────────────────────────────────────────────────────────
ORANGE_CAP: dict[int, tuple] = {
    2008:("Shaun Marsh",616),       2009:("Matthew Hayden",572),
    2010:("Sachin Tendulkar",618),  2011:("Chris Gayle",608),
    2012:("Chris Gayle",733),       2013:("Michael Hussey",733),
    2014:("Robin Uthappa",660),     2015:("David Warner",562),
    2016:("Virat Kohli",973),       2017:("David Warner",641),
    2018:("Kane Williamson",735),   2019:("David Warner",692),
    2020:("KL Rahul",670),          2021:("Ruturaj Gaikwad",635),
    2022:("Jos Buttler",863),       2023:("Shubman Gill",890),
    2024:("Virat Kohli",741),       2025:("Sai Sudharsan",759),
}

# ── Purple Cap history ────────────────────────────────────────────────────────
PURPLE_CAP: dict[int, tuple] = {
    2008:("Sohail Tanvir",22),      2009:("RP Singh",23),
    2010:("Pragyan Ojha",21),       2011:("Lasith Malinga",28),
    2012:("Morne Morkel",25),       2013:("Dwayne Bravo",32),
    2014:("Mohit Sharma",23),       2015:("Dwayne Bravo",26),
    2016:("Bhuvneshwar Kumar",23),  2017:("Bhuvneshwar Kumar",26),
    2018:("Andrew Tye",24),         2019:("Imran Tahir",26),
    2020:("Kagiso Rabada",30),      2021:("Harshal Patel",32),
    2022:("Yuzvendra Chahal",27),   2023:("Mohammed Shami",28),
    2024:("Harshal Patel",24),      2025:("Prasidh Krishna",25),
}

# ══════════════════════════════════════════════════════════════════════════════
# IPL 2026 LIVE DATA — Updated May 20, 2026 (after Match 64: RR vs LSG)
# Sources: ESPNCricinfo, Business Standard, KhelNow, IPLDaily
# ══════════════════════════════════════════════════════════════════════════════
IPL_2026_LIVE: dict = {

    # ── Points table ──────────────────────────────────────────────────────────
    # status: Q=Qualified, E=Eliminated, blank=in race
    "points_table": [
        {"pos":1, "team":"RCB",  "m":12, "w":9, "l":3, "pts":18, "nrr":"+1.053", "status":"Q"},
        {"pos":2, "team":"GT",   "m":13, "w":8, "l":5, "pts":16, "nrr":"+0.614", "status":"Q"},
        {"pos":3, "team":"SRH",  "m":13, "w":8, "l":5, "pts":16, "nrr":"+0.431", "status":"Q"},
        {"pos":4, "team":"RR",   "m":13, "w":7, "l":6, "pts":14, "nrr":"+0.203", "status":""},
        {"pos":5, "team":"PBKS", "m":13, "w":6, "l":6, "pts":13, "nrr":"-0.109", "status":""},
        {"pos":6, "team":"CSK",  "m":13, "w":6, "l":7, "pts":12, "nrr":"+0.178", "status":""},
        {"pos":7, "team":"DC",   "m":13, "w":6, "l":7, "pts":12, "nrr":"-0.245", "status":""},
        {"pos":8, "team":"KKR",  "m":13, "w":5, "l":7, "pts":11, "nrr":"-0.332", "status":""},
        {"pos":9, "team":"MI",   "m":13, "w":4, "l":9, "pts":8,  "nrr":"-0.521", "status":"E"},
        {"pos":10,"team":"LSG",  "m":13, "w":4, "l":9, "pts":8,  "nrr":"-0.791", "status":"E"},
    ],

    # ── Orange Cap (Top run scorers) ──────────────────────────────────────────
    "orange_cap": [
        {"rank":1, "name":"Vaibhav Sooryavanshi","team":"RR",  "runs":579,"avg":44.53,"sr":"202.1","matches":13},
        {"rank":2, "name":"Mitchell Marsh",       "team":"LSG", "runs":563,"avg":43.30,"sr":"171.6","matches":13},
        {"rank":3, "name":"Heinrich Klaasen",     "team":"SRH", "runs":555,"avg":50.45,"sr":"183.2","matches":13},
        {"rank":4, "name":"Sai Sudharsan",        "team":"GT",  "runs":554,"avg":46.17,"sr":"156.5","matches":13},
        {"rank":5, "name":"Shubman Gill",         "team":"GT",  "runs":552,"avg":46.00,"sr":"148.3","matches":13},
        {"rank":6, "name":"Virat Kohli",          "team":"RCB", "runs":542,"avg":49.27,"sr":"144.9","matches":12},
        {"rank":7, "name":"KL Rahul",             "team":"DC",  "runs":533,"avg":41.00,"sr":"139.8","matches":13},
    ],

    # ── Purple Cap (Top wicket takers) ────────────────────────────────────────
    "purple_cap": [
        {"rank":1, "name":"Bhuvneshwar Kumar","team":"RCB", "wickets":24,"avg":16.37,"econ":"7.4","matches":13},
        {"rank":2, "name":"Kagiso Rabada",    "team":"GT",  "wickets":21,"avg":21.95,"econ":"8.1","matches":13},
        {"rank":3, "name":"Anshul Kamboj",    "team":"CSK", "wickets":20,"avg":23.70,"econ":"8.6","matches":13},
        {"rank":4, "name":"Jofra Archer",     "team":"RR",  "wickets":18,"avg":19.44,"econ":"8.3","matches":13},
        {"rank":5, "name":"Eshan Malinga",    "team":"SRH", "wickets":17,"avg":22.11,"econ":"8.9","matches":13},
    ],

    # ── Upcoming matches ──────────────────────────────────────────────────────
    "upcoming_matches": [
        {"match_no":65, "team1":"GT",   "team2":"CSK",  "date":"May 21, 2026","time":"7:30 PM","venue":"Narendra Modi Stadium, Ahmedabad"},
        {"match_no":66, "team1":"KKR",  "team2":"MI",   "date":"May 21, 2026","time":"2:00 PM","venue":"Eden Gardens, Kolkata"},
        {"match_no":67, "team1":"SRH",  "team2":"RCB",  "date":"May 22, 2026","time":"7:30 PM","venue":"Rajiv Gandhi Intl. Stadium, Hyderabad"},
        {"match_no":68, "team1":"LSG",  "team2":"PBKS", "date":"May 23, 2026","time":"7:30 PM","venue":"BRSABV Ekana Stadium, Lucknow"},
        {"match_no":69, "team1":"MI",   "team2":"DC",   "date":"May 24, 2026","time":"3:30 PM","venue":"Wankhede Stadium, Mumbai"},
        {"match_no":70, "team1":"KKR",  "team2":"RR",   "date":"May 24, 2026","time":"7:30 PM","venue":"Eden Gardens, Kolkata"},
        {"match_no":"Q1","team1":"TBA", "team2":"TBA",  "date":"May 26, 2026","time":"7:30 PM","venue":"Dharamsala"},
        {"match_no":"EL","team1":"TBA", "team2":"TBA",  "date":"May 27, 2026","time":"7:30 PM","venue":"Mullanpur"},
        {"match_no":"Q2","team1":"TBA", "team2":"TBA",  "date":"May 29, 2026","time":"7:30 PM","venue":"Mullanpur"},
        {"match_no":"F", "team1":"TBA", "team2":"TBA",  "date":"May 31, 2026","time":"7:30 PM","venue":"Narendra Modi Stadium, Ahmedabad"},
    ],

    # ── Season-level batting/bowling stats ────────────────────────────────────
    "season_stats": {
        "Most Sixes":            "Nicholas Pooran (LSG) — 46",
        "Most Fours":            "Sai Sudharsan (GT) — 62",
        "Highest Strike Rate":   "Vaibhav Sooryavanshi (RR) — 202.1",
        "Highest Ind. Score":    "V. Sooryavanshi 106* (RR vs DC)",
        "Best Bowling Figures":  "Bhuvneshwar Kumar 5/14 (RCB vs MI)",
        "Most Dot Balls (Bowl)": "Bhuvneshwar Kumar — 182 dot balls",
        "Most Dot Balls (Bat)":  "Shubman Gill — 91 dots faced",
        "Highest Team Score":    "SRH 252/4 vs MI (Mar 31)",
        "Lowest Team Score":     "MI 98 all out vs RCB (Apr 8)",
        "Most Matches Played":   "13 matches (8 teams, 64 played)",
    },

    # ── Recent results (last 5 matches) ──────────────────────────────────────
    "recent_results": [
        {"match_no":64,"result":"RR beat LSG by 7 wkts (19.1 ov)","potm":"Vaibhav Sooryavanshi 93(38)","venue":"Jaipur","date":"May 19"},
        {"match_no":63,"result":"LSG beat RCB by 5 wkts","potm":"Mitchell Marsh 78(45)","venue":"Lucknow","date":"May 18"},
        {"match_no":62,"result":"CSK beat SRH by 4 wkts","potm":"Anshul Kamboj 4/22","venue":"Chennai","date":"May 17"},
        {"match_no":61,"result":"GT beat DC by 8 runs","potm":"Kagiso Rabada 3/18","venue":"Ahmedabad","date":"May 16"},
        {"match_no":60,"result":"RCB beat PBKS by 6 wkts","potm":"Virat Kohli 89(52)","venue":"Bengaluru","date":"May 15"},
    ],

    # ── Playoff qualification status ──────────────────────────────────────────
    "playoff_status": {
        "qualified":  ["RCB", "GT", "SRH"],
        "eliminated": ["MI", "LSG"],
        "in_race":    ["RR (14 pts, needs win vs KKR)", "PBKS (13 pts)", "CSK (12 pts)", "DC (12 pts)", "KKR (11 pts, nearly out)"],
        "last_league_day": "May 24, 2026",
        "playoff_venues": {"Q1":"Dharamsala (May 26)", "EL":"Mullanpur (May 27)", "Q2":"Mullanpur (May 29)", "Final":"Ahmedabad (May 31)"},
    },

    # ── Key IPL 2026 facts ────────────────────────────────────────────────────
    "season_info": {
        "edition": "19th (Season 19)",
        "start_date": "March 28, 2026",
        "final_date": "May 31, 2026",
        "total_matches": 84,
        "league_matches": 70,
        "defending_champion": "Royal Challengers Bengaluru",
        "most_expensive_auction_buy": "Cameron Green — ₹25.20 crore",
        "notable": "IPL 2025 was suspended May 9–16 due to India–Pakistan tensions; resumed May 17",
    },
}

# ── Quick question chips ──────────────────────────────────────────────────────
QUICK_QUESTIONS: list[str] = [
    "📊 IPL 2026 points table & playoff race",
    "🟠 IPL 2026 Orange Cap — top run scorers",
    "🟣 IPL 2026 Purple Cap — top wicket takers",
    "📅 Upcoming IPL 2026 matches",
    "🏆 All IPL champions from 2008 to 2025",
    "💰 How does the IPL auction work?",
    "🎯 Most dot balls in IPL 2026",
    "🏏 Most sixes and fours in IPL 2026",
    "🏅 Man of the Match — recent IPL 2026 games",
    "❓ How does the IPL playoff format work?",
]