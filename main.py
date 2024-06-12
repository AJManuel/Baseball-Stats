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
window.geometry("600x600")

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

#-----------------api variables-----------------


#-----------------functions-----------------
# quit function
def quitWindow():
    window.destroy()
    sys.exit(0)
    print("uncomment the destroy method and exit method statements above, then delete this print statement...")

homeTeams = []
awayTeams = []
homePitchers = []
awayPitchers = []
def todaySchedule():
    schedule = statsapi.schedule(start_date=currentDate, end_date=currentDate)
    for haha in schedule:
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

#-----------------matchups-----------------

dateLabel = Label(tab1, text=currentDate, fg='black', font=('arial', 20))
dateLabel.grid(column=2, row=0)

for count, each in enumerate(homeTeams):
    homeTeamLabel = Label(tab1, text=each, fg='black', font=('arial', 20))
    homeTeamLabel.grid(column=1, row=count + 1, pady=10, padx=3)
    print(count)


for amount, each in enumerate(homeTeams):
    atLabel = Label(tab1, text='--->', fg='black', font=('arial', 20))
    atLabel.grid(column=2, row=amount + 1, pady=10, padx=3)
    print(count)

for value, each in enumerate(awayTeams):
    awayTeamLabel = Label(tab1, text=each, fg='black', font=('arial', 20))
    awayTeamLabel.grid(column=3, row=value + 1, pady=10, padx=3)
    print(value)

#-----------------Standings-----------------
divisions = ["AL East", 'AL Central', 'AL West', 'NL East', 'NL Central', 'NL West']
var = StringVar()
swapDivs = customtkinter.CTkComboBox(master=tab3, state='readonly', values=divisions, variable=var)
swapDivs.set('Select Division')
#customtkinter.CTkOptionMenu
#swapDivs['values'] = divisions
#swapDivs['state'] = 'readonly'
swapDivs.grid(row=1, column=3, pady=10, padx=3)



divTeams = customtkinter.CTkLabel(master=tab3, text="Teams")
divTeams.grid(row=2, column=1, columnspan=2,pady=10, padx=3)
divWins = customtkinter.CTkLabel(master=tab3, text='W')
divWins.grid(row=2, column=3, columnspan=1,pady=10, padx=3)
divLosses = customtkinter.CTkLabel(master=tab3, text='L')
divLosses.grid(row=2, column=4, columnspan=1,pady=10, padx=3)
divGbs = customtkinter.CTkLabel(master=tab3, text='Gb')
divGbs.grid(row=2, column=5, columnspan=1,pady=10, padx=3)

def swapAllStats(*args):
    currentDiv = swapDivs.get()
    print(currentDiv)
    if currentDiv == 'AL East':
        drawAlEastStandings()
    elif currentDiv == 'AL Central':
        drawAlCentralStandings()
    elif currentDiv == 'AL West':
        drawAlWestStandings()
    elif currentDiv == 'NL East':
        drawNlEastStandings()
    elif currentDiv == 'NL Central':
        drawNlCentralStandings()
    else:
        drawNlWestStandings()

def drawAlEastStandings():
    
    for count, each in enumerate(aleTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(aleTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(aleTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(aleTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawAlCentralStandings():
    for count, each in enumerate(alcTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(alcTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alcTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alcTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawAlWestStandings():
    for count, each in enumerate(alwTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(alwTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alwTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(alwTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)


def drawNlEastStandings():
    for count, each in enumerate(nleTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nleTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nleTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nleTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawNlCentralStandings():
    for count, each in enumerate(nlcTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nlcTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlcTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlcTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

def drawNlWestStandings():
    for count, each in enumerate(nlwTeamNames):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)

    for count, each in enumerate(nlwTeamWins):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlwTeamLosses):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)

    for count, each in enumerate(nlwTeamGbs):
        team1 = customtkinter.CTkLabel(master=tab3, text=each)
        team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)


var.trace('w', swapAllStats)
#swapAllStats()
#swapDivs.bind("<<ComboboxSelected>>", swapAllStats())

# for count, each in enumerate(aleTeamNames):
#     team1 = customtkinter.CTkLabel(master=tab3, text=each)
#     team1.grid(row=count + 3, column=1, columnspan=2, pady=10, padx=3)
#
# for count, each in enumerate(aleTeamWins):
#     team1 = customtkinter.CTkLabel(master=tab3, text=each)
#     team1.grid(row=count + 3, column=3, columnspan=1, pady=10, padx=3)
#
# for count, each in enumerate(aleTeamLosses):
#     team1 = customtkinter.CTkLabel(master=tab3, text=each)
#     team1.grid(row=count + 3, column=4, columnspan=1, pady=10, padx=3)
#
# for count, each in enumerate(aleTeamGbs):
#     team1 = customtkinter.CTkLabel(master=tab3, text=each)
#     team1.grid(row=count + 3, column=5, columnspan=1, pady=10, padx=3)

# add quit button
quit_button = tk.Button(tab1, text='Quit', command=quitWindow).grid(row=10, column=2, sticky='n')




# start the GUI --> Leave here at the end!
notebook.pack()
window.mainloop()
