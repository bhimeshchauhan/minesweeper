#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QLCDNumber, QLabel
from PyQt5.QtGui import QIcon, QColor, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
from qtconsole.qt import QtGui
from functools import partial
import random

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Minesweeper'
        self.left = 20
        self.top = 20
        self.width = 625
        self.height = 625
        self.mat = []
        self.visited = []
        self.mines = []
        self.time = QLCDNumber()
        self.initUI()

    def start_timer(self):
        # Initialize timer
        self.timer = QTimer()
        self.now = 0
        # Update display and start timer
        self.update_timer()
        self.timer.timeout.connect(self.tick_timer)
        self.timer.start(1000)  # Duration of one second = 1000 msec

    def update_timer(self):
        self.runtime = "%d:%02d" % (self.now / 60, self.now % 60)
        self.time.display(self.runtime)
        # print(self.runtime)

    def tick_timer(self):
        self.now += 1
        self.update_timer()

    def stop_timer(self):
        self.timer.stop()

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

    def replacezero(self, xpos, ypos, layout):
        width = len(self.mat[0])
        height = len(self.mat)
        if xpos - 1 >= 0 and self.mat[xpos - 1][ypos] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # i+1
        if xpos + 1 < height and self.mat[xpos + 1][ypos] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # ypos+1
        if ypos + 1 < width and self.mat[xpos][ypos + 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # ypos-1
        if ypos - 1 >= 0 and self.mat[xpos][ypos - 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # i-1 ypos-1
        if ypos - 1 >= 0 and xpos - 1 >= 0 and self.mat[xpos - 1][ypos - 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # i+1 ypos+1
        if ypos + 1 < width and xpos + 1 < height and self.mat[xpos + 1][ypos + 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # i-1 ypos+1
        if ypos + 1 < width and xpos - 1 >= 0 and self.mat[xpos - 1][ypos + 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1
        # i+1 ypos-1
        if ypos - 1 >= 0 and xpos + 1 < height and self.mat[xpos + 1][ypos - 1] == 0:
            layout.itemAtPosition(xpos-1, ypos).widget().setText(str(self.mat[xpos-1][ypos]))
            self.mat[xpos][ypos] += 1

    def replaceCount(self, layout):
        width = len(self.mat[0])
        height = len(self.mat)
        for xpos in range(width):
            for ypos in range(height):
                if self.mat[xpos][ypos] != '*' and (xpos, ypos) not in self.visited:
                    # i-1
                    if xpos - 1 >= 0 and self.mat[xpos - 1][ypos] == "*":
                        self.mat[xpos][ypos] += 1
                    # i+1
                    if xpos + 1 < height and self.mat[xpos + 1][ypos] == "*":
                        self.mat[xpos][ypos] += 1
                    # ypos+1
                    if ypos + 1 < width and self.mat[xpos][ypos + 1] == "*":
                        self.mat[xpos][ypos] += 1
                    # ypos-1
                    if ypos - 1 >= 0 and self.mat[xpos][ypos - 1] == "*":
                        self.mat[xpos][ypos] += 1
                    # i-1 ypos-1
                    if ypos - 1 >= 0 and xpos - 1 >= 0 and self.mat[xpos - 1][ypos - 1] == "*":
                        self.mat[xpos][ypos] += 1
                    # i+1 ypos+1
                    if ypos + 1 < width and xpos + 1 < height and self.mat[xpos + 1][ypos + 1] == "*":
                        self.mat[xpos][ypos] += 1
                    # i-1 ypos+1
                    if ypos + 1 < width and xpos - 1 >= 0 and self.mat[xpos - 1][ypos + 1] == "*":
                        self.mat[xpos][ypos] += 1
                    # i+1 ypos-1
                    if ypos - 1 >= 0 and xpos + 1 < height and self.mat[xpos + 1][ypos - 1] == "*":
                        self.mat[xpos][ypos] += 1

                    if self.mat[xpos][ypos] == 0:
                        self.replacezero(xpos, ypos, layout)
                    self.visited.append((xpos, ypos))

    def main(self, width, height, num):
        if num > height * width:
            print("Board exploded: Max mines reached")
            return
        buckets = [[0 for col in range(width)] for row in range(height)]
        # print(buckets)
        freq = list(self.findsum(list(range(1, 9)), num, height, width))
        # print("freq",freq)
        for i in range(len(freq)):
            changefor = random.sample(list(enumerate(buckets[i])), freq[i])
            for j in changefor:
                self.mines.append((i, j[0]))
                buckets[i][j[0]] = "*"
        # mat = self.replaceCount(buckets, width, height)
        for item in buckets:
            print(''.join(str(x) for x in item))
        return buckets

    def reveal_mines(self, layout):
        # print(self.mines, "are revieled")
        for item in self.mines:
            layout.itemAtPosition(item[0], item[1]).widget().setText(str(self.mat[item[0]][item[1]]))
        self.stop_timer()

    def setval(self, x, y, btn, layout):
        # print(self.mines)
        if (x,y) in self.mines:
            self.reveal_mines(layout)
        btn.setText(str(self.mat[x][y]))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.scoreLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalScoreGroupBox, 0)
        self.createGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox, 2)
        self.setLayout(windowLayout)
        self.start_timer()
        self.show()

    def createGridLayout(self):
        height = width = 5
        # width = random.randint(5, 15)
        maxbombs = 2
        print(height, width, maxbombs)
        self.mat = self.main(width, height, maxbombs)
        self.horizontalGroupBox = QGroupBox()
        # self.horizontalGroupBox.setContentsMargins(0, 0, 0, 0)
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # count = 0
        parentwidth = layout.geometry()
        print(parentwidth, self.width)
        for x in range(height):
            for y in range(width):
                # count += 1
                button = QPushButton()
                button.setContentsMargins(0,0,0,0)
                button.setFixedHeight(self.height // height)
                button.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
                button.clicked.connect(partial(self.setval, x, y, button, layout))
                button.setStyleSheet(
                                     "border-width: 2px; "
                                     "border-style: solid;"
                                     "border-color: black;"
                                     "font-size: 50px;"
                                     "border-radius: 0;"
                                     "padding: 0px;"
                                     "margin: 0px")
                layout.addWidget(button, x, y)
        self.replaceCount(layout)
        self.horizontalGroupBox.setLayout(layout)

    def scoreLayout(self):
        self.horizontalScoreGroupBox = QGroupBox()
        scoreLayout = QGridLayout()
        # scoreLayout.setAlignment(Qt.AlignCenter)
        # scoreLayout.setContentsMargins(0, 0, 0, 0)
        scoreLayout.setSpacing(0)

        score = QLCDNumber()
        score.display(000)
        score.setStyleSheet("background-color: black;")

        # icon = QtGui.QPixmap(QIcon('./smiley.jpg'))
        # image = QPushButton()
        # image.setIcon(QIcon('./smiley.jpg'))
        label = QLabel(self)
        pixmap = QPixmap('./smiley.jpg')
        small = pixmap.scaled(32, 32)
        label.setPixmap(small)
        label.setStyleSheet("color: red; margin-left: 10em;")

        self.time.display("00:00")
        self.time.setStyleSheet("background-color: black;")

        scoreLayout.addWidget(score, 0, 0)
        scoreLayout.addWidget(label, 0, 1)
        scoreLayout.addWidget(self.time, 0, 2)
        self.horizontalScoreGroupBox.setLayout(scoreLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
