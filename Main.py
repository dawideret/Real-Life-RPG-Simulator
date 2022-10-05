from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

app_xpos = 750
app_ypos = 200
app_width = 360
app_height = 640


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(app_xpos, app_ypos, app_width, app_height)
        self.setWindowTitle("Life Ireru")
        self.initUI()

    def initUI(self):
        # App Interface goes below
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Some Text")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("It's a Button")
        self.b1.clicked.connect(self.button1)
        # App Interface goes above

    def button1(self):
        self.label.setText("Beep!")
        self.update()

    def update(self):
        self.label.adjustSize()


def button1():
    print("Boop!")


def main_window():
    app = QApplication(sys.argv)
    win = MainWindow()
    
    win.show()
    sys.exit(app.exec_())


main_window()
