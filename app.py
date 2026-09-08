from flask import Flask, render_template, abort, request, flash, redirect
from datetime import datetime, timedelta
from operator import attrgetter
import os

app = Flask(__name__)
# app.secret_key = os.environ['SECRET_KEY']  # Disabled during dev so Debugger can attach.

# SECRET_KEY=whatever uv run app.py
# Can also use SECRET_KEY='whatever' uv run app.py
# Once installed - use SECRET_KEY='password' uv run gunicorn app:app
# in render.io the start command is gunicorn app:app
# add **/__pycache__/ into .gitignore
# https://github.com/yoniLavi/mod2_unit_11_flask_example
# https://mod2-unit-11-flask-example.onrender.com/


leagueTable = ""
debug = False


allmatches = [
    {"ID": "1", "Round": 1, "Home": "Benetton", "Away": "Dragons", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "2", "Round": 1, "Home": "Connacht", "Away": "Stormers", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "3", "Round": 1, "Home": "Ulster", "Away": "Edinburgh", "Date": "Fri 25 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "4", "Round": 1, "Home": "Lions", "Away": "Leinster", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "5", "Round": 1, "Home": "Sharks", "Away": "Ospreys", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "6", "Round": 1, "Home": "Zebre Parma", "Away": "Bulls", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "7", "Round": 1, "Home": "Munster", "Away": "Glasgow Warriors", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "8", "Round": 1, "Home": "Scarlets", "Away": "Cardiff", "Date": "Sat 26 Sep 2026 ", "Scores": [ ]} ,
    {"ID": "9", "Round": 2, "Home": "Benetton", "Away": "Connacht", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "10", "Round": 2, "Home": "Cardiff", "Away": "Zebre Parma", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "11", "Round": 2, "Home": "Edinburgh", "Away": "Stormers", "Date": "Fri 02 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "12", "Round": 2, "Home": "Lions", "Away": "Ospreys", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "13", "Round": 2, "Home": "Dragons", "Away": "Scarlets", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "14", "Round": 2, "Home": "Sharks", "Away": "Leinster", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "15", "Round": 2, "Home": "Glasgow Warriors", "Away": "Ulster", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "16", "Round": 2, "Home": "Munster", "Away": "Bulls", "Date": "Sat 03 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "17", "Round": 3, "Home": "ragons", "Away": "Ospreys", "Date": "Fri 9 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "18", "Round": 3, "Home": "Glasgow Warriors", "Away": "Connacht", "Date": "Fri 9 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "19", "Round": 3, "Home": "Bulls", "Away": "Lions", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "20", "Round": 3, "Home": "Stormers", "Away": "Sharks", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "21", "Round": 3, "Home": "Zebre Parma", "Away": "Edinburgh", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "22", "Round": 3, "Home": "Scarlets", "Away": "Benetton", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "23", "Round": 3, "Home": "Ulster", "Away": "Munster", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "24", "Round": 3, "Home": "Leinster", "Away": "Cardiff", "Date": "Sat 10 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "25", "Round": 4, "Home": "Cardiff", "Away": "Sharks", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "26", "Round": 4, "Home": "Connacht", "Away": "Zebre Parma", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "27", "Round": 4, "Home": "Edinburgh", "Away": "Lions", "Date": "Fri 23 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "28", "Round": 4, "Home": "Bulls", "Away": "Ulster", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "29", "Round": 4, "Home": "Benetton", "Away": "Glasgow Warriors", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "30", "Round": 4, "Home": "Stormers", "Away": "Scarlets", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "31", "Round": 4, "Home": "Leinster", "Away": "Munster", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "32", "Round": 4, "Home": "Ospreys", "Away": "Dragons", "Date": "Sat 24 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "33", "Round": 5, "Home": "Connacht", "Away": "Leinster", "Date": "Fri 30 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "34", "Round": 5, "Home": "Glasgow Warriors", "Away": "Lions", "Date": "Fri 30 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "35", "Round": 5, "Home": "Stormers", "Away": "Ulster", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "36", "Round": 5, "Home": "Benetton", "Away": "Edinburgh", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "37", "Round": 5, "Home": "Bulls", "Away": "Scarlets", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "38", "Round": 5, "Home": "Dragons", "Away": "Zebre Parma", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "39", "Round": 5, "Home": "Munster", "Away": "Sharks", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "40", "Round": 5, "Home": "Ospreys", "Away": "Cardiff", "Date": "Sat 31 Oct 2026 ", "Scores": [ ]} ,
    {"ID": "41", "Round": 6, "Home": "Edinburgh", "Away": "Dragons", "Date": "Fri 04 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "42", "Round": 6, "Home": "Ospreys", "Away": "Leinster", "Date": "Fri 04 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "43", "Round": 6, "Home": "Lions", "Away": "Bulls", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "44", "Round": 6, "Home": "Sharks", "Away": "Stormers", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "45", "Round": 6, "Home": "Cardiff", "Away": "Ulster", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "46", "Round": 6, "Home": "Scarlets", "Away": "Connacht", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "47", "Round": 6, "Home": "Zebre Parma", "Away": "Munster", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "48", "Round": 6, "Home": "Glasgow Warriors", "Away": "Benetton", "Date": "Sat 05 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "49", "Round": 7, "Home": "Munster", "Away": "Scarlets", "Date": "Fri 18 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "50", "Round": 7, "Home": "Ulster", "Away": "Ospreys", "Date": "Fri 18 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "51", "Round": 7, "Home": "Stormers", "Away": "Lions", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "52", "Round": 7, "Home": "Zebre Parma", "Away": "Benetton", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "53", "Round": 7, "Home": "Cardiff", "Away": "Dragons", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "54", "Round": 7, "Home": "Sharks", "Away": "Bulls", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "55", "Round": 7, "Home": "Leinster", "Away": "Glasgow Warriors", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "56", "Round": 7, "Home": "Connacht", "Away": "Edinburgh", "Date": "Sat 19 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "57", "Round": 8, "Home": "Dragons", "Away": "Cardiff", "Date": "Sat 26 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "58", "Round": 8, "Home": "Ospreys", "Away": "Scarlets", "Date": "Sat 26 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "59", "Round": 8, "Home": "Benetton", "Away": "Zebre Parma", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "60", "Round": 8, "Home": "Edinburgh", "Away": "Glasgow Warriors", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "61", "Round": 8, "Home": "Ulster", "Away": "Connacht", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "62", "Round": 8, "Home": "Munster", "Away": "Leinster", "Date": "Sun 27 Dec 2026 ", "Scores": [ ]} ,
    {"ID": "63", "Round": 8, "Home": "Lions", "Away": "Sharks", "Date": "Sat 20 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "64", "Round": 8, "Home": "Bulls", "Away": "Stormers", "Date": "Sun 21 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "65", "Round": 9, "Home": "Sharks", "Away": "Lions", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "66", "Round": 9, "Home": "Zebre Parma", "Away": "Glasgow Warriors", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "67", "Round": 9, "Home": "Scarlets", "Away": "Dragons", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "68", "Round": 9, "Home": "Connacht", "Away": "Munster", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "69", "Round": 9, "Home": "Cardiff", "Away": "Ospreys", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "70", "Round": 9, "Home": "Edinburgh", "Away": "Benetton", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "71", "Round": 9, "Home": "Leinster", "Away": "Ulster", "Date": "Sat 02 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "72", "Round": 9, "Home": "Stormers", "Away": "Bulls", "Date": "Sun 03 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "73", "Round": 10, "Home": "Glasgow Warriors", "Away": "Scarlets", "Date": "Fri 22 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "74", "Round": 10, "Home": "Ulster", "Away": "Sharks", "Date": "Fri 22 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "75", "Round": 10, "Home": "Lions", "Away": "Zebre Parma", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "76", "Round": 10, "Home": "Stormers", "Away": "Cardiff", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "77", "Round": 10, "Home": "Ospreys", "Away": "Edinburgh", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "78", "Round": 10, "Home": "Benetton", "Away": "Bulls", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "79", "Round": 10, "Home": "Leinster", "Away": "Dragons", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "80", "Round": 10, "Home": "Munster", "Away": "Connacht", "Date": "Sat 23 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "81", "Round": 11, "Home": "Dragons", "Away": "Munster", "Date": "Fri 29 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "82", "Round": 11, "Home": "Glasgow Warriors", "Away": "Ospreys", "Date": "Fri 29 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "83", "Round": 11, "Home": "Lions", "Away": "Cardiff", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "84", "Round": 11, "Home": "Stormers", "Away": "Zebre Parma", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "85", "Round": 11, "Home": "Scarlets", "Away": "Edinburgh", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "86", "Round": 11, "Home": "Leinster", "Away": "Bulls", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "87", "Round": 11, "Home": "Benetton", "Away": "Sharks", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "88", "Round": 11, "Home": "Connacht", "Away": "Ulster", "Date": "Sat 30 Jan 2027 ", "Scores": [ ]} ,
    {"ID": "89", "Round": 12, "Home": "Dragons", "Away": "Ulster", "Date": "Fri 26 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "90", "Round": 12, "Home": "Munster", "Away": "Benetton", "Date": "Fri 26 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "91", "Round": 12, "Home": "Lions", "Away": "Stormers", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "92", "Round": 12, "Home": "Bulls", "Away": "Sharks", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "93", "Round": 12, "Home": "Cardiff", "Away": "Glasgow Warriors", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "94", "Round": 12, "Home": "Zebre Parma", "Away": "Scarlets", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "95", "Round": 12, "Home": "Ospreys", "Away": "Connacht", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "96", "Round": 12, "Home": "Edinburgh", "Away": "Leinster", "Date": "Sat 27 Feb 2027 ", "Scores": [ ]} ,
    {"ID": "97", "Round": 13, "Home": "Sharks", "Away": "Edinburgh", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "98", "Round": 13, "Home": "Connacht", "Away": "Cardiff", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "99", "Round": 13, "Home": "Glasgow Warriors", "Away": "Stormers", "Date": "Fri 19 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "100", "Round": 13, "Home": "Bulls", "Away": "Dragons", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "101", "Round": 13, "Home": "Ulster", "Away": "Zebre Parma", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "102", "Round": 13, "Home": "Munster", "Away": "Ospreys", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "103", "Round": 13, "Home": "Scarlets", "Away": "Lions", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "104", "Round": 13, "Home": "Leinster", "Away": "Benetton", "Date": "Sat 20 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "105", "Round": 14, "Home": "Glasgow Warriors", "Away": "Zebre Parma", "Date": "Fri 26 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "106", "Round": 14, "Home": "Scarlets", "Away": "Leinster", "Date": "Fri 26 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "107", "Round": 14, "Home": "Bulls", "Away": "Edinburgh", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "108", "Round": 14, "Home": "Connacht", "Away": "Lions", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "109", "Round": 14, "Home": "Sharks", "Away": "Dragons", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "110", "Round": 14, "Home": "Cardiff", "Away": "Munster", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "111", "Round": 14, "Home": "Benetton", "Away": "Ulster", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "112", "Round": 14, "Home": "Ospreys", "Away": "Stormers", "Date": "Sat 27 Mar 2027 ", "Scores": [ ]} ,
    {"ID": "113", "Round": 15, "Home": "Dragons", "Away": "Glasgow Warriors", "Date": "Fri 16 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "114", "Round": 15, "Home": "Edinburgh", "Away": "Cardiff", "Date": "Fri 16 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "115", "Round": 15, "Home": "Lions", "Away": "Munster", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "116", "Round": 15, "Home": "Stormers", "Away": "Benetton", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "117", "Round": 15, "Home": "Ospreys", "Away": "Bulls", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "118", "Round": 15, "Home": "Leinster", "Away": "Connacht", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "119", "Round": 15, "Home": "Zebre Parma", "Away": "Sharks", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "120", "Round": 15, "Home": "Ulster", "Away": "Scarlets", "Date": "Sat 17 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "121", "Round": 16, "Home": "Zebre Parma", "Away": "Ospreys", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "122", "Round": 16, "Home": "Ulster", "Away": "Leinster", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "123", "Round": 16, "Home": "Cardiff", "Away": "Bulls", "Date": "Fri 23 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "124", "Round": 16, "Home": "Lions", "Away": "Benetton", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "125", "Round": 16, "Home": "Scarlets", "Away": "Sharks", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "126", "Round": 16, "Home": "Stormers", "Away": "Munster", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "127", "Round": 16, "Home": "Glasgow Warriors", "Away": "Edinburgh", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "128", "Round": 16, "Home": "Connacht", "Away": "Dragons", "Date": "Sat 24 Apr 2027 ", "Scores": [ ]} ,
    {"ID": "129", "Round": 17, "Home": "Dragons", "Away": "Lions", "Date": "Fri 07 May 2027 ", "Scores": [ ]} ,
    {"ID": "130", "Round": 17, "Home": "Edinburgh", "Away": "Zebre Parma", "Date": "Fri 07 May 2027 ", "Scores": [ ]} ,
    {"ID": "131", "Round": 17, "Home": "Sharks", "Away": "Connacht", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "132", "Round": 17, "Home": "Bulls", "Away": "Glasgow Warriors", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "133", "Round": 17, "Home": "Munster", "Away": "Ulster", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "134", "Round": 17, "Home": "Scarlets", "Away": "Ospreys", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "135", "Round": 17, "Home": "Benetton", "Away": "Cardiff", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "136", "Round": 17, "Home": "Leinster", "Away": "Stormers", "Date": "Sat 08 May 2027 ", "Scores": [ ]} ,
    {"ID": "137", "Round": 18, "Home": "Edinburgh", "Away": "Benetton", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "138", "Round": 18, "Home": "Ospreys", "Away": "Benetton", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "139", "Round": 18, "Home": "Ulster", "Away": "Lions", "Date": "Fri 14 May 2027 ", "Scores": [ ]} ,
    {"ID": "140", "Round": 18, "Home": "Bulls", "Away": "Connacht", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "141", "Round": 18, "Home": "Sharks", "Away": "Glasgow Warriors", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "142", "Round": 18, "Home": "Cardiff", "Away": "Scarlets", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "143", "Round": 18, "Home": "Zebre Parma", "Away": "Leinster", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
    {"ID": "144", "Round": 18, "Home": "Dragons", "Away": "Stormers", "Date": "Sat 15 May 2027 ", "Scores": [ ]} ,
]

"""       {"Team": "Benetton", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Bulls", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Cardiff Rugby", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Connacht", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Dragons", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Edinburgh", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Glasgow Warriors", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Leinster", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Lions", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Munster", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Ospreys", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Scarlets", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Stormers", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Sharks", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Ulster", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },
            {"Team": "Zebre", "P": 0, "W": 0, "D": 0, "L": 0, "TF": 0, "TA": 0, "CF": 0, "CA": 0, "GF": 0, "GA": 0, "TBP": 0, "LBP": 0, "Pts": 0 },],
 """


class League:
    def __init__(self):
        self.matches = []
        self.table = [
                Team("Benetton"),
                Team("Bulls"),
                Team("Cardiff"),
                Team("Connacht"),
                Team("Dragons"),
                Team("Edinburgh"),
                Team("Glasgow Warriors"),
                Team("Leinster"),
                Team("Lions"),
                Team("Munster"),
                Team("Ospreys"),
                Team("Scarlets"),
                Team("Stormers"),
                Team("Sharks"),
                Team("Ulster"),
                Team("Zebre Parma")
            ]

        # Populate Matches Data.
        matchID = 0
        for entry in allmatches:
            # Match object per entry in allmatches
            self.matches.append(Match(entry, matchID))
            matchID += 1
#            for table in self.table:
#                endDate = time.strpTime(table.get("Week"), "%a %d %b %Y")
#                startDate = time.strpTime(entry.get("Date"), "%a %d %b %Y")

    def getTable(self, date):
        index = 0
        startDate = datetime.strptime("20  Sep 2026", "%d %b %Y")
        for team in self.table:
            team.clearData()
        for match in self.matches:
            matchData = match.calcPoints()
            for team in self.table:
                if (match.date <= (startDate + timedelta(days=7))):
                    if team.name == match.home:
                        team.points += matchData.get('homePoints')
                        team.trybonuspoints += matchData.get('homeTryBonusPoints')
                        team.tries_for += matchData.get('homeTries')
                        team.tries_against += matchData.get('awayTries')
                        team.losingbonuspoints += matchData.get('homeLosingBonusPoints')
                        team.played += 1
                        team.won += (matchData.get('homeScore') > matchData.get('awayScore'))
                        team.drawn += (matchData.get('homeScore') == matchData.get('awayScore'))
                        team.lost += (matchData.get('homeScore') < matchData.get('awayScore'))
                        team.pointsdifference += matchData.get('homePointsDifference')

                    if team.name == match.away:
                        team.points += matchData.get('awayPoints')
                        team.trybonuspoints += matchData.get('awayTryBonusPoints')
                        team.tries_for += matchData.get('awayTries')
                        team.tries_against += matchData.get('homeTries')
                        team.losingbonuspoints += matchData.get('awayLosingBonusPoints')
                        team.played += 1
                        team.won += (matchData.get('homeScore') < matchData.get('awayScore'))
                        team.drawn += (matchData.get('homeScore') == matchData.get('awayScore'))
                        team.lost += (matchData.get('homeScore') > matchData.get('awayScore'))
                        team.pointsdifference += matchData.get('awayPointsDifference')

        returnTable = []
        # TODO: Update the Sorting for the table.
        
        for team in sorted(self.table, key=attrgetter('points', 'won', 'pointsdifference'), reverse=True):
            index += 1
            returnTable.append({
                "name": team.name,
                "position": index,
                "stats": team.getEntry()})

        return returnTable


class Match:
    def __init__(self, dict, id):
        self.round = dict.get("Round")
        self.home = dict.get("Home")
        self.away = dict.get("Away")
        self.date = datetime.strptime(dict.get("Date").strip(), "%a %d %b %Y")
        self.scores = dict.get("Scores")
        self.status = "scheduled"
        self.id = id
        self.undoLocked = False

    def updateScore(self, score):
        self.scores.append(score)
        self.undoLocked = False

    def undoScore(self):
        lastIndex = 0
        lastIndex = len(self.scores)
        lastIndex = lastIndex - 1
        lastScore = self.scores[lastIndex]
        scoreType = self.scores[lastIndex].type
        if (scoreType != 'C'):
            self.undoLocked = True

        del self.scores[-1]

    def calcPoints(self):
        homeScore = 0
        awayScore = 0
        homeTries = 0
        awayTries = 0
        homeTryBonusPoints = 0
        homeLosingBonusPoints = 0
        awayTryBonusPoints = 0
        awayLosingBonusPoints = 0
        homePoints = 0
        awayPoints = 0

        # Calculate the total score for each team and the
        # number of tries each team has scored.
        for score in self.scores:
            if score.scorer == "home":
                homeScore += score.value
                match score.type:
                    case "T":
                        homeTries += 1
                    case "PT":
                        homeTries += 1
            else:
                awayScore += score.value
                match score.type:
                    case "T":
                        awayTries += 1
                    case "PT":
                        awayTries += 1

        # Now we have the scores and number of tries, calculate the
        # number of match points each team has gotten from the match
        if homeScore > awayScore:       # Home win
            homePoints = 4
            awayPoints = 0
            if homeScore - awayScore <= 7:
                awayLosingBonusPoints = 1

        elif homeScore < awayScore:     # Away Win
            homePoints = 0
            awayPoints = 4
            if awayScore - homeScore <= 7:
                homeLosingBonusPoints = 1

        else:                           # Draw
            homePoints = 2
            awayPoints = 2

        # Calculate Bonus points.
        if homeTries > 4:
            homeTryBonusPoints += 1

        if awayTries > 4:
            awayTryBonusPoints += 1

        return {
            "homeScore": homeScore,
            "awayScore": awayScore,
            "homePoints": homePoints + homeTryBonusPoints +
            homeLosingBonusPoints,
            "awayPoints": awayPoints + awayTryBonusPoints +
            awayLosingBonusPoints,
            "homeTries": homeTries,
            "awayTries": awayTries,
            "homeTryBonusPoints": homeTryBonusPoints,
            "awayTryBonusPoints": awayTryBonusPoints,
            "homeLosingBonusPoints": homeLosingBonusPoints,
            "awayLosingBonusPoints": awayLosingBonusPoints,
            "homePointsDifference": homeScore - awayScore,
            "awayPointsDifference": awayScore - homeScore,
            "undoLocked": self.undoLocked
            }

    def getMatchDetails(self, currentDate):
        matchPoints = self.calcPoints()
        if (self.date > currentDate):
            self.status = 'scheduled'
        elif (self.date == currentDate):
            self.status = 'in-progress'
        else:
            self.status = 'full-time'

        returnObj = {}
        returnObj['game'] = self.home + " vs " + self.away
        returnObj['home'] = self.home
        returnObj['away'] = self.away
        returnObj['date'] = datetime.strftime(self.date, "%a %d %b %Y")
        returnObj['homeScore'] = matchPoints['homeScore']
        returnObj['awayScore'] = matchPoints['awayScore']
        returnObj['status'] = self.status
        returnObj['ID'] = self.id

        scores = [[]*2, []]
        for score in self.scores:
            if score.scorer == "home":
                scores[0].append(score.type)
                scores[1].append("")
            else:
                scores[1].append(score.type)
                scores[0].append("")

        returnObj['Scores'] = scores
        returnObj['undoLocked'] = self.undoLocked
        # debugPrint(debug, matchPoints)    # TODO: Remove after Debug.
        return returnObj


class Score:
    def __init__(self, type, value, timer, scorer):
        self.type = type
        self.value = value
        self.time = timer
        self.scorer = scorer


class Team:
    def __init__(self, name):
        self.name = name
        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.tries_for = 0
        self.tries_against = 0
        self.conversions_for = 0
        self.conversions_against = 0
        self.dropgoals_for = 0
        self.dropgoals_against = 0
        self.penaltytries_for = 0
        self.penaltytries_against = 0
        self.penalties_for = 0
        self.penalties_against = 0
        self.trybonuspoints = 0
        self.losingbonuspoints = 0
        self.pointsdifference = 0
        self.points = 0

    def getEntry(self):
        return [
            self.name,
            self.played,
            self.won,
            self.drawn,
            self.lost,
            self.trybonuspoints,
            self.losingbonuspoints,
            self.pointsdifference,
            self.points]

    def clearData(self):
        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.tries_for = 0
        self.tries_against = 0
        self.conversions_for = 0
        self.conversions_against = 0
        self.dropgoals_for = 0
        self.dropgoals_against = 0
        self.penaltytries_for = 0
        self.penaltytries_against = 0
        self.penalties_for = 0
        self.penalties_against = 0
        self.trybonuspoints = 0
        self.losingbonuspoints = 0
        self.pointsdifference = 0
        self.points = 0
        


# debug function for testing.
# Add a bunch of match results so that we can see the table and the matches
# being displayed.
# TODO: Remove before Launch
def dbgPopulateMatches(matches):
    matches[0].updateScore(Score("T", 5, datetime.now(), "away"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))
    matches[0].updateScore(Score("C", 2, datetime.now(), "home"))
    matches[0].updateScore(Score("T", 5, datetime.now(), "home"))


@app.route("/")
def home():
    today = datetime.strptime("26 Sep 2026", "%d %b %Y")
    leagueTable = league.getTable("27 Sep 2026")
    matchDetails = []

    for match in league.matches:
        matchDetails.append(match.getMatchDetails(today))

    debugPrint(debug, matchDetails)  # TODO: Remove after Debug AC 2026-09-05
    return render_template(
        "home.html",
        leagueTable=leagueTable,
        matchDetails=matchDetails
        )


@app.route("/matches/<int:matchID>", methods=["GET", "POST"])
def showMatch(matchID):
    today = datetime.strptime("26 Sep 2026", "%d %b %Y")
    if request.method == "POST":
        homescore = request.form.get("homescore", "")
        debugPrint(debug, homescore)
        awayscore = request.form.get("awayscore", "")
        debugPrint(debug, awayscore)
        homeButtonVal = request.form.get("homeButton")
        awayButtonVal = request.form.get("awayButton")
        undoButtonVal = request.form.get("undoButton")
        if (homeButtonVal is not None):
            match homescore:
                case "ht":
                    league.matches[matchID].updateScore(Score("T", 5, datetime.now(), "home"))
                case "hc":
                    league.matches[matchID].updateScore(Score("C", 2, datetime.now(), "home"))
                case "hp":
                    league.matches[matchID].updateScore(Score("P", 3, datetime.now(), "home"))
                case "hg":
                    league.matches[matchID].updateScore(Score("G", 3, datetime.now(), "home"))
                case "hpt":
                    league.matches[matchID].updateScore(Score("PT", 7, datetime.now(), "home"))

        if (awayButtonVal is not None):
            match awayscore:
                case "at":
                    league.matches[matchID].updateScore(Score("T", 5, datetime.now(), "away"))
                case "ac":
                    league.matches[matchID].updateScore(Score("C", 2, datetime.now(), "away"))
                case "ap":
                    league.matches[matchID].updateScore(Score("P", 3, datetime.now(), "away"))
                case "ag":
                    league.matches[matchID].updateScore(Score("G", 3, datetime.now(), "away"))
                case "apt":
                    league.matches[matchID].updateScore(Score("PT", 7, datetime.now(), "away"))

        if (undoButtonVal is not None):
            league.matches[matchID].undoScore()

    displayMatch = league.matches[matchID].getMatchDetails(today)
    return render_template("match.html", match=displayMatch)


# debug print convenience message.
# Make it easier to deactivate messages when not debugging.
def debugPrint(debug, message):
    if debug is True:
        print(message)


# Create the league on startup.
league = League()


# Add some scores for testing.  TODO Remove before launch AC 2026-09-04
dbgPopulateMatches(league.matches)

if __name__ == "__main__":
    app.run(debug=True)
