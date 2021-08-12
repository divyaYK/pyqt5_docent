import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 1050, 600)  # x, y and w, h
    self.setWindowTitle("Images")
    self.UI()

  def UI(self):
    self.image = QLabel(self)
    self.image.setPixmap(QPixmap('./ocean.webp'))
    self.image.move(150, 50)
    self.show()

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
