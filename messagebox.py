import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QApplication

font = QFont("Times New Roman", 12)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Message Box")
    self.UI()

  def UI(self):
    button = QPushButton("Click Me", self)
    button.setFont(font)
    button.move(200, 150)
    button.clicked.connect(self.messageBox)
    self.show()

  def messageBox(self):
    mbox = QMessageBox.question(self, "Warning!", "You might Exit?",
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
    if mbox == QMessageBox.Yes:
      sys.exit()
    else:
      print("Yay, you didn't exit.")

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
