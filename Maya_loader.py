####################
# Run this in your maya script editor:

import sys

# change this path to your location of the pythonSchool git repo
sys.path.append("V:/projects/coding/teamShirts")

import teamSelector_main

if teamSelector_main.INSTANCE:
    teamSelector_main.INSTANCE.close()
    teamSelector_main.INSTANCE

reload(teamSelector_main)

teamSelector_main.show_gui()
