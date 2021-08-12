import sys
from PyQt5.QtWidgets import QLineEdit, QListWidget, QPushButton, QWidget, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 640, 480)  # x, y and w, h
    self.setWindowTitle("List")
    self.UI()

  def UI(self):
    self.addRecord = QLineEdit(self)
    self.addRecord.move(100, 50)
    self.listWidget = QListWidget(self)
    self.listWidget.move(100, 80)

    list1 = ["Male", "Female", "Others"]
    self.listWidget.addItems(list1)
    self.listWidget.addItem("Prefer not to say")

    btnAdd = QPushButton("Add", self)
    btnAdd.move(360, 80)
    btnAdd.clicked.connect(self.funcAdd)
    btnDelete = QPushButton("Delete", self)
    btnDelete.move(360, 110)
    btnDelete.clicked.connect(self.funcDelete)
    btnGet = QPushButton("Get", self)
    btnGet.move(360, 140)
    btnGet.clicked.connect(self.funcGet)
    btnDeleteAll = QPushButton("Delete All", self)
    btnDeleteAll.move(360, 170)
    btnDeleteAll.clicked.connect(self.funcDeleteAll)

    self.show()

  def funcAdd(self):
    value = self.addRecord.text()
    self.listWidget.addItem(value)
    self.addRecord.setText("")

  def funcDelete(self):
    id = self.listWidget.currentRow()
    self.listWidget.takeItem(id)

  def funcGet(self):
    value = self.listWidget.currentItem().text()
    print(value)

  def funcDeleteAll(self):
    self.listWidget.clear()

def main():
  app = QApplication(sys.argv)
  window = Window()
  sys.exit(app.exec_())

if __name__=='__main__':
  main()