import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter
import requests
import statsapi
import datetime
from datetime import date
import notebook

#basic tk setup
window = customtkinter.CTk()

window.title("The Score")

window.geometry("700x700")

#window.resizable(0,0)

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")



notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Matchups")
notebook.add(tab2, text="Stats")
notebook.add(tab3, text="Standings")


#time setup
today = datetime.date.today()
currentDate = (f'{today.month}/{today.day}/{today.year}')
print(currentDate)
tomorrow = today + datetime.timedelta(days=1)


#-----------------functions-----------------
homeTeams = []
awayTeams = []
homePitchers = []
awayPitchers = []
homeScores = []
awayScores = []
homeRoster = []
homeTeamId = []
awayTeamId = []
gameIds = []
schedule = statsapi.schedule(start_date=currentDate, end_date=currentDate)
print(schedule)
def todaySchedule():
    for haha in schedule:
        for each7 in haha:
            if each7 == 'game_id':
                global gameIds
                theGameIds = haha[each7]
                gameIds.append(theGameIds)
        for each2 in haha:
            if each2 == 'home_name':
                global homeTeams
                theHomeTeam = haha[each2]
                homeTeams.append(theHomeTeam)
        for thing2 in haha:
            if thing2 == 'home_probable_pitcher':
                global homePitchers
                theHomePitcher = haha[thing2]
                homePitchers.append(theHomePitcher)
        for thing4 in haha:
            if thing4 == 'home_score':
                global homeScores
                theHomeScore = haha[thing4]
                homeScores.append(theHomeScore)
        for thing5 in haha:
            if thing5 == 'home_id':
                global homeTeamId
                theHomeTeamId = haha[thing5]
                homeTeamId.append(theHomeTeamId)
        for each3 in haha:
            if each3 == 'away_name':
                global awayTeams
                theAwayTeam = haha[each3]
                awayTeams.append(theAwayTeam)
        for thing3 in haha:
            if thing3 == 'away_probable_pitcher':
                global awayPitchers
                theAwayPitcher = haha[thing3]
                awayPitchers.append(theAwayPitcher)
        for thing4 in haha:
            if thing4 == 'away_score':
                global awayScores
                theAwayScore = haha[thing4]
                awayScores.append(theAwayScore)
        for thing6 in haha:
            if thing6 == 'away_id':
                global awayTeamId
                theAwayTeamId = haha[thing6]
                awayTeamId.append(theAwayTeamId)
        #print(f'{homeTeams} --> {awayTeams}')

todaySchedule()


#-----------------standings functions-----------------
aleTeamNames = []
aleTeamWins = []
aleTeamLosses = []
aleTeamGbs = []

