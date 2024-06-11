from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
import statsapi
import datetime
from datetime import date
import notebook

#basic tk setup
window = tk.Tk()
window.title("The Score")
window.geometry("600x600")

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Matchups")
notebook.add(tab2, text="Standings")
notebook.add(tab3, text="Stats")


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
def todaySchedule():
    schedule = statsapi.schedule(start_date=currentDate, end_date=currentDate)
    for haha in schedule:
        for each2 in haha:
            if each2 == 'home_name':
                global homeTeams
                theHomeTeam = haha[each2]
                homeTeams.append(theHomeTeam)
        for each3 in haha:
            if each3 == 'away_name':
                global awayTeams
                theAwayTeam = haha[each3]
                awayTeams.append(theAwayTeam)
        #print(f'{homeTeams} --> {awayTeams}')

def todayStandings():
    standings = statsapi.standings(date=currentDate)
    #print(standings)
todaySchedule()
#print(homeTeams)

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
print(alcTeamNames)
print(alcTeamWins)
print(alcTeamLosses)
print(alcTeamGbs)

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
print(alwTeamNames)
print(alwTeamWins)
print(alwTeamLosses)
print(alwTeamGbs)

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

top5eraLeadersNames = []
top5eraLeadersStats = []
def top5eraFunc():
    top5era = statsapi.league_leader_data('earnedRunAverage', statGroup='pitching', limit=5, season=2024)
    global top5eraLeadersNames
    global top5eraLeadersStats
    for each in top5era:
        top5eraLeadersNames.append(each[1])
        top5eraLeadersStats.append(each[3])

top5hrLeadersNames = []
top5hrLeadersStats = []
def top5hrFunc():
    top5hr = statsapi.league_leader_data('homeRuns', statGroup='hitting', limit=5, season=2024)
    global top5hrLeadersNames
    global top5hrLeadersStats
    for each in top5hr:
        top5hrLeadersNames.append(each[1])
        top5hrLeadersStats.append(each[3])

top5runsLeadersNames = []
top5runsLeadersStats = []
def top5runsFunc():
    top5runs = statsapi.league_leader_data('runs', statGroup='hitting', limit=5, season=2024)
    global top5runsLeadersNames
    global top5runsLeadersStats
    for each in top5runs:
        top5runsLeadersNames.append(each[1])
        top5runsLeadersStats.append(each[3])

top5rbiLeadersNames = []
top5rbiLeadersStats = []
def top5rbiFunc():
    top5rbi = statsapi.league_leader_data('runsBattedIn', statGroup='hitting', limit=5, season=2024)
    global top5rbiLeadersNames
    global top5rbiLeadersStats
    for each in top5rbi:
        top5rbiLeadersNames.append(each[1])
        top5rbiLeadersStats.append(each[3])

top5winsLeadersNames = []
top5winsLeadersStats = []
def top5winsFunc():
    top5wins = statsapi.league_leader_data('wins', statGroup='pitching', limit=5, season=2024)
    global top5winsLeadersNames
    global top5winsLeadersStats
    for each in top5wins:
        top5winsLeadersNames.append(each[1])
        top5winsLeadersStats.append(each[3])


top5averageLeadersNames = []
top5averageLeadersStats = []
def top5averageFunc():
    top5average = statsapi.league_leader_data('avg', statGroup='hitting', limit=5, season=2024)
    global top5averageLeadersNames
    global top5averageLeadersStats
    for each in top5average:
        top5averageLeadersNames.append(each[1])
        top5averageLeadersStats.append(each[3])


top5savesLeadersNames = []
top5savesLeadersStats = []
def top5savesFunc():
    top5saves = statsapi.league_leader_data('saves', statGroup='pitching', limit=5, season=2024)
    global top5savesLeadersNames
    global top5savesLeadersStats
    for each in top5saves:
        top5savesLeadersNames.append(each[1])
        top5savesLeadersStats.append(each[3])

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


# add quit button
quit_button = tk.Button(tab1, text='Quit', command=quitWindow).grid(row=10, column=2, sticky='n')









# start the GUI --> Leave here at the end!
notebook.pack()
window.mainloop()
