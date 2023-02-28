from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import barcodeClass
import qdarktheme
import sys
import os


class MainClass():

    def __init__(self):
        print("MainClass")

    def fileOpen(self):
        textResult.clear()
        barcodeFile = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        linePath.setText(barcodeFile[0])
        ImgDraw(barcodeFile[0])
        barcodeClass.init(barcodeFile[0])
        print(barcodeClass.getType())
        print(barcodeClass.getData())

        if len(barcodeClass.getType()) > 0:
            dir = os.path.abspath(os.curdir)
            ImgDraw(dir + "/barcode_detected.png")
            for position in enumerate(barcodeClass.getType()):
                print(position[0])
                textResult.append("Type: " + barcodeClass.getType()[position[0]] + "\nData: " + barcodeClass.getData()[position[0]].decode("utf-8") + "\n__________________\n")
        else:
            textResult.setPlainText("No data recognized")


class ImgDraw:
    def __init__(self, imgpath):
        # print(imgpath)
        pixmap = QPixmap(imgpath)
        spix = pixmap.scaledToHeight(380)
        imgLabel.setPixmap(spix)
        self.__showResult()

    def __showResult(self):
        textResult.setHidden(False)



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__initUi()


    def __initUi(self):
        buttonPath = QPushButton("  Browse ...  ", self)
        global linePath
        global imgLabel
        global lay
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

        self.barcodeResults()
        textResult.setHidden(True)

    def barcodeResults(self):
        global textResult
        textResult = QTextEdit()
        textResult.setMinimumHeight(100)
        textResult.setMaximumHeight(100)
        lay.addWidget(textResult)



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
