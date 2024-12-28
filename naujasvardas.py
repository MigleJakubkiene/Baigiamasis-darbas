from PyQt6.QtWidgets import QApplication, QMainWindow
from vardas import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mygtukas.clicked.connect(self.paspausta)
        

    def paspausta(self) :
        metai = 2024 - int(self.amzius.text())
        
        self.zinute.setText(f"Sveiki {self.vardas.text()} {self.pavarde.text()} ,Jums {str(metai)} metai")
        
        

        
aplikacija = QApplication([])
langas = Langas()
langas.show()
aplikacija.exec()
