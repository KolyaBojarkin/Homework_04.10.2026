from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QGridLayout, QHBoxLayout

app = QApplication([])

window = QMainWindow()
window.setFixedSize(750, 800)

frame = QFrame()
frame.setStyleSheet("background-color: gray")

layout = QGridLayout(frame)
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(8)


red1 = QFrame()
red1.setStyleSheet("background-color: red")
red1_layout = QHBoxLayout(red1)
red1_layout.setContentsMargins(40, 20, 40, 20)

sq1 = QFrame()
sq1.setStyleSheet("background-color: white")
sq1.setFixedSize(30, 30)

sq2 = QFrame()
sq2.setStyleSheet("background-color: lightgray")
sq2.setFixedSize(30, 30)

red1_layout.addWidget(sq1)
red1_layout.addWidget(sq2)
layout.addWidget(red1, 1, 0)

red2 = QFrame()
red2.setStyleSheet("background-color: red")
layout.addWidget(red2, 1, 1)

red3 = QFrame()
red3.setStyleSheet("background-color: red")
red3_layout = QHBoxLayout(red3)
red3_layout.setContentsMargins(40, 20, 40, 20)

sq3 = QFrame()
sq3.setStyleSheet("background-color: white")
sq3.setFixedSize(30, 30)

sq4 = QFrame()
sq4.setStyleSheet("background-color: lightgray")
sq4.setFixedSize(30, 30)

red3_layout.addWidget(sq3)
red3_layout.addWidget(sq4)
layout.addWidget(red3, 1, 2)


green1 = QFrame()
green1.setStyleSheet("background-color: green")
green1_layout = QGridLayout(green1)

lbl1 = QLabel("Лейбл 1")
lbl2 = QLabel("Лейбл 2")

green1_layout.addWidget(lbl1, 0, 0)
green1_layout.addWidget(lbl2, 1, 0)
layout.addWidget(green1, 2, 0)

green2 = QFrame()
green2.setStyleSheet("background-color: green")
green2_layout = QGridLayout(green2)

lbl3 = QLabel("Лейбл 1")
lbl4 = QLabel("Лейбл 2")

green2_layout.addWidget(lbl3, 0, 0)
green2_layout.addWidget(lbl4, 1, 0)
layout.addWidget(green2, 2, 1)

green3 = QFrame()
green3.setStyleSheet("background-color: green")
green3_layout = QGridLayout(green3)

lbl5 = QLabel("Лейбл 1")
lbl6 = QLabel("Лейбл 2")

green3_layout.addWidget(lbl5, 0, 0)
green3_layout.addWidget(lbl6, 1, 0)
layout.addWidget(green3, 2, 2)


blue1 = QFrame()
blue1.setStyleSheet("background-color: blue")
blue1_layout = QHBoxLayout(blue1)
blue1_layout.setContentsMargins(40, 20, 40, 20)

sq5 = QFrame()
sq5.setStyleSheet("background-color: white")
sq5.setFixedSize(30, 30)

sq6 = QFrame()
sq6.setStyleSheet("background-color: lightgray")
sq6.setFixedSize(30, 30)

blue1_layout.addWidget(sq5)
blue1_layout.addWidget(sq6)
layout.addWidget(blue1, 3, 0)

blue2 = QFrame()
blue2.setStyleSheet("background-color: blue")
layout.addWidget(blue2, 3, 1)

blue3 = QFrame()
blue3.setStyleSheet("background-color: blue")
blue3_layout = QHBoxLayout(blue3)
blue3_layout.setContentsMargins(40, 20, 40, 20)

sq7 = QFrame()
sq7.setStyleSheet("background-color: white")
sq7.setFixedSize(30, 30)

sq8 = QFrame()
sq8.setStyleSheet("background-color: lightgray")
sq8.setFixedSize(30, 30)

blue3_layout.addWidget(sq7)
blue3_layout.addWidget(sq8)
layout.addWidget(blue3, 3, 2)


window.setCentralWidget(frame)
window.show()

app.exec()