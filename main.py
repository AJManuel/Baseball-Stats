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
        print(f'{homeTeams} --> {awayTeams}')

def todayStandings():
    standings = statsapi.standings(date=currentDate)
    print(standings)
todaySchedule()
print(homeTeams)

#-----------------matchups-----------------

dateLabel = Label(tab1, text=currentDate, fg='black', font=('arial', 20))
dateLabel.grid(column=2, row=0)

for count, each in enumerate(homeTeams):
    homeTeamLabel = Label(tab1, text=each, fg='black', font=('arial', 20))
    homeTeamLabel.grid(column=1, row=count + 1, pady=10, padx=3)
    print(count)


for amount, each in enumerate(homeTeams):
    atLabel = Label(tab1, text='@', fg='black', font=('arial', 20))
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
