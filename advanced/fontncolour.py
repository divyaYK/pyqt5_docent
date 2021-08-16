
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFontDialog, QHBoxLayout, QPushButton, QTextEdit, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Font & Colour Dialog")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    self.editor = QTextEdit()

    fontBtn = QPushButton("Change Font")
    fontBtn.clicked.connect(self.changefont)
    colorBtn = QPushButton("Change Colour")
    colorBtn.clicked.connect(self.changecolour)

    hbox.addStretch()
    hbox.addWidget(fontBtn)
    hbox.addWidget(colorBtn)
    hbox.addStretch()
    vbox.addWidget(self.editor)
    vbox.addLayout(hbox)

    self.setLayout(vbox)
    self.show()

  def changefont(self):
    font = QFontDialog.getFont()
    self.editor.setCurrentFont(font[0])

  def changecolour(self):
    colour = QColorDialog.getColor()
    self.editor.setTextColor(colour)

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
