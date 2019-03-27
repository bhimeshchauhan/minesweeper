import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QLCDNumber, QLabel
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import pyqtSlot
from qtconsole.qt import QtGui


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.scoreLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalScoreGroupBox)
        self.createGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        count = 0
        for x in range(10):
            for y in range(10):
                count += 1
                button = QPushButton(str(count))
                button.setContentsMargins(0,0,0,0)
                button.setStyleSheet(
                                     "border-width: 2px; "
                                     "border-style: solid;"
                                     "border-color: black;"
                                     "border-radius: 0;"
                                     "padding: 6px;")
                layout.addWidget(button, x, y)
        self.horizontalGroupBox.setLayout(layout)

    def scoreLayout(self):
        self.horizontalScoreGroupBox = QGroupBox()
        scoreLayout = QGridLayout()
        scoreLayout.setContentsMargins(0, 0, 0, 0)
        scoreLayout.setSpacing(0)
        score = QLCDNumber()
        score.display(int("109"))

        # score.setPalette()
        score.setStyleSheet("margin-left: 25%; margin-right: 25%; color: red;")

        # icon = QtGui.QPixmap(QIcon('./smiley.jpg'))
        # image = QPushButton()
        # image.setIcon(QIcon('./smiley.jpg'))
        label = QLabel(self)
        pixmap = QPixmap('./smiley.jpg')
        smallerpix = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        label.setPixmap(smallerpix)

        time = QLCDNumber()
        time.display(int("009"))
        time.setStyleSheet("margin-left: 25%; margin-right: 25%;")
        scoreLayout.addWidget(score, 0, 0)
        scoreLayout.addWidget(label, 0, 1)
        scoreLayout.addWidget(time, 0, 2)
        self.horizontalScoreGroupBox.setLayout(scoreLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
