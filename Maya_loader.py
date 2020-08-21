####################
# Run this in your maya script editor:

import sys

# change this path to your location of the pythonSchool git repo
sys.path.append("V:/projects/coding/teamShirts")

import teamSelector_maya

if teamSelector_maya.INSTANCE:
    teamSelector_maya.INSTANCE.close()
    teamSelector_maya.INSTANCE

reload(teamSelector_maya)

teamSelector_maya.show_gui()
