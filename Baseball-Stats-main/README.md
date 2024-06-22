# Baseball-Stats

I feel that I was quite successful in what I set out to do when I started this process. When I started out my goal was to use the MLB-stats api to get up to date stats on the matchups and standings. I had never used an api so it was a lot of learning and documentation reading but I managed to learn.
	The app uses the custom tkinter add-on to add different themes of buttons and labels to the normal tkinter. This gives the app a slightly more modern theme for the gui than using normal tkinter
	In my code, each section of my work is laid out through a comment that looks like this:
#-------------------------Matchups tab function—--------------------
	
	Most of the information in my code is taken from the api through looping through dictionaries and lists. This is seen in my first function in the document, as well as through for tab 2 and 3 information.
	The button for the matchup information and creating a child window is done through a lambda function
	There are occasional errors when you press the matchup button to look at a specific matchup. If some of the teams lineups are out but not all of them it will throw in error. This does not affect anything in the gui. The teams that have their game lineups out will still show. The teams that have not announced their lineup will show an empty space where the lineup will be when its announced.

Features to test out:
View matchup to see up-to-date score and lineup (Tab 1)
Swap through all major stats leaders (Tab 2)
Look at standings of each division in real time (Tab 3)
For tab 2 and 3, these update as of the next morning after games
Swap between light and dark mode in your computers system settings to see different themes for the app


Important installs for file to run:
Pip3 install MLB-StatsAPI
Pip3 install datetime
Pip3 install tk
Pip3 install customtkinter
Pip3 install notebook
