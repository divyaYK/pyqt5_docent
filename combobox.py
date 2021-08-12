import sys
from PyQt5.QtWidgets import QComboBox, QPushButton, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Combo Box")
    self.UI()

  def UI(self):
    self.combo = QComboBox(self)
    self.combo.move(150, 100)
    button = QPushButton("Save", self)
    button.move(150, 130)
    button.clicked.connect(self.getValue)
    self.combo.addItem("Item 0")
    self.combo.addItems(["Item 1", "Item 2", "Item 3"])
    self.show()

  def getValue(self):
    value = self.combo.currentText()
    print(value)

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()