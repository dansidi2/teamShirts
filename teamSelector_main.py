import sys
from PySide2 import QtWidgets


class ssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ssDialog, self).__init__(parent)

        # Teams
        countries = ["Austria",
                     "Azerbaijan",
                     "Belgium",
                     "Czech Republic",
                     "Denmark",
                     "England",
                     "Finland",
                     "France",
                     "Germany",
                     "Greece",
                     "Israel",
                     "Italy",
                     "Kazakhstan",
                     "Netherlands",
                     "Norway",
                     "Poland",
                     "Portugal",
                     "Romania",
                     "Russia",
                     "Scotland",
                     "Serbia",
                     "Spain",
                     "Sweden",
                     "Switzerland",
                     "Ukraine"]

        leagues = {"Austria": ["Bundesliga"],
                   "Azerbaijan": ["Premiere League"],
                   "Belgium": ["Pro League"],
                   "Czech Republic": ["Czech First League"],
                   "Denmark": ["Superliga"],
                   "England": ["Premiere League", "Championship", "League 1", "League 2"],
                   "Finland": ["Veikkausliiga"],
                   "France": ["Ligue 1", "Ligue 2"],
                   "Germany": ["Bundesliga", "Bundesliga 2"],
                   "Greece": ["Super League"],
                   "Israel": ["Premiere League"],
                   "Italy": ["Serie A", "Serie B"],
                   "Kazakhstan": ["Premiere League"],
                   "Netherlands": ["Eredivisie"],
                   "Norway": ["Eliteserien"],
                   "Poland": ["Ekstraklasa"],
                   "Portugal": ["Primeira Liga", "Segunda Liga"],
                   "Romania": ["Liga 1"],
                   "Russia": ["Championship"],
                   "Scotland": ["Premiership", "Championship", "League 1", "League 2"],
                   "Serbia": ["Super Liga"],
                   "Spain": ["La Liga", "Segunda Division"],
                   "Sweden": ["Allsvenskan"],
                   "Switzerland": ["Super League"],
                   "Ukraine": ["Championship"]
                   }

        # Layouts
        main_layout = QtWidgets.QHBoxLayout()
        home_layout = QtWidgets.QVBoxLayout()
        away_layout = QtWidgets.QVBoxLayout()
        home_country_layout = QtWidgets.QHBoxLayout()
        away_country_layout = QtWidgets.QHBoxLayout()

        # Widgets
        home_label = QtWidgets.QLabel("Home team:")
        away_label = QtWidgets.QLabel("Away team:")
        self.home_country_cb = QtWidgets.QComboBox()
        self.away_country_cb = QtWidgets.QComboBox()
        self.home_country_cb.addItems(countries)
        self.away_country_cb.addItems(countries)
        home_country_label = QtWidgets.QLabel("Country: ")
        away_country_label = QtWidgets.QLabel("Country: ")

        self.button1 = QtWidgets.QPushButton("Go")
        self.label_name1 = QtWidgets.QLabel("Team Name:")

        # setup
        main_layout.addItem(home_layout)
        main_layout.addItem(away_layout)

        home_layout.addWidget(home_label)
        home_layout.addItem(home_country_layout)
        home_country_layout.addWidget(home_country_label)
        home_country_layout.addWidget(self.home_country_cb)

        away_layout.addWidget(away_label)
        away_layout.addItem(away_country_layout)
        away_country_layout.addWidget(away_country_label)
        away_country_layout.addWidget(self.away_country_cb)

        self.setLayout(main_layout)

    def lower_case(self, name="Test Name"):
        return name.replace(" ", "_").lower()


def show_dialog():
    app = QtWidgets.QApplication(sys.argv)
    d = ssDialog()
    d.exec_()  # blocking call


if __name__ == "__main__":
    show_dialog()
