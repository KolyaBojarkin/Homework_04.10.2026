
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QGridLayout, QPushButton

app = QApplication([])

window = QMainWindow()
window.setFixedSize(750, 800)

frame = QFrame(window)
frame.setGeometry(0, 0, 750, 800)
frame.setStyleSheet("background-color: darkgray")

layout = QGridLayout(frame)
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(15)

lbl = QLabel("0")
lbl.setStyleSheet("color: white; font-size: 48px")
layout.addWidget(lbl, 0, 0)

sixty_seven = QPushButton("67")
sixty_seven.setStyleSheet("background-color: gray; color: white")
layout.addWidget(sixty_seven, 1, 0)

plus = QPushButton("+")
plus.setStyleSheet("background-color: gray; color: white")
layout.addWidget(plus, 2, 0)

minus = QPushButton("-")
minus.setStyleSheet("background-color: gray; color: white")
layout.addWidget(minus, 3, 0)

reset = QPushButton("Reset")
reset.setStyleSheet("background-color: gray; color: white")
layout.addWidget(reset, 4, 0)

number = [0]

def add_67():
    number[0] += 67
    lbl.setText(str(number[0]))

def increase():
    number[0] += 1
    lbl.setText(str(number[0]))

def decrease():
    number[0] -= 1
    lbl.setText(str(number[0]))

def reset_number():
    number[0] = 0
    lbl.setText(str(number[0]))

sixty_seven.clicked.connect(add_67)
plus.clicked.connect(increase)
minus.clicked.connect(decrease)
reset.clicked.connect(reset_number)


