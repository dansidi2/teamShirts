import sys
sys.path.append("V:/projects/coding/teamShirts")

from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import teamSelector_main
from PySide2 import QtWidgets

reload(teamSelector_main)

ptr = omui.MQtUtil.mainWindow()
widget = wrapInstance(long(ptr), QtWidgets.QWidget)


d = teamSelector_main.ssDialog(widget)
d.exec_()