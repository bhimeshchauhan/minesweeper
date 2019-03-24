import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


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
        windowLayout.addWidget(self.horizontalGroupBox2)

        self.createGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        # self.setLayout(windowLayout)


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
        self.horizontalGroupBox2 = QGroupBox()
        layout2 = QGridLayout()
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.setSpacing(0)
        button2 = QPushButton("no")
        layout2.addWidget(button2, 0, 0)
        self.horizontalGroupBox2.setLayout(layout2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
