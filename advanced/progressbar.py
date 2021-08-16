
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QProgressBar, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Progress Bar Widget")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    self.progressBar = QProgressBar()
    btnStart = QPushButton("Start")
    btnStart.clicked.connect(self.timerStart)
    btnStop = QPushButton("Stop")
    btnStop.clicked.connect(self.timerStop)

    self.count = 0

    self.timer = QTimer()
    self.timer.setInterval(100)
    self.timer.timeout.connect(self.runProgressBar)

    vbox.addWidget(self.progressBar)
    vbox.addLayout(hbox)
    hbox.addWidget(btnStart)
    hbox.addWidget(btnStop)

    self.setLayout(vbox)
    self.show()

  def runProgressBar(self):
    self.count += 1
    self.progressBar.setValue(self.count)
    if self.count == 100:
      self.timer.stop()
      self.count = 0

  def timerStart(self):
    self.timer.start()

  def timerStop(self):
    self.timer.stop()
    self.count = 0

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
