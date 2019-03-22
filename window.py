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
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)
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
                # grid_layout.addWidget(button, x, y)

        # layout.addWidget(QPushButton('1'), 0, 0)
        # layout.addWidget(QPushButton('2'), 0, 1)
        # layout.addWidget(QPushButton('3'), 0, 2)
        # layout.addWidget(QPushButton('4'), 1, 0)
        # layout.addWidget(QPushButton('5'), 1, 1)
        # layout.addWidget(QPushButton('6'), 1, 2)
        # layout.addWidget(QPushButton('7'), 2, 0)
        # layout.addWidget(QPushButton('8'), 2, 1)
        # layout.addWidget(QPushButton('9'), 2, 2)
        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)
#
#
# class basicWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         grid_layout = QGridLayout()
#         # grid_layout.setContentsMargins(0, 0, 0, 0)
#         grid_layout.setSpacing(0)
#         self.setLayout(grid_layout)
#         # self.setGeometry(0,0,250,250)
#         count = 0
#         for x in range(10):
#             for y in range(10):
#                 count += 1
#                 button = QPushButton(str(count))
#
#                 button.setContentsMargins(0,0,0,0)
#                 button.setStyleSheet(
#                                      "border-width: 2px; "
#                                      "border-style: solid;"
#                                      "border-color: black;"
#                                      "border-radius: 0;"
#                                      "padding: 6px;")
#                 grid_layout.addWidget(button, x, y)
#
#         self.setWindowTitle('Basic Grid Layout')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     windowExample = basicWindow()
#     windowExample.show()
#     sys.exit(app.exec_())
