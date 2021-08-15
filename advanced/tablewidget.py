import sys
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Table Widget")
    self.setGeometry(50, 50, 640, 480)
    self.UI()

  def UI(self):
    vbox = QVBoxLayout()
    self.table = QTableWidget()
    btn = QPushButton("Get")
    self.table.setRowCount(5)
    self.table.setColumnCount(3)
    self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
    self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))
    self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Address"))

    self.table.setItem(0, 0, QTableWidgetItem("hello"))
    self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    btn.clicked.connect(self.getValue)

    vbox.addWidget(self.table)
    vbox.addWidget(btn)
    self.setLayout(vbox)

    self.show()

  def getValue(self):
    for item in self.table.selectedItems():
      print(item.text(), item.row(), item.column())

def main():
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())


if __name__ == "__main__":
  main()
