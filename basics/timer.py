import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("Timer")
    self.UI()

  def UI(self):
    self.colorLabel = QLabel(self)
    self.colorLabel.resize(250, 250)
    self.colorLabel.setStyleSheet("background-color: green")
    self.colorLabel.move(100, 50)

    btnStart = QPushButton("Start", self)
    btnStart.move(80, 300)
    btnStart.clicked.connect(self.start)
    btnStop = QPushButton("Stop", self)
    btnStop.move(190, 300)
    btnStop.clicked.connect(self.stop)

    self.timer = QTimer()
    self.timer.setInterval(100)
    self.timer.timeout.connect(self.changeColor)
    self.value = 0
    self.show()

  def changeColor(self):
    if self.value==0:
      self.colorLabel.setStyleSheet("background-color: yellow")
      self.value = 1
    else:
      self.colorLabel.setStyleSheet("background-color: pink")
      self.value = 0

  def start(self):
    self.timer.start()

  def stop(self):
    self.timer.stop()

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()