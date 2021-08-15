import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Tab Widget")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    mainLayout = QVBoxLayout()
    self.tabs = QTabWidget()

    self.tab1 = QWidget()
    self.tab2 = QWidget()
    self.tabs.addTab(self.tab1, "First")
    self.tabs.addTab(self.tab2, "Second")


    mainLayout.addWidget(self.tabs)
    self.setLayout(mainLayout)
    self.show()

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
