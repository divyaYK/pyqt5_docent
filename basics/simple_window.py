import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Simple Window")
    self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())