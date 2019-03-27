import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QLCDNumber, QLabel
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from qtconsole.qt import QtGui
from functools import partial
import random

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

    def findsum(self, candidates, target, maxsize, width):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res, maxsize, width)
        return random.choice(res)

    def dfs(self, nums, target, index, path, res, maxsize, width):
        if target < 0:
            return  # backtracking
        if target == 0:
            if len(path) <= maxsize:
                if all(i <= width for i in path):
                    res.append(path)
                return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res, maxsize, width)

    def replaceCount(self, matrix, width, height):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != '*':
                    # i-1
                    if i - 1 >= 0 and matrix[i - 1][j] == "*":
                        matrix[i][j] += 1
                    # i+1
                    if i + 1 < height and matrix[i + 1][j] == "*":
                        matrix[i][j] += 1
                    # j+1
                    if j + 1 < width and matrix[i][j + 1] == "*":
                        matrix[i][j] += 1
                    # j-1
                    if j - 1 >= 0 and matrix[i][j - 1] == "*":
                        matrix[i][j] += 1
                    # i-1 j-1
                    if j - 1 >= 0 and i - 1 >= 0 and matrix[i - 1][j - 1] == "*":
                        matrix[i][j] += 1

                    # i+1 j+1
                    if j + 1 < width and i + 1 < height and matrix[i + 1][j + 1] == "*":
                        matrix[i][j] += 1
                    # i-1 j+1
                    if j + 1 < width and i - 1 >= 0 and matrix[i - 1][j + 1] == "*":
                        matrix[i][j] += 1
                    # i+1 j-1
                    if j - 1 >= 0 and i + 1 < height and matrix[i + 1][j - 1] == "*":
                        matrix[i][j] += 1
        return matrix

    def main(self, width, height, num):
        if num > height * width:
            print("Board exploded: Max mines reached")
            return
        buckets = [[0 for col in range(width)] for row in range(height)]
        freq = list(self.findsum(list(range(1, 9)), num, height, width))
        # print("freq",freq)
        for i in range(len(freq)):
            changefor = random.sample(list(enumerate(buckets[i])), freq[i])
            for j in changefor:
                buckets[i][j[0]] = "*"
        mat = self.replaceCount(buckets, width, height)
        for item in mat:
            print(''.join(str(x) for x in item))
        return mat

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
        height = 4
        width = 4
        maxbombs = 5
        mat = self.main(width, height, maxbombs)
        self.horizontalGroupBox = QGroupBox()
        # self.horizontalGroupBox.setContentsMargins(0, 0, 0, 0)
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # count = 0
        parentwidth = layout.geometry()
        print( parentwidth, self.width)
        for x in range(height):
            for y in range(width):
                # count += 1
                button = QPushButton(str(mat[x][y]))
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
