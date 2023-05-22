
import sys

from PyQt5.QtWidgets import *
from forex_python.converter import CurrencyRates

class Cafe(QWidget):
    def __init__(self):
        super().__init__()
        self.setupui_cafe()
#----------------------------Title-----------------------------------
    def setupui_cafe(self):
        self.resize(1350, 800)
        self.move(60, 80)
        self.setWindowTitle("Coffee Shop")
# ----------------------------Payment-----------------------------------
        c = CurrencyRates()
        c.get_rates('USD')
        print(c.get_rates('USD'))
    #----------------------------END-------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Cafe()
    form.show()
    app.exec()
