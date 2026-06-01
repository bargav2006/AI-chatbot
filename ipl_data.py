"""
ipl_data.py — All IPL data 2008-2026
Updated: June 1, 2026 — FINAL COMPLETED. RCB won IPL 2026!
"""

IPL_TEAMS = {
    "Mumbai Indians":             {"short":"MI",   "color":"#004BA0","active":True,"titles":5},
    "Chennai Super Kings":        {"short":"CSK",  "color":"#F7C948","active":True,"titles":5},
    "Kolkata Knight Riders":      {"short":"KKR",  "color":"#3A225D","active":True,"titles":3},
    "Royal Challengers Bengaluru":{"short":"RCB",  "color":"#D71920","active":True,"titles":2},
    "Delhi Capitals":             {"short":"DC",   "color":"#0078BC","active":True,"titles":0},
    "Sunrisers Hyderabad":        {"short":"SRH",  "color":"#F26522","active":True,"titles":1},
    "Punjab Kings":               {"short":"PBKS", "color":"#ED1B24","active":True,"titles":0},
    "Rajasthan Royals":           {"short":"RR",   "color":"#EA1A85","active":True,"titles":1},
    "Lucknow Super Giants":       {"short":"LSG",  "color":"#A72056","active":True,"titles":0},
    "Gujarat Titans":             {"short":"GT",   "color":"#1C3E6E","active":True,"titles":1},
}

IPL_WINNERS = {
    2008:"Rajasthan Royals",    2009:"Deccan Chargers",
    2010:"Chennai Super Kings", 2011:"Chennai Super Kings",
    2012:"Kolkata Knight Riders",2013:"Mumbai Indians",
    2014:"Kolkata Knight Riders",2015:"Mumbai Indians",
    2016:"Sunrisers Hyderabad", 2017:"Mumbai Indians",
    2018:"Chennai Super Kings", 2019:"Mumbai Indians",
    2020:"Mumbai Indians",      2021:"Chennai Super Kings",
    2022:"Gujarat Titans",      2023:"Chennai Super Kings",
    2024:"Kolkata Knight Riders",2025:"Royal Challengers Bengaluru",
    2026:"Royal Challengers Bengaluru",
}

