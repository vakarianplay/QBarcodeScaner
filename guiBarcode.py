# from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton, QFileDialog, QLabel
# from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
# from PyQt5.QtCore import Qt

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import barcodeClass
import qdarktheme
import sys


class MainClass:

    def __init__(self):
        print("MainClass")


    def fileOpen(self):
        barcodeFile = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        linePath.setText(barcodeFile[0])
        barcodeClass.init(barcodeFile[0])
        ImgDraw(barcodeFile[0])



class ImgDraw:
    def __init__(self, imgpath):
        print(imgpath)
        pixmap = QPixmap(imgpath)
        spix = pixmap.scaledToHeight(380)
        imgLabel.setPixmap(spix)




class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        buttonPath = QPushButton("  Browse ...  ", self)
        global linePath
        global imgLabel
        imgLabel = QLabel(self)
        imgLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        imgLabel.setAlignment(Qt.AlignCenter)
        imgLabel.setText("Load barcode image")
        imgLabel.setStyleSheet("QLabel {font-size: 15pt; font-weight: bolder;}")

        linePath = QLineEdit()
        buttonPath.clicked.connect(MainClass.fileOpen)

        lay = QVBoxLayout()
        layH = QHBoxLayout()
        layV = QVBoxLayout()
        layH.addWidget(linePath)
        layH.addWidget(buttonPath)
        layV.addWidget(imgLabel)
        lay.addStretch(1)
        lay.addLayout(layV)
        lay.addLayout(layH)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())
    # linePath = QLineEdit()


    # barcode = barcodeClass()
    main = MainClass()
    widget = Window()

    widget.show()
    widget.resize(600, 400)
    sys.exit(app.exec_())
