import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Simple Window")
    self.UI()

  def UI(self):
    self.text = QLabel("Label Text", self)
    enterButton = QPushButton("Enter", self)
    exitButton = QPushButton("Exit", self)
    self.text.move(160, 50)
    enterButton.move(100, 80)
    exitButton.move(200, 80)
    enterButton.clicked.connect(self.enterFunction)
    exitButton.clicked.connect(self.exitFunction)
    self.show()

  def enterFunction(self):
    self.text.setText("Entered")

  def exitFunction(self):
    self.text.setText("Exited")

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()