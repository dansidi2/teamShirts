import sys
from PySide2 import QtWidgets
import json
from PySide2.QtGui import QPixmap
try:
    import maya.cmds as mc
except ModuleNotFoundError:
    pass


def lower_case(name):
    return name.replace(" ", "_").lower()


def get_thumb_file(proper_name):
    suffix = (str(lower_case(proper_name)) + "_1001")
    extension = (suffix + (".png"))
    thumb_file = ("V:\projects\StadiumCrowd\Assets\clothing\clubShirts\\thumbs\\" + str(extension))
    return thumb_file


def get_UDIM_file(proper_name):
    suffix = (str(lower_case(proper_name)) + "_<UDIM>")
    extension = (suffix + (".png"))
    UDIM_file = ("V:\projects\StadiumCrowd\Assets\clothing\clubShirts\\thumbs\\" + str(extension))
    return UDIM_file

def get_texture_node(selected):
    selectedNode = mc.ls(sl=True, dag=True, s=True)
    print("Selected node: " + str(selectedNode))
    shadeEng = mc.listConnections(selectedNode, type="shadingEngine")
    print("ShadeEng: " + str(shadeEng))
    materials = mc.ls(mc.listConnections(shadeEng), materials=True)
    print("Materials: " + str(materials))
    texture_node = mc.listConnections(materials)[0]
    print("Texture node: " + str(texture_node))
    return texture_node


class TeamSelectorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(TeamSelectorDialog, self).__init__(parent)

        # Teams
        with open("V:/projects/coding/teamShirts/teams.py") as json_file:
            self.teams = json.load(json_file)
        countries = self.teams.keys()

        # Layouts
        main_layout = QtWidgets.QVBoxLayout()
        country_layout = QtWidgets.QHBoxLayout()
        league_layout = QtWidgets.QHBoxLayout()
        team_layout = QtWidgets.QHBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()
        display_layout = QtWidgets.QHBoxLayout()

        # Widgets
        main_label = QtWidgets.QLabel("Team Selector:")
        self.country_cb = QtWidgets.QComboBox()
        self.country_cb.addItems(countries)
        self.country_cb.currentTextChanged.connect(self.country_click_event)
        country_label = QtWidgets.QLabel("Country: ")
        league_label = QtWidgets.QLabel("League: ")
        self.league_list = QtWidgets.QListWidget()
        self.league_list.setFixedSize(250, 100)
        self.league_list.itemClicked.connect(self.league_clicked_event)
        team_label = QtWidgets.QLabel("Team:")
        self.team_list = QtWidgets.QListWidget()
        self.team_list.setFixedSize(250, 100)
        self.team_list.itemClicked.connect(self.team_clicked_event)
        self.home_pb = QtWidgets.QPushButton("Set as &Home team")
        self.home_pb.clicked.connect(self.home_button_clicked)
        self.home_pb.setFixedWidth(120)
        self.away_pb = QtWidgets.QPushButton("Set as &Away team")
        self.away_pb.clicked.connect(self.away_button_clicked)
        self.away_pb.setFixedWidth(120)
        display_label = QtWidgets.QLabel("Team shirt: ")
        self.display_pixmap = QPixmap()
        self.display_pixmap_label = QtWidgets.QLabel()
        self.display_pixmap_label.setStyleSheet("border: 1px solid black")
        self.display_pixmap_label.setFixedSize(120, 120)
        self.display_pixmap_label.setPixmap(self.display_pixmap)
        self.display_pixmap_label.setScaledContents(True)

        # setup
        main_layout.addWidget(main_label)
        main_layout.addItem(country_layout)
        country_layout.addWidget(country_label)
        country_layout.addWidget(self.country_cb)
        main_layout.addItem(league_layout)
        league_layout.addWidget(league_label)
        league_layout.addWidget(self.league_list)
        main_layout.addItem(team_layout)
        team_layout.addWidget(team_label)
        team_layout.addWidget(self.team_list)
        main_layout.addItem(display_layout)
        display_layout.addWidget(display_label)
        display_layout.addWidget(self.display_pixmap_label)
        main_layout.addItem(button_layout)
        button_layout.addWidget(self.home_pb)
        button_layout.addWidget(self.away_pb)

        self.setLayout(main_layout)
        self.resize(400, 300)

    def country_click_event(self):
        self.league_list.clear()
        self.country_clicked = self.country_cb.currentText()
        self.leagues = list(self.teams.get(self.country_clicked).keys())
        self.league_list.addItems(self.leagues)

    def league_clicked_event(self):
        self.team_list.clear()
        row_clicked = self.league_list.currentRow()
        league_clicked = self.leagues[row_clicked]
        self.teams_in_league = self.teams.get(self.country_clicked).get(league_clicked)
        self.team_list.addItems(self.teams_in_league)

    def team_clicked_event(self):
        row_clicked = self.team_list.currentRow()
        self.team_selected = self.teams_in_league[row_clicked]
        print(self.team_selected)
        self.display_pixmap.load(get_thumb_file(self.team_selected))
        self.display_pixmap_label.setPixmap(self.display_pixmap)
        #self.display_pixmap_label.show()

    def home_button_clicked(self):
        print("Thumb file: " + str(get_thumb_file(self.team_selected)))
        print("Getting texture node...")
        texture_node = get_texture_node(mc.ls(sl=True))
        print("texture node: " + str(texture_node))
        mc.setAttr((str(texture_node) + ".fileTextureName"), str(get_UDIM_file(self.team_selected)), type="string")

    def away_button_clicked(self):
        print("Away button clicked with " + str(self.team_selected) + " selected")


def show_dialog():
    app = QtWidgets.QApplication(sys.argv)
    d = TeamSelectorDialog()
    d.exec_()  # blocking call


if __name__ == "__main__":
    show_dialog()
