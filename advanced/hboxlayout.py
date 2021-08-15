import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Horizontal Box Layout")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    hbox = QHBoxLayout()
    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")
    button3 = QPushButton("Button 3")

    hbox.addStretch()
    hbox.addWidget(button1)
    hbox.addWidget(button2)
    hbox.addWidget(button3)
    hbox.addStretch()

    self.setLayout(hbox)

    self.show()


def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
