import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Labels")
    self.UI()

  def UI(self):
    text1 = QLabel("Label 1", self)
    text2 = QLabel("Label 2", self)
    text1.move(100, 50)
    text2.move(200, 50)
    self.show()

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()