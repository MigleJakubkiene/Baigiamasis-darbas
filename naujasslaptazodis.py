from PyQt6.QtWidgets import QApplication, QMainWindow
from slaptazodis import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.mygtukas.clicked.connect(self.paspausta)

    def paspausta(self) :
        pastas = "admin@vilniuscoding.lt"
        pasvord = str(12345)

        if self.elpastas.text() == pastas and self.slaptazodis.text() == pasvord :
            self.Komentaras.setText("Sveikiname sėkmingai prisijungus")

        else :
            self.Komentaras.setText("Neteisingi prisijungimo duomenys")

        if self.elpastas.text() == "" :
            self.Komentaras.setText("Negavome jokių duomenų, bandykite dar kartą")

        if self.slaptazodis.text() == "" :
            self.Komentaras.setText("Negavome jokių duomenų, bandykite dar kartą")

        
aplikacija = QApplication([])
langas = Langas()
langas.show()
aplikacija.exec()