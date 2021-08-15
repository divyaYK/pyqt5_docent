import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Form Layout")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    formLayout = QFormLayout()
    formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
    name_text = QLabel("Name: ")
    name_input = QLineEdit()
    pass_text = QLabel("Password: ")
    pass_input = QLineEdit()

    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(QPushButton("Enter"))
    hbox.addWidget(QPushButton("Exit"))

    formLayout.addRow(name_text, name_input)
    formLayout.addRow(pass_text, pass_input)
    formLayout.addRow(QLabel("Country: "), QComboBox())
    formLayout.addRow(hbox)

    self.setLayout(formLayout)
    self.show()


def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
