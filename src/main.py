import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import map_generator


class SettingUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Generate")

        self.map_scale = QtWidgets.QSpinBox(self) 
        self.map_scale.setRange(8,16)
        self.threshold = QtWidgets.QSpinBox(self)
        self.threshold.setRange(-8,8)
        self.threshold.setValue(-2)
        self.seed = QtWidgets.QSpinBox(self)
        self.seed.setRange(-50000,50000)
        self.seed.setValue(random.randint(0,5000))
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.text = QtWidgets.QLabel("Map scale", alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.map_scale)
        self.text = QtWidgets.QLabel("Ocean Threshold",alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.threshold)
        self.text = QtWidgets.QLabel("Random Seed",alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.seed)

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.drawMap)


    def drawMap(self):
        seedval = self.seed.value() 
        thresholdval = self.threshold.value()
        map_scaleval = self.map_scale.value()
        map_generator.main(seedval,map_scaleval,thresholdval)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = SettingUI()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