def alEastStandingsFunc():
    alEastStandings = statsapi.standings_data(leagueId="103", division="ale", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global aleTeamNames
    global aleTeamWins
    global aleTeamLosses
    global aleTeamGbs
    for each in alEastStandings[201]['teams']:
        eachTeamName = each['name']
        aleTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        aleTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        aleTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        aleTeamGbs.append(eachTeamGbs)
alEastStandingsFunc()

alcTeamNames = []
alcTeamWins = []
alcTeamLosses = []
alcTeamGbs = []
def alCentralStandingsFunc():
    alCentralStandings = statsapi.standings_data(leagueId="103", division="alc", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global alcTeamNames
    global alcTeamWins
    global alcTeamLosses
    global alcTeamGbs
    for each in alCentralStandings[202]['teams']:
        eachTeamName = each['name']
        alcTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        alcTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        alcTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        alcTeamGbs.append(eachTeamGbs)
alCentralStandingsFunc()


alwTeamNames = []
alwTeamWins = []
alwTeamLosses = []
alwTeamGbs = []
def alWestStandingsFunc():
    alWestStandings = statsapi.standings_data(leagueId="103", division="alw", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global alwTeamNames
    global alwTeamWins
    global alwTeamLosses
    global alwTeamGbs
    for each in alWestStandings[200]['teams']:
        eachTeamName = each['name']
        alwTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        alwTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        alwTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        alwTeamGbs.append(eachTeamGbs)
alWestStandingsFunc()


nleTeamNames = []
nleTeamWins = []
nleTeamLosses = []
nleTeamGbs = []
def nlEastStandingsFunc():
    nlEastStandings = statsapi.standings_data(leagueId="104", division="nle", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global nleTeamNames
    global nleTeamWins
    global nleTeamLosses
    global nleTeamGbs
    for each in nlEastStandings[204]['teams']:
        eachTeamName = each['name']
        nleTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        nleTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        nleTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        nleTeamGbs.append(eachTeamGbs)
nlEastStandingsFunc()


nlcTeamNames = []
nlcTeamWins = []
nlcTeamLosses = []
nlcTeamGbs = []
def nlCentralStandingsFunc():
    nlCentralStandings = statsapi.standings_data(leagueId="104", division="nlc", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global nlcTeamNames
    global nlcTeamWins
    global nlcTeamLosses
    global nlcTeamGbs
    for each in nlCentralStandings[205]['teams']:
        eachTeamName = each['name']
        nlcTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        nlcTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        nlcTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        nlcTeamGbs.append(eachTeamGbs)
nlCentralStandingsFunc()


nlwTeamNames = []
nlwTeamWins = []
nlwTeamLosses = []
nlwTeamGbs = []

def nlWestStandingsFunc():
    nlWestStandings = statsapi.standings_data(leagueId="104", division="nlw", include_wildcard=True, season=2024,
                                              standingsTypes=None, date=None)
    global nlwTeamNames
    global nlwTeamWins
    global nlwTeamLosses
    global nlwTeamGbs
    for each in nlWestStandings[203]['teams']:
        eachTeamName = each['name']
        nlwTeamNames.append(eachTeamName)
        eachTeamWins = each['w']
        nlwTeamWins.append(eachTeamWins)
        eachTeamLosses = each['l']
        nlwTeamLosses.append(eachTeamLosses)
        eachTeamGbs = each['gb']
        nlwTeamGbs.append(eachTeamGbs)
nlWestStandingsFunc()


#-----------------top5leaders functions-----------------

top5opsLeadersNames = []
top5opsLeadersStats = []
def top5opsFunc():
    top5ops = statsapi.league_leader_data('onBasePlusSlugging', statGroup='hitting', limit=5, season=2024)
    global top5opsLeadersNames
    global top5opsLeadersStats
    for each in top5ops:
        top5opsLeadersNames.append(each[1])
        top5opsLeadersStats.append(each[3])
top5opsFunc()

top5eraLeadersNames = []
top5eraLeadersStats = []
def top5eraFunc():
    top5era = statsapi.league_leader_data('earnedRunAverage', statGroup='pitching', limit=5, season=2024)
    global top5eraLeadersNames
    global top5eraLeadersStats
    for each in top5era:
        top5eraLeadersNames.append(each[1])
        top5eraLeadersStats.append(each[3])
top5eraFunc()

top5hrLeadersNames = []
top5hrLeadersStats = []
def top5hrFunc():
    top5hr = statsapi.league_leader_data('homeRuns', statGroup='hitting', limit=5, season=2024)
    global top5hrLeadersNames
    global top5hrLeadersStats
    for each in top5hr:
        top5hrLeadersNames.append(each[1])
        top5hrLeadersStats.append(each[3])
top5hrFunc()

top5runsLeadersNames = []
top5runsLeadersStats = []
def top5runsFunc():
    top5runs = statsapi.league_leader_data('runs', statGroup='hitting', limit=5, season=2024)
    global top5runsLeadersNames
    global top5runsLeadersStats
    for each in top5runs:
        top5runsLeadersNames.append(each[1])
        top5runsLeadersStats.append(each[3])
top5runsFunc()

top5rbiLeadersNames = []
top5rbiLeadersStats = []
def top5rbiFunc():
    top5rbi = statsapi.league_leader_data('runsBattedIn', statGroup='hitting', limit=5, season=2024)
    global top5rbiLeadersNames
    global top5rbiLeadersStats
    for each in top5rbi:
        top5rbiLeadersNames.append(each[1])
        top5rbiLeadersStats.append(each[3])
top5rbiFunc()

top5winsLeadersNames = []
top5winsLeadersStats = []
def top5winsFunc():
    top5wins = statsapi.league_leader_data('wins', statGroup='pitching', limit=5, season=2024)
    global top5winsLeadersNames
    global top5winsLeadersStats
    for each in top5wins:
        top5winsLeadersNames.append(each[1])
        top5winsLeadersStats.append(each[3])
top5winsFunc()


top5averageLeadersNames = []
top5averageLeadersStats = []
def top5averageFunc():
    top5average = statsapi.league_leader_data('avg', statGroup='hitting', limit=5, season=2024)
    global top5averageLeadersNames
    global top5averageLeadersStats
    for each in top5average:
        top5averageLeadersNames.append(each[1])
        top5averageLeadersStats.append(each[3])
top5averageFunc()

top5savesLeadersNames = []
top5savesLeadersStats = []
def top5savesFunc():
    top5saves = statsapi.league_leader_data('saves', statGroup='pitching', limit=5, season=2024)
    global top5savesLeadersNames
    global top5savesLeadersStats
    for each in top5saves:
        top5savesLeadersNames.append(each[1])
        top5savesLeadersStats.append(each[3])
top5savesFunc()

top = ""

#----------------Leaders Page----------------
statistics = ['AVG', 'OPS', 'RUNS', 'RBI', 'HR', 'WINS', 'ERA', 'SAVES']
swapStatBox = customtkinter.CTkComboBox(master=tab2, state='readonly', values=statistics)
swapStatBox.grid(row=0, column=0)

leadersNamesLabel = customtkinter.CTkLabel(master=tab2, text='Name')
leadersNamesLabel.grid(row=1, column=0, columnspan=2)

LeadersStatLabel = customtkinter.CTkLabel(master=tab2, text='Stat')
LeadersStatLabel.grid(row=1, column=3)

allPlayerNames = []
for count, each in enumerate(top5averageLeadersNames):
    player1 = customtkinter.CTkLabel(master=tab2, text=each)
    player1.grid(row=count + 3, column=0, columnspan=2, pady=10, padx=3)
    allPlayerNames.append(player1)

allPlayerStats = []
for count, each in enumerate(top5averageLeadersStats):
    stats1 = customtkinter.CTkLabel(master=tab2, text=each)
    stats1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    allPlayerStats.append(stats1)

def drawAverageStats():
    global top5averageLeadersNames
    global top5averageLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5averageLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5averageLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawOpsStats():
    global top5opsLeadersNames
    global top5opsLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5opsLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5opsLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawRunsStats():
    global top5runsLeadersNames
    global top5runsLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5runsLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5runsLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawRbisStats():
    global top5rbiLeadersNames
    global top5rbiLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5rbiLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5rbiLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawHrsStats():
    global top5hrLeadersNames
    global top5hrLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5hrLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5hrLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawWinsStats():
    global top5winsLeadersNames
    global top5winsLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5winsLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5winsLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawEraStats():
    global top5eraLeadersNames
    global top5eraLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5eraLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5eraLeadersStats):
        allPlayerStats[count].configure(text=each)

def drawSavesStats():
    global top5savesLeadersNames
    global top5savesLeadersStats
    global allPlayerStats
    global allPlayerNames

    for count, each in enumerate(top5savesLeadersNames):
        allPlayerNames[count].configure(text=each)

    for count, each in enumerate(top5savesLeadersStats):
        allPlayerStats[count].configure(text=each)

def swapAllNumbers():
    currentStat = swapStatBox.get()
    print(currentStat)
    if currentStat == 'AVG':
        drawAverageStats()
    elif currentStat == 'OPS':
        drawOpsStats()
    elif currentStat == 'RUNS':
        drawRunsStats()
    elif currentStat == 'RBI':
        drawRbisStats()
    elif currentStat == 'HR':
        drawHrsStats()
    elif currentStat == 'WINS':
        drawWinsStats()
    elif currentStat == 'ERA':
        drawEraStats()
    elif currentStat == 'SAVES':
        drawSavesStats()
    else:
        pass

changeStatButton = customtkinter.CTkButton(master=tab2, text='Update', command=swapAllNumbers)
changeStatButton.grid(row=8, column=1, columnspan=2, pady=10, padx=3)

def open_popup():
    global top
    top = Toplevel(tab2)
    top.geometry("300x410")
    top.title("Child_Window")
    #window.withdraw()

def viewMatchupFunc(t):
    open_popup()
    global awayTeams
    #print(t)
    if matchupButtons[0]:
        teamName = t
        for count, each in enumerate(homeTeams):
            schedule = statsapi.schedule(sportId=1)
            games = [game['game_id'] for game in schedule]
            params = {
                "sportId": 1,
                "gamePk": gameIds[count],
                "hydrate": "lineups",
            }
            gamedata = statsapi.get("schedule", params)
            teamdata = gamedata['dates'][0]['games'][0]['lineups']
            print(teamdata)
            print('herer')
            lineups = {}
            home = []
            away = []
            if len(teamdata) == 0:
                 pass
            elif len(teamdata) != 0:
                for player in teamdata['homePlayers']:
                    name = player['fullName']
                    home.append(name)
                lineups['home'] = home

            if len(teamdata) == 0:
                pass
            elif len(teamdata) != 0:
                if teamdata['awayPlayers'] != '':
                    for player in teamdata['awayPlayers']:
                        name = player['fullName']
                        away.append(name)
                    lineups['away'] = away


            if each == teamName:
                childWindowLabelHome = customtkinter.CTkLabel(master=top, text=t)
                childWindowLabelHome.grid(row=1, column=3)

                childWindowProbablePitcherHome = customtkinter.CTkLabel(master=top, text=homePitchers[count])
                childWindowProbablePitcherHome.grid(row=2, column=3)
                if homePitchers[count] == '':
                    childWindowProbablePitcherHome.configure(text='TBD')

                scoreFont = ('arial', 25, 'bold')
                childWindowHomeScore = customtkinter.CTkLabel(master=top, text=homeScores[count], font=scoreFont)
                childWindowHomeScore.grid(row=3, column=3)

                for num in range(len(home)):
                    childWindowHomeRoster = customtkinter.CTkLabel(master=top, text=f'{num + 1}. {home[0 + num]}')
                    childWindowHomeRoster.grid(row=4 + num, column=3)
                #print(teamName)
                childWindowLabelAway = customtkinter.CTkLabel(master=top, text=awayTeams[count])
                childWindowLabelAway.grid(row=1, column=1)

                childWindowProbablePitcherAway = customtkinter.CTkLabel(master=top, text=awayPitchers[count])
                childWindowProbablePitcherAway.grid(row=2, column=1)
                if awayPitchers[count] == '':
                    childWindowProbablePitcherAway.configure(text='TBD')

                childWindowAwayScore = customtkinter.CTkLabel(master=top, text=awayScores[count], font=scoreFont)
                childWindowAwayScore.grid(row=3, column=1)

                for num in range(len(away)):
                    childWindowAwayRoster = customtkinter.CTkLabel(master=top, text=f'{num + 1}. {away[0 + num]}')
                    childWindowAwayRoster.grid(row=4 + num, column=1)
                #print(teamName)
    elif matchupButtons[1]:
        homeRoster = statsapi.roster(teamId=homeTeamId[1], season=2024, date=currentDate)
        awayRoster = statsapi.roster(teamId=awayTeamId[1], season=2024, date=currentDate)
        teamName = t
        for each in homeTeams:
            if each == teamName:
                childWindowLabelHome = customtkinter.CTkLabel(master=top, text=t)
                childWindowLabelHome.grid(row=0, column=0)
                #print(teamName)
                childWindowLabelAway = customtkinter.CTkLabel(master=top, text=awayTeams[1])
                childWindowLabelAway.grid(row=1, column=1)
    else:
        pass
#print(tester19)
#-----------------matchups-----------------
matchupButtons = []
homeTeamsMatchups = []
dateLabel = customtkinter.CTkLabel(tab1, text=currentDate)
dateLabel.grid(column=2, row=0)

for value, each in enumerate(awayTeams):
    awayTeamLabel = customtkinter.CTkLabel(master=tab1, text=each)
    awayTeamLabel.grid(column=1, row=value + 1, pady=10, padx=3)
    #print(value)

for value, each in enumerate(awayTeams):
    atLabel = customtkinter.CTkLabel(master=tab1, text="@")
    atLabel.grid(column=2, row=value + 1, pady=10, padx=3)
    #print(value)

for count, each in enumerate(homeTeams):
    homeTeamLabel = customtkinter.CTkLabel(master=tab1, text=each)
    homeTeamLabel.grid(column=3, row=count + 1, pady=10, padx=1)
    eachTeam = homeTeamLabel.cget('text')
    homeTeamsMatchups.append(eachTeam)
    #print(homeTeamsMatchups)

for amount, each in enumerate(homeTeams):
    #lambda t= "Button-2 Clicked": get_button(t)
    matchupButton = customtkinter.CTkButton(master=tab1, text='View Matchup', command=lambda t=homeTeams[amount] : viewMatchupFunc(t))
    matchupButton.grid(column=4, columnspan=2, row=amount + 1, pady=10, padx=5)
    matchupButtons.append(matchupButton)
    #print(matchupButton)




#-----------------Standings-----------------
divisions = ["AL East", 'AL Central', 'AL West', 'NL East', 'NL Central', 'NL West']
#var = StringVar()
# swapDivs = customtkinter.CTkComboBox(master=tab3, state='readonly', values=divisions, variable=var)
swapDivs = customtkinter.CTkComboBox(master=tab3, state='readonly', values=divisions)

# swapDivs.set('AL East')
swapDivs.grid(row=1, column=3, pady=10, padx=3)


divTeams = customtkinter.CTkLabel(master=tab3, text="Teams")
divTeams.grid(row=2, column=1, columnspan=2,pady=10, padx=3)
divWins = customtkinter.CTkLabel(master=tab3, text='W')
divWins.grid(row=2, column=3, columnspan=1,pady=10, padx=3)
divLosses = customtkinter.CTkLabel(master=tab3, text='L')
divLosses.grid(row=2, column=4, columnspan=1,pady=10, padx=3)
divGbs = customtkinter.CTkLabel(master=tab3, text='Gb')
divGbs.grid(row=2, column=5, columnspan=1,pady=10, padx=3)

def drawAlEastStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(aleTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(aleTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(aleTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(aleTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)


def drawAlCentralStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(alcTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(alcTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alcTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alcTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawAlWestStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(alwTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(alwTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alwTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alwTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)
    # for count, each in enumerate(alwTeamNames):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
    #
    # for count, each in enumerate(alwTeamWins):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(alwTeamLosses):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(alwTeamGbs):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)


def drawNlEastStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(nleTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nleTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nleTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nleTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)
    # for count, each in enumerate(nleTeamNames):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
    #
    # for count, each in enumerate(nleTeamWins):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nleTeamLosses):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nleTeamGbs):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawNlCentralStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(nlcTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nlcTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlcTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlcTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)
    # for count, each in enumerate(nlcTeamNames):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
    #
    # for count, each in enumerate(nlcTeamWins):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nlcTeamLosses):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nlcTeamGbs):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawNlWestStandings():
    global allTeamLabels
    global allTeamWinsLabels
    global allTeamLossesLabels
    global allTeamGbsLabels

    for count, each in enumerate(nlwTeamNames):
        allTeamLabels[count].configure(text=each)
        print(each)
        # team1 = customtkinter.CTkLabel(master=tab3, text=each)
        # team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nlwTeamWins):
        allTeamWinsLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlwTeamLosses):
        allTeamLossesLabels[count].configure(text=each)
        # team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlwTeamGbs):
        allTeamGbsLabels[count].configure(text=each)
        #team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)
    # for count, each in enumerate(nlwTeamNames):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
    #
    # for count, each in enumerate(nlwTeamWins):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nlwTeamLosses):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
    #
    # for count, each in enumerate(nlwTeamGbs):
    #     team1 = customtkinter.CTkLabel(master=tab3, text=each)
    #     team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

# def swapAllStats(*args):
def swapAllStats():
    currentDiv = swapDivs.get()
    print(currentDiv)
    if currentDiv == 'AL East':
        print('work')
        drawAlEastStandings()
    elif currentDiv == 'AL Central':
        print('working')
        drawAlCentralStandings()
    elif currentDiv == 'AL West':
        drawAlWestStandings()
    elif currentDiv == 'NL East':
        drawNlEastStandings()
    elif currentDiv == 'NL Central':
        drawNlCentralStandings()
    elif currentDiv == 'NL West':
        drawNlWestStandings()
    else:
        pass

changeDivButton = customtkinter.CTkButton(master=tab3, text='Update', command=swapAllStats)
changeDivButton.grid(row=8, column=2, columnspan=2, pady=10, padx=3)

allTeamLabels = []
for count, each in enumerate(aleTeamNames):
    team1 = customtkinter.CTkLabel(master=tab3, text=each)
    team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
    allTeamLabels.append(team1)

allTeamWinsLabels = []
for count, each in enumerate(aleTeamWins):
    wins1 = customtkinter.CTkLabel(master=tab3, text=each)
    wins1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
    allTeamWinsLabels.append(wins1)

allTeamLossesLabels = []
for count, each in enumerate(aleTeamLosses):
    losses1 = customtkinter.CTkLabel(master=tab3, text=each)
    losses1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
    allTeamLossesLabels.append(losses1)

allTeamGbsLabels = []
for count, each in enumerate(aleTeamGbs):
    gbs1 = customtkinter.CTkLabel(master=tab3, text=each)
    gbs1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)
    allTeamGbsLabels.append(gbs1)

#var.trace('w', swapAllStats)
#swapAllStats()
#swapDivs.bind("<<ComboboxSelected>>", swapAllStats())

# add quit button
#quit_button = tk.Button(tab1, text='Quit', command=quitWindow).grid(row=10, column=2, sticky='n')




# start the GUI --> Leave here at the end!
notebook.pack()

window.mainloop()
