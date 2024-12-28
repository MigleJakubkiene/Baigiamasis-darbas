from PyQt6.QtWidgets import QApplication, QMainWindow
from skelbimai import Ui_MainWindow

import requests
from bs4 import BeautifulSoup
base_url = "https://www.skelbimai.lt/"


class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mygtukas.clicked.connect(self.paspausta)

    def paspausta(self) :
        url = self.nuoroda.text()
        if "https://www.skelbimai.lt" in url:
            data = requests.get(url)
            html = BeautifulSoup(data.text, "html.parser")
            category = html.select_one("span.item-wp.last > span")
            category = category.text.strip() 
            number = html.select_one("div.description.f")
            number = number.text.strip()
            self.mygtukas.Text.setText(f"{category} {number}")  
        else:
            self.mygtukas.Text.setText(f"{url} netinkamas web puslapis")

         
        
if __name__ == "__main__":
    app = QApplication([])
    Langas = QMainWindow()
    Langas.setWindowTitle("Input Form")
    Langas.show()
    app.exec()