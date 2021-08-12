import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QRadioButton, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Radio Box")
    self.UI()

  def UI(self):
    self.name = QLineEdit(self)
    self.name.move(150, 50)
    self.name.setPlaceholderText("Name:")
    self.male = QRadioButton("Male", self)
    self.female = QRadioButton("Female", self)
    self.male.move(150, 110)
    self.male.setChecked(True)
    self.female.move(220, 110)
    button = QPushButton("Submit", self)
    button.move(200, 140)
    button.clicked.connect(self.getValues)
    self.show()

  def getValues(self):
    name = self.name.text()
    if self.male.isChecked():
      print("male")
    else:
      print("Female")

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
