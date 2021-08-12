import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Playing with QLineEdit")
    self.UI()

  def UI(self):
    self.nameTextBox = QLineEdit(self)
    self.nameTextBox.setPlaceholderText("Please Enter Your Name")
    self.nameTextBox.move(120, 50)
    self.passTextBox = QLineEdit(self)
    self.passTextBox.setPlaceholderText("Please Enter Your Password")
    self.passTextBox.setEchoMode(QLineEdit.Password)
    self.passTextBox.move(120, 80)
    button = QPushButton("Save", self)
    button.move(180, 110)
    button.clicked.connect(self.getValues)
    self.show()

  def getValues(self):
    name = self.nameTextBox.text()
    password = self.passTextBox.text()
    print(name, password)

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
