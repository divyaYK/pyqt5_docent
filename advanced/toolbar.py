
import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Toolbar")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    menubar = self.menuBar()
    file = menubar.addMenu("File")
    edit = menubar.addMenu("Edit")
    help_menu = menubar.addMenu("Help")

    new = QAction("New Project", self)
    new.setShortcut("Ctrl+N")
    file.addAction(new)
    open = QAction("Open", self)
    file.addAction(open)
    exit = QAction("Exit", self)
    file.addAction(exit)
    # exit.setIcon(QIcon())
    exit.triggered.connect(self.exitFunction)

    tb = self.addToolBar("New Toolbar")
    newTab = QAction("new", self)
    tb.addAction(newTab)
    self.show()

  def exitFunction(self):
    sys.exit()

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
