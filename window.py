import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QLCDNumber, QLabel
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from qtconsole.qt import QtGui
from functools import partial


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Minesweeper'
        self.left = 20
        self.top = 20
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.width = 625
        self.height = 625
        self.initUI()

    def meme(self, name):
        print("awesome", name)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.scoreLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalScoreGroupBox, 0)
        self.createGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox, 2)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        # self.horizontalGroupBox.setContentsMargins(0, 0, 0, 0)
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        count = 0
        height = 8
        width = 10
        parentwidth = layout.geometry()
        print( parentwidth, self.width)
        for x in range(height):
            for y in range(width):
                count += 1
                button = QPushButton(str(count))
                button.setContentsMargins(0,0,0,0)
                button.setFixedHeight(self.height // height)
                button.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
                button.clicked.connect(partial(self.meme, button.text()))
                button.setStyleSheet(
                                     "border-width: 2px; "
                                     "border-style: solid;"
                                     "border-color: black;"
                                     "border-radius: 0;"
                                     "padding: 0px;"
                                     "margin: 0px")
                layout.addWidget(button, x, y)
        self.horizontalGroupBox.setLayout(layout)

    def scoreLayout(self):
        self.horizontalScoreGroupBox = QGroupBox()
        scoreLayout = QGridLayout()
        # scoreLayout.setAlignment(Qt.AlignCenter)
        # scoreLayout.setContentsMargins(0, 0, 0, 0)
        scoreLayout.setSpacing(0)

        score = QLCDNumber()
        score.display(109)
        score.setStyleSheet("background-color: black;")

        # icon = QtGui.QPixmap(QIcon('./smiley.jpg'))
        # image = QPushButton()
        # image.setIcon(QIcon('./smiley.jpg'))
        label = QLabel(self)
        pixmap = QPixmap('./smiley.jpg')
        small = pixmap.scaled(32, 32)
        label.setPixmap(small)
        label.setStyleSheet("color: red;")

        time = QLCDNumber()
        time.display(int("009"))
        time.setStyleSheet("margin-left: 25%;color: red;")

        scoreLayout.addWidget(score, 0, 0)
        scoreLayout.addWidget(label, 0, 1)
        scoreLayout.addWidget(time, 0, 2)
        self.horizontalScoreGroupBox.setLayout(scoreLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
