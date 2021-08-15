import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Slider Widget")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    vbox = QVBoxLayout()
    self.slider = QSlider(Qt.Horizontal)
    self.slider.setMinimum(0)
    self.slider.setMaximum(100)
    self.slider.setTickPosition(QSlider.TicksAbove)
    self.slider.setTickInterval(10)
    self.slider.valueChanged.connect(self.getValue)

    self.text1 = QLabel("0")
    self.text1.setAlignment(Qt.AlignCenter)
    self.text2 = QLabel("Hi there!")

    vbox.addStretch()
    vbox.addWidget(self.text1)
    vbox.addWidget(self.text2)
    vbox.addWidget(self.slider)
    self.setLayout(vbox)

    self.show()

  def getValue(self):
    value = self.slider.value()
    self.text1.setText(str(value))
    fontSize = value
    font = QFont("Times", fontSize)
    self.text2.setFont(font)


def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
