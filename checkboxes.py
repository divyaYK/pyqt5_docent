import sys
from PyQt5.QtWidgets import QCheckBox, QLineEdit, QPushButton, QWidget, QApplication, QLabel

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Simple Window")
    self.UI()

  def UI(self):
    self.name = QLineEdit(self)
    self.surname = QLineEdit(self)
    self.name.move(150, 50)
    self.surname.move(150, 80)
    self.remember = QCheckBox("Remember me", self)
    self.remember.move(150, 110)
    button = QPushButton("Submit", self)
    button.move(200, 140)
    button.clicked.connect(self.submit)
    self.show()

  def submit(self):
    if(self.remember.isChecked()):
      print(f"Name: {self.name.text()}\nSurname: {self.surname.text()}\nRemember me checked")
    else:
      print("Forgot you already")

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()