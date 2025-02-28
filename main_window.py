import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from curcle_widget import CircleWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(200, 300)
        self.setWindowTitle("Рисование случайных кругов")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.pushButton = QPushButton("Создать круги", self)
        self.pushButton.clicked.connect(self.create_circles)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.pushButton)

        self.circle_widget = CircleWidget(self)
        self.layout.addWidget(self.circle_widget)

    def create_circles(self):
        self.circle_widget.create_circle()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
