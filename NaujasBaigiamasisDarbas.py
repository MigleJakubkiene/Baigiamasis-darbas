from PyQt6.QtWidgets import QApplication, QMainWindow
from BaigiamasisDarbas import Ui_MainWindow
import requests
from bs4 import BeautifulSoup

class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mygtukas.clicked.connect(self.paspausta)

    def paspausta(self) :
        url = self.nuoroda.text()
        if "https://elenta.lt/" in url:
            data = requests.get(url)
            html = BeautifulSoup(data.text, "html.parser")
            for box in html.select(".summary") :
                Pavadinimas = box.select_one("h3.ad-hyperlink")
                Pavadinimas = Pavadinimas.text if Pavadinimas else ""
                Kaina = box.select_one("span.price-box")
                Kaina = Kaina.text if Kaina else ""
                self.komentaras.setText(f"Skelbimo pavadinimas- {Pavadinimas}, kaina - {Kaina} Eur.")             
      

aplikacija = QApplication([])
langas = Langas()
langas.show()
aplikacija.exec()