# ── IPL 2026 COMPLETE DATA — Season Over (June 1, 2026) ──────────────────────
IPL_2026_LIVE = {

    # Final league standings
    "points_table": [
        {"pos":1, "team":"RCB",  "m":14,"w":9,"l":5,"pts":18,"nrr":"+1.420","status":"Q"},
        {"pos":2, "team":"PBKS", "m":14,"w":8,"l":5,"pts":14,"nrr":"+1.043","status":"Q"},
        {"pos":3, "team":"SRH",  "m":14,"w":8,"l":5,"pts":12,"nrr":"+0.832","status":"Q"},
        {"pos":4, "team":"RR",   "m":14,"w":7,"l":6,"pts":12,"nrr":"+0.510","status":"Q"},
        {"pos":5, "team":"GT",   "m":14,"w":6,"l":7,"pts":10,"nrr":"-0.192","status":"E"},
        {"pos":6, "team":"DC",   "m":14,"w":5,"l":8,"pts":8, "nrr":"-0.895","status":"E"},
        {"pos":7, "team":"CSK",  "m":14,"w":4,"l":9,"pts":6, "nrr":"-0.121","status":"E"},
        {"pos":8, "team":"KKR",  "m":14,"w":3,"l":9,"pts":5, "nrr":"-0.751","status":"E"},
        {"pos":9, "team":"MI",   "m":14,"w":3,"l":9,"pts":4, "nrr":"-0.784","status":"E"},
        {"pos":10,"team":"LSG",  "m":14,"w":3,"l":9,"pts":4, "nrr":"-1.106","status":"E"},
    ],

    # Final Orange Cap standings
    "orange_cap": [
        {"rank":1,"name":"Vaibhav Sooryavanshi","team":"RR", "runs":776,"avg":55.4,"sr":"237.3","matches":16},
        {"rank":2,"name":"Shubman Gill",         "team":"GT", "runs":748,"avg":57.5,"sr":"157.1","matches":16},
        {"rank":3,"name":"Sai Sudharsan",        "team":"GT", "runs":698,"avg":53.7,"sr":"155.9","matches":16},
        {"rank":4,"name":"Virat Kohli",          "team":"RCB","runs":675,"avg":52.7,"sr":"165.8","matches":15},
        {"rank":5,"name":"Ishan Kishan",         "team":"SRH","runs":638,"avg":49.1,"sr":"168.4","matches":15},
        {"rank":6,"name":"Riyan Parag",          "team":"RR", "runs":597,"avg":44.2,"sr":"160.2","matches":16},
        {"rank":7,"name":"Travis Head",          "team":"SRH","runs":561,"avg":43.1,"sr":"178.3","matches":15},
    ],

    # Final Purple Cap standings
    "purple_cap": [
        {"rank":1,"name":"Kagiso Rabada",     "team":"GT", "wickets":29,"avg":17.5,"econ":"8.2","matches":16},
        {"rank":2,"name":"Bhuvneshwar Kumar", "team":"RCB","wickets":28,"avg":16.8,"econ":"7.5","matches":15},
        {"rank":3,"name":"Jofra Archer",      "team":"RR", "wickets":22,"avg":18.9,"econ":"8.4","matches":16},
        {"rank":4,"name":"Arshdeep Singh",    "team":"PBKS","wickets":20,"avg":21.4,"econ":"8.7","matches":14},
        {"rank":5,"name":"Eshan Malinga",     "team":"SRH","wickets":20,"avg":22.1,"econ":"9.3","matches":15},
    ],

    # No upcoming matches — season over
    "upcoming_matches": [],

    # All playoff + final results
    "recent_results": [
        {"match_no":"FINAL","result":"RCB beat GT by 5 wkts (18 ov) — GT 155/8, RCB 161/5",
         "potm":"Virat Kohli 75*(42) — fastest IPL fifty 25 balls","venue":"Narendra Modi Stadium, Ahmedabad","date":"May 31"},
        {"match_no":"Q2",  "result":"GT beat RR by 7 wkts (18.4 ov) — Shubman Gill 100*(53)",
         "potm":"Shubman Gill 100*(53)","venue":"Mullanpur","date":"May 29"},
        {"match_no":"EL",  "result":"RR beat SRH by 5 wkts — Vaibhav Sooryavanshi 97(47)",
         "potm":"Vaibhav Sooryavanshi 97(47)","venue":"New Chandigarh","date":"May 27"},
        {"match_no":"Q1",  "result":"RCB beat GT by 4 wkts — Virat Kohli 85*(52)",
         "potm":"Virat Kohli 85*(52)","venue":"HPCA Stadium, Dharamsala","date":"May 26"},
        {"match_no":70,    "result":"PBKS beat RR by 3 wkts","potm":"Arshdeep Singh 3/22",
         "venue":"New Chandigarh","date":"May 24"},
    ],

    # Complete season awards
    "season_stats": {
        "🏆 IPL 2026 Champion":        "Royal Challengers Bengaluru (back-to-back!)",
        "🥈 Runner-Up":                "Gujarat Titans",
        "🏅 Final POTM":               "Virat Kohli 75*(42) — fastest IPL fifty in 25 balls",
        "🌟 MVP / Player of Tournament":"Vaibhav Sooryavanshi (RR) — 776 runs, SR 237.3",
        "🟠 Orange Cap":               "Vaibhav Sooryavanshi (RR) — 776 runs",
        "🟣 Purple Cap":               "Kagiso Rabada (GT) — 29 wickets",
        "🚀 Most Sixes":               "Vaibhav Sooryavanshi (RR) — Super Sixes award",
        "🔵 Most Fours":               "Sai Sudharsan (GT) — 75 fours",
        "⚡ Highest Strike Rate":       "Vaibhav Sooryavanshi (RR) — 237.3",
        "🎯 Most Dot Balls (Bowler)":  "Mohammed Siraj (GT) — 172 dot balls",
        "🏏 Best Bowling Figures":      "Rasikh Salam (RCB) 3/27 (Final)",
        "🌱 Emerging Player":          "Vaibhav Sooryavanshi (RR)",
        "🤝 Fair Play Award":          "Punjab Kings",
        "🏟️ Best Catch":              "Manish Pandey (KKR) — Tim David dismissal",
        "📊 Highest Team Score":       "RR 237/3 vs SRH (Eliminator, May 27)",
        "📉 Lowest Team Score":        "MI 98 all out vs RCB (Apr 8)",
    },

    # Playoff summary
    "playoff_info": {
        "Q1_result":  "RCB beat GT by 4 wkts (May 26, Dharamsala) → RCB to Final",
        "EL_result":  "RR beat SRH by 5 wkts (May 27, New Chandigarh) → SRH eliminated",
        "Q2_result":  "GT beat RR by 7 wkts (May 29, Mullanpur) → RR eliminated, GT to Final",
        "Final":      "RCB beat GT by 5 wkts (May 31, Ahmedabad) — RCB are IPL 2026 Champions!",
        "Finalists":  ["RCB (Champions 🏆)", "GT (Runners-up)"],
    },

    # Final scorecard
    "final_scorecard": {
        "GT_innings":  "GT 155/8 (20 ov) — Washington Sundar 50*(37), Rasikh Salam 3/27, Bhuvneshwar Kumar 2/29",
        "RCB_innings": "RCB 161/5 (18 ov) — Virat Kohli 75*(42), Venkatesh Iyer 32(16), Rashid Khan 2/25",
        "result":      "RCB won by 5 wickets with 12 balls to spare",
        "toss":        "RCB won toss, chose to bowl",
        "venue":       "Narendra Modi Stadium, Ahmedabad",
        "date":        "May 31, 2026",
    },

    # 2026 squads
    "squads": {
        "RCB":  {"captain":"Rajat Patidar","coach":"Andy Flower",
                 "players":["Rajat Patidar","Virat Kohli","Phil Salt","Devdutt Padikkal",
                            "Jitesh Sharma","Krunal Pandya","Tim David","Jacob Bethell",
                            "Romario Shepherd","Venkatesh Iyer","Bhuvneshwar Kumar",
                            "Josh Hazlewood","Yash Dayal","Rasikh Salam","Nuwan Thushara",
                            "Suyash Sharma","Vicky Ostwal","Jordan Cox","Swapnil Singh"]},
        "GT":   {"captain":"Shubman Gill","coach":"Ashish Nehra",
                 "players":["Shubman Gill","Sai Sudharsan","Jos Buttler","Glenn Phillips",
                            "Rahul Tewatia","Washington Sundar","Rashid Khan","Kagiso Rabada",
                            "Mohammed Siraj","Prasidh Krishna","Nishant Sindhu","Jason Holder",
                            "Jayant Yadav","Shahrukh Khan","Kumar Kushagra","Manav Suthar",
                            "Gurnoor Singh Brar","Sai Kishore","Arshad Khan"]},
        "SRH":  {"captain":"Pat Cummins","coach":"Daniel Vettori",
                 "players":["Pat Cummins","Travis Head","Heinrich Klaasen","Ishan Kishan",
                            "Abhishek Sharma","Nitish Kumar Reddy","Harshal Patel",
                            "Liam Livingstone","Kamindu Mendis","Eshan Malinga",
                            "Brydon Carse","Shivam Mavi","Zeeshan Ansari","Jaydev Unadkat"]},
        "RR":   {"captain":"Riyan Parag","coach":"Kumar Sangakkara",
                 "players":["Riyan Parag","Vaibhav Sooryavanshi","Yashasvi Jaiswal",
                            "Shimron Hetmyer","Dhruv Jurel","Ravindra Jadeja","Jofra Archer",
                            "Ravi Bishnoi","Yudhvir Singh Charak","Tushar Deshpande",
                            "Kwena Maphaka","Sandeep Sharma","Sushant Mishra","Adam Milne"]},
        "CSK":  {"captain":"Ruturaj Gaikwad","coach":"Stephen Fleming",
                 "players":["Ruturaj Gaikwad","MS Dhoni","Sanju Samson","Dewald Brevis",
                            "Ayush Mhatre","Shivam Dube","Anshul Kamboj","Noor Ahmad",
                            "Khaleel Ahmed","Rahul Chahar","Matt Henry","Spencer Johnson",
                            "Jamie Overton","Matthew Short","Mukesh Choudhary"]},
        "MI":   {"captain":"Hardik Pandya","coach":"Mahela Jayawardene",
                 "players":["Rohit Sharma","Suryakumar Yadav","Hardik Pandya","Jasprit Bumrah",
                            "Tilak Varma","Ryan Rickelton","Quinton de Kock","Trent Boult",
                            "Deepak Chahar","Allah Ghazanfar","Will Jacks","Mitchell Santner",
                            "Naman Dhir","Shardul Thakur","Corbin Bosch","Robin Minz"]},
        "KKR":  {"captain":"Ajinkya Rahane","coach":"Abhishek Nayar",
                 "players":["Ajinkya Rahane","Sunil Narine","Rinku Singh","Andre Russell",
                            "Varun Chakaravarthy","Cameron Green","Angkrish Raghuvanshi",
                            "Finn Allen","Rachin Ravindra","Blessing Muzarabani",
                            "Matheesha Pathirana","Vaibhav Arora","Rovman Powell"]},
        "DC":   {"captain":"Axar Patel","coach":"Hemang Badani",
                 "players":["Axar Patel","KL Rahul","David Miller","Karun Nair","Tristan Stubbs",
                            "Mitchell Starc","Kuldeep Yadav","T Natarajan","Mukesh Kumar",
                            "Nitish Rana","Sameer Rizvi","Ashutosh Sharma","Prithvi Shaw"]},
        "PBKS": {"captain":"Shreyas Iyer","coach":"Ricky Ponting",
                 "players":["Shreyas Iyer","Prabhsimran Singh","Shashank Singh","Nehal Wadhera",
                            "Arshdeep Singh","Yuzvendra Chahal","Marco Jansen","Marcus Stoinis",
                            "Azmatullah Omarzai","Lockie Ferguson","Xavier Bartlett",
                            "Priyansh Arya","Musheer Khan","Harprett Brar","Mitch Owen"]},
        "LSG":  {"captain":"Rishabh Pant","coach":"Justin Langer",
                 "players":["Rishabh Pant","Nicholas Pooran","Mitchell Marsh","Aiden Markram",
                            "Mohammad Shami","Avesh Khan","Mayank Yadav","Wanindu Hasaranga",
                            "Anrich Nortje","Abdul Samad","Ayush Badoni","Josh Inglis",
                            "Shahbaz Ahamad","Arjun Tendulkar","Mohsin Khan"]},
    },
}

QUICK_QUESTIONS = [
    "🏆 RCB won IPL 2026! Tell me about the final",
    "📊 IPL 2026 complete season summary & awards",
    "🟠 Orange Cap — Sooryavanshi wins with 776 runs",
    "🟣 Purple Cap — Kagiso Rabada 29 wickets",
    "🏏 All season records — sixes, fours, dot balls, SR",
    "📋 All IPL champions from 2008 to 2026",
    "🏅 Man of the Match — all playoff & final results",
    "📋 RCB squad for IPL 2026",
    "🌟 Who won MVP / Player of Tournament 2026?",
    "❓ How does the IPL playoff format work?",
]
