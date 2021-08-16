
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Grid Layout")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    self.gridLayout = QGridLayout()
    btn1 = QPushButton("Button 1")
    btn2 = QPushButton("Button 2")
    btn3 = QPushButton("Button 3")
    btn4 = QPushButton("Button 4")

    self.gridLayout.addWidget(btn1, 0, 0)
    self.gridLayout.addWidget(btn2, 0, 1)
    self.gridLayout.addWidget(btn3, 1, 0)
    self.gridLayout.addWidget(btn4, 1, 1)

    self.setLayout(self.gridLayout)
    self.show()

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
