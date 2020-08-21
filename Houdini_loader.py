####################
# Run this in your maya script editor:

import sys

# change this path to your location of the pythonSchool git repo
sys.path.append("V:/projects/coding/teamShirts")

import teamSelector_houdini

if teamSelector_houdini.INSTANCE:
    teamSelector_houdini.INSTANCE.close()
    teamSelector_houdini.INSTANCE

reload(teamSelector_houdini)

teamSelector_houdini.show_gui()
