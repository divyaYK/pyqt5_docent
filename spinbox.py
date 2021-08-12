import sys
from PyQt5.QtWidgets import QSpinBox, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("SpinBox")
    self.UI()

  def UI(self):
    self.spinBox = QSpinBox(self)
    self.spinBox.move(150, 100)
    self.spinBox.setMinimum(25)
    self.spinBox.setMaximum(50)
    # self.spinBox.setRange(25, 50)
    self.spinBox.setPrefix("$")
    self.spinBox.setSuffix(" USD")
    self.spinBox.setSingleStep(5)
    self.spinBox.valueChanged.connect(self.getValue)
    self.show()

  def getValue(self):
    value = self.spinBox.value()
    print(value)

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()