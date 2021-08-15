import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Vertical Box Layout")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    vbox = QVBoxLayout()
    button1 = QPushButton("Save")
    button2 = QPushButton("Exit")

    vbox.addStretch()
    vbox.addWidget(button1)
    vbox.addWidget(button2)
    vbox.addStretch()

    self.setLayout(vbox)
    self.show()


def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
