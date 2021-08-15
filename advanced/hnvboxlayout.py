import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QHBoxLayout, QPushButton, QRadioButton, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Horizontal N Vertical Box Layout")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    mainLayout = QVBoxLayout()
    topLayout = QHBoxLayout()
    bottomLayout = QHBoxLayout()
    mainLayout.addLayout(topLayout)
    mainLayout.addLayout(bottomLayout)

    cbox = QCheckBox()
    rbtn = QRadioButton()
    combo = QComboBox()
    btn1 = QPushButton()
    btn2 = QPushButton()

    topLayout.setContentsMargins(100, 10, 20, 20)  # left, top, right, bottom
    topLayout.addWidget(cbox)
    topLayout.addWidget(rbtn)
    topLayout.addWidget(combo)

    bottomLayout.addWidget(btn1)
    bottomLayout.addWidget(btn2)

    self.setLayout(mainLayout)

    self.show()


def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
