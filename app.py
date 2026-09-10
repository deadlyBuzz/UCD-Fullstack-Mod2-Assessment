from flask import Flask, render_template, abort, request, flash, redirect
from datetime import datetime, timedelta
from operator import attrgetter
from static.data.allMatches import allMatches, Calendar
import os

app = Flask(__name__)
# app.secret_key = os.environ['SECRET_KEY']  # Disabled during dev so Debugger can attach.

leagueTable = ""
debug = False
allmatches = allMatches
calendar = Calendar()


class League:
    def __init__(self):
        self.matches = []
        self.table = [
                Team("Benetton", "green", "white", "success"),
                Team("Bulls", "blue", "white", "info"),
                Team("Cardiff", "blue", "navy", "primary"),
                Team("Connacht", "green", "white", "success"),
                Team("Dragons", "black", "yellow", "warning"),
                Team("Edinburgh", "navy", "orange", "primary"),
                Team("Glasgow Warriors", "black", "blue", "dark"),
                Team("Leinster", "blue", "white", "info"),
                Team("Lions", "red", "white", "danger"),
                Team("Munster", "red", "navy", "danger"),
                Team("Ospreys", "black", "white", "dark"),
                Team("Scarlets", "red", "red", "danger"),
                Team("Stormers", "blue", "white", "info"),
                Team("Sharks", "black", "grey", "dark"),
                Team("Ulster", "white", "red", "light"),
                Team("Zebre Parma", "yellow", "blue", "warning")
            ]

        # Populate Matches Data.
        matchID = 0
        for entry in allmatches:
            # Match object per entry in allmatches
            self.matches.append(Match(entry, matchID))
            matchID += 1

    def getTable(self, date):
        index = 0
        prevTableBuilt = False
        selectedDate = date.startDate
        prevTable = []
        for team in self.table:
            team.clearData()
        for match in self.matches:
            if ((prevTableBuilt is False) and (match.date >= selectedDate)):
                prevTable = self.table
                prevTableBuilt = True

            matchData = match.calcPoints()
            for team in self.table:
                if (match.date < (date.endDate)):
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
                        team.conversions_for += matchData.get('homeConversions')
                        team.conversions_against += matchData.get('awayConversions')
                        team.dropgoals_for += matchData.get('homeDropgoals')
                        team.dropgoals_against += matchData.get('awayDropgoals')
                        team.penalties_for += matchData.get('homePenalties')
                        team.penalties_against += matchData.get('awayPenalties')

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
                        team.conversions_for += matchData.get('awayConversions')
                        team.conversions_against += matchData.get('homeConversions')
                        team.dropgoals_for += matchData.get('awayDropgoals')
                        team.dropgoals_against += matchData.get('homeDropgoals')
                        team.penalties_for += matchData.get('awayPenalties')
                        team.penalties_against += matchData.get('homePenalties')

                team.setRecords(match)

        returnTable = []
        prevReturnTable = []

        for team in sorted(prevTable, key=attrgetter('points', 'won', 'pointsdifference'), reverse=True):
            index += 1
            prevReturnTable.append({
                "name": team.name,
                "position": index,
                "stats": team.getEntry()})

        index = 0

        for team in sorted(self.table, key=attrgetter('points', 'won', 'pointsdifference'), reverse=True):
            index += 1
            if len(prevReturnTable) > 0:
                lastWeek = next(item for item in prevReturnTable if item['name'] == team.name)
            tableDelta = lastWeek.get('position')
            returnTable.append({
                "name": team.name,
                "position": index,
                "tabledelta": tableDelta,
                "stats": team.getEntry()})

        return returnTable

    def getTeam(self, teamName):
        return next((team for team in self.table if team.name == teamName), None)


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
        homeConversions = 0
        awayConversions = 0
        homeDropgoals = 0
        awayDropgoals = 0
        homePenalties = 0
        awayPenalties = 0
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
                    case "C":
                        homeConversions += 1
                    case "P":
                        homePenalties += 1
                    case "DG":
                        homeDropgoals += 1

            else:
                awayScore += score.value
                match score.type:
                    case "T":
                        awayTries += 1
                    case "PT":
                        awayTries += 1
                    case "C":
                        awayConversions += 1
                    case "P":
                        awayPenalties += 1
                    case "DG":
                        awayDropgoals += 1

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
        if homeTries >= 4:
            homeTryBonusPoints += 1

        if awayTries >= 4:
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
            "homeConversions": homeConversions,
            "awayConversions": awayConversions,
            "homePenalties": homePenalties,
            "awayPenalties": awayPenalties,
            "homeDropgoals": homeDropgoals,
            "awayDropgoals": awayDropgoals,
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
    def __init__(self, name, primaryColour, secondaryColour, theme):
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
        self.primaryColour = primaryColour
        self.secondaryColour = secondaryColour
        self.theme = theme
        self.stats = {"biggestwin": {"Score": 0, "match": "Not Recorded"},
                      "biggestloss": {"Score": 0, "match": "Not Recorded"},
                      "mosttriesscored": {"Score": 0, "match": "Not Recorded"},
                      "mosttriesconceded": {"Score": 0, "match": "Not Recorded"},
                      "highestscore": {"Score": 0, "match": "Not Recorded"},
                      "highestconceded": {"Score": 0, "match": "Not Recorded"}}

    def getEntry(self):
        return [
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

    def setRecords(self, match):
        # Check if team is home or away
        matchName = ""
        matchData = match.calcPoints()
        if match.home == self.name:
            matchName = "At Home to " + match.away + " " + datetime.strftime(match.date, "%d %b %Y")
            pointsDiff = matchData.get("homeScore") - matchData.get("awayScore")
            # Tries Scored
            if matchData.get("homeTries") > self.stats["mosttriesscored"]["Score"]:
                self.stats["mosttriesscored"]["Score"] = matchData.get("homeTries")
                self.stats["mosttriesscored"]["match"] = matchName
            # Tries Conceded
            if matchData.get("awayTries") > self.stats["mosttriesconceded"]["Score"]:
                self.stats["mosttriesconceded"]["Score"] = matchData.get("awayTries")
                self.stats["mosttriesconceded"]["match"] = matchName
            # Highest Score
            if matchData.get("homeScore") > self.stats["highestscore"]["Score"]:
                self.stats["highestscore"]["Score"] = matchData.get("homeScore")
                self.stats["highestscore"]["match"] = matchName
            # Highest Conceded
            if matchData.get("awayScore") > self.stats["highestconceded"]["Score"]:
                self.stats["highestconceded"]["Score"] = matchData.get("awayScore")
                self.stats["highestconceded"]["match"] = matchName
            # biggest win
            if pointsDiff > self.stats["biggestwin"]["Score"]:
                self.stats["biggestwin"]["Score"] = pointsDiff
                self.stats["biggestwin"]["match"] = matchName
            # biggest Loss
            if pointsDiff < self.stats["biggestloss"]["Score"]: 
                self.stats["biggestloss"]["Score"] = pointsDiff
                self.stats["biggestloss"]["match"] = matchName

        if match.away == self.name:
            matchName = "Away to " + match.away + " " + datetime.strftime(match.date, "%d %b %Y")
            pointsDiff = matchData.get("awayScore") - matchData.get("homeScore")
            # Tries Scored
            if matchData.get("awayTries") > self.stats["mosttriesscored"]["Score"]:
                self.stats["mosttriesscored"]["Score"] = matchData.get("awayTries")
                self.stats["mosttriesscored"]["match"] = matchName
            # Tries Conceded
            if matchData.get("homeTries") > self.stats["mosttriesconceded"]["Score"]:
                self.stats["mosttriesconceded"]["Score"] = matchData.get("homeTries")
                self.stats["mosttriesconceded"]["match"] = matchName
            # Highest Score
            if matchData.get("awayScore") > self.stats["highestscore"]["Score"]:
                self.stats["highestscore"]["Score"] = matchData.get("awayScore")
                self.stats["highestscore"]["match"] = matchName
            # Highest Conceded
            if matchData.get("homeScore") > self.stats["highestconceded"]["Score"]:
                self.stats["highestconceded"]["Score"] = matchData.get("homeScore")
                self.stats["highestconceded"]["match"] = matchName
            # biggest win
            if pointsDiff > self.stats["biggestwin"]["Score"]:
                self.stats["biggestwin"]["Score"] = pointsDiff
                self.stats["highestconceded"]["match"] = matchName
            # biggest Loss
            if pointsDiff < self.stats["biggestloss"]["Score"]: 
                self.stats["biggestloss"]["Score"] = pointsDiff
                self.stats["biggestloss"]["match"] = matchName


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
    today = datetime.today()
    weekDetails = calendar.getRound(datetime.today())
    weekNo = weekDetails.Round

    leagueTable = league.getTable(calendar.rounds[weekNo-1])
    matchDetails = []

    for match in league.matches:
        matchDetails.append(match.getMatchDetails(today))

    debugPrint(debug, matchDetails)  # TODO: Remove after Debug AC 2026-09-05
    return render_template(
        "home.html",
        leagueTable=leagueTable,
        matchDetails=matchDetails,
        weekData=weekDetails
        )


@app.route("/WeekNo/<int:weekNumber>")
def homeSelectedWeek(weekNumber):
    today = datetime.today()

    if weekNumber >= 1:
        weekDetails = next((week for week in calendar.rounds if week.Round == weekNumber ),None)
    else:
        weekDetails = next((week for week in calendar.rounds if week.Round == 1 ),None)

    leagueTable = league.getTable(next(week for week in calendar.rounds if week.Round == weekNumber ))
    matchDetails = []

    for match in league.matches:
        matchDetails.append(match.getMatchDetails(today))

    debugPrint(debug, matchDetails)  # TODO: Remove after Debug AC 2026-09-05
    return render_template(
        "home.html",
        leagueTable=leagueTable,
        matchDetails=matchDetails,
        weekData=weekDetails
        )


@app.route("/matches/<int:matchID>", methods=["GET", "POST"])
def showMatch(matchID):
    today = datetime.today()
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


@app.route("/teams/<teamname>")
def displayTeam(teamname, queryDate=datetime.today()):
    today = queryDate
    matchDetails = []
    leagueTable = league.getTable(datetime.strftime(queryDate, "%d %b %Y"))
    for match in league.matches:
        if (match.home == teamname) or ((match.away == teamname)):
            matchDetails.append(match.getMatchDetails(today))

    team = league.getTeam(teamname)
    return render_template("team.html", leagueTable=leagueTable, matchDetails=matchDetails, team=team)


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
