from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #self.pirmas_mygtukas.clicked.connect(self.paspaudimas)
        self.zinute.setText("Mygtukas paspaustas")
       

    def paspaudimas(self) :
        print("Paspaudimas įvyko")

aplikacija = QApplication([])
langas = Langas()
langas.show()
aplikacija.exec()