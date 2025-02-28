import random
import sys

from PyQt6.QtCore import QRect
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow

from design import Design


class MainWindow(QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.create_circles)

        self.circles = []

    def create_circles(self):
        x = random.randint(20, 180)
        y = random.randint(20, 250)
        radius = random.randint(20, 50)

        if x - radius < 0: x = radius
        if y - radius < 0: y = radius
        if x + radius > 200: x = 200 - radius
        if y + radius > 300: y = 300 - radius

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circles.append((x, y, radius, color))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for (x, y, radius, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QRect(x - radius, y - radius, radius * 2, radius * 2))

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

