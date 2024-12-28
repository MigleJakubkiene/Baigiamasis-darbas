from PyQt6.QtWidgets import QApplication, QMainWindow
from uzduotis import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.mygtukas_minus.clicked.connect(self.pridėti)
        self.mygtukas_plius.clicked.connect(self.pridėti)
        self.laukelis.setText("10")

    def pridėti(self) :
        print("Paspaudimas įvyko")


aplikacija = QApplication([])
langas = Langas()
langas.show()
aplikacija.exec()

