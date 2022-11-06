from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6 import QtCore,QtGui
from PySide6.QtCore import Qt
import os
from qr import QR

path_to_image = "path.txt"
path_to_id = "id.txt"

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'QR'
        self.left = 0
        self.top = 0
        self.width = 492
        self.height = 492
        self.resize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if (not os.path.isfile("qr.png")):
            self.widget = QtWidgets.QLineEdit()
            self.widget.setMaxLength(24)
            self.widget.setFixedSize(self.width,self.height/4)
            self.resize(self.widget.size())
            self.widget.setAlignment(Qt.AlignHCenter)
            self.widget.setPlaceholderText("Enter Door ID")
            self.widget.returnPressed.connect(self.return_pressed)
            self.setCentralWidget(self.widget)
        else :
            self.widget = QtWidgets.QLabel(self)
            self.setCentralWidget(self.widget)
            timer = QtCore.QTimer(self)
            timer.timeout.connect(self.update_image)
            timer.start(500)
            self.update_image()
            
    def return_pressed(self):
        f = open(path_to_id,"w")
        f.write(self.widget.text())
        f.close()
        qr_generator = QR()
        qr_generator.create_qr_image(self.widget.text())
        self.widget = QtWidgets.QLabel(self)
        self.setCentralWidget(self.widget)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_image)
        timer.start(500)
        self.update_image()


    def update_image(self):
        f = open(path_to_image,"r")
        path = f.read()
        f.close()
        pixmap = QtGui.QPixmap(path)
        if not pixmap.isNull():
            self.widget.setPixmap(pixmap)
            self.resize(pixmap.size())
            self.widget.adjustSize()