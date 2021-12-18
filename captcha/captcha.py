from PyQt5 import QtWidgets, QtGui
import sys
import random
from string import ascii_letters

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Captcha")
        self.setWindowIcon(QtGui.QIcon("captcha.png"))
        #self.setGeometry(400, 250, 600, 250)
        self.setMaximumSize(600, 250)
        self.setMinimumSize(600, 250)
        self.setStyleSheet("background-color: #E6E6FA;")
        self.show()
        self.init_ui()

    def init_ui(self):
        self.word = QtWidgets.QLabel()
        self.maked_word = self.make_word()
        self.word.setText(self.maked_word)
        self.word.setFont(QtGui.QFont("Segoe Script", 17))
        self.word.setStyleSheet("border: 1px solid black; border-color: grey; background-color: white;")
        info = QtWidgets.QLabel("To continue, type the characters you see in the picture.")
        info.setFont(QtGui.QFont("Arial", 13))
        info2 = QtWidgets.QLabel("Characters:")
        info2.setFont(QtGui.QFont("Arial", 14))
        self.info3 = QtWidgets.QLabel()
        self.info3.setFont(QtGui.QFont("Arial", 13))
        self.input = QtWidgets.QLineEdit()
        self.input.setFont(QtGui.QFont("Arial", 12))

        self.button = QtWidgets.QPushButton("Continue")
        self.button.setStyleSheet("QPushButton::hover""{"" border-style: outset; border-width: 3px;border-radius: 5px;"
                                  "border-color: #2752B8;""}")
        self.button.setFont(QtGui.QFont("Arial", 12))
        self.button.clicked.connect(self.click)

        self.change_button = QtWidgets.QPushButton("Change word")
        self.change_button.setStyleSheet("QPushButton::hover""{"" border-style: outset; border-width: 3px;"
                                         "border-radius: 5px;border-color: #2752B8;""}")
        self.change_button.setFont(QtGui.QFont("Arial", 12))
        self.change_button.clicked.connect(self.change)

        # Horizontal boxes
        hBox1 = QtWidgets.QHBoxLayout()
        hBox1.addWidget(info)
        hBox1.addStretch()
        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addStretch()
        hBox2.addWidget(self.word)
        hBox2.addStretch()
        hBox3 = QtWidgets.QHBoxLayout()
        hBox3.addStretch()
        hBox3.addWidget(info2)
        hBox3.addWidget(self.input)
        hBox4 = QtWidgets.QHBoxLayout()
        hBox4.addStretch()
        hBox4.addWidget(self.change_button)
        hBox4.addWidget(self.button)
        hBox5 = QtWidgets.QHBoxLayout()
        hBox5.addWidget(self.info3)
        hBox5.addStretch()

        # Vertical boxes
        vBox1 = QtWidgets.QVBoxLayout()
        vBox1.addLayout(hBox1)
        vBox1.addStretch()
        vBox2 = QtWidgets.QVBoxLayout()
        vBox2.addLayout(hBox2)
        vBox2.addStretch()
        vBox3 = QtWidgets.QVBoxLayout()
        vBox3.addLayout(hBox3)
        vBox3.addStretch()
        vBox4 = QtWidgets.QVBoxLayout()
        vBox4.addLayout(hBox4)
        vBox4.addStretch()

        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(vBox1)
        vBox.addLayout(vBox2)
        vBox.addLayout(vBox3)
        vBox.addLayout(vBox4)
        vBox.addLayout(hBox5)

        self.setLayout(vBox)

    def make_word(self):
        letters_and_nums = ascii_letters + "0123456789"
        word = ""
        for i in range(8):
            word += random.choice(list(letters_and_nums))

        return word

    def click(self):
        if self.maked_word == self.input.text():
            self.info3.setText(" ")
            self.info3.setStyleSheet("color: green;")
            self.info3.setText("You are not a robot.")
        elif len(self.input.text()) == 0:
            self.info3.setText(" ")
            self.info3.setStyleSheet("color: red;")
            self.info3.setText("Fill in the blank!")
        else:
            self.info3.setText(" ")
            self.info3.setStyleSheet("color: red;")
            self.info3.setText("You are a robot :)")

    def change(self):
        self.maked_word = self.make_word()
        self.word.setText(self.maked_word)

app = QtWidgets.QApplication(sys.argv)
pencere = Window()
sys.exit(app.exec_())
