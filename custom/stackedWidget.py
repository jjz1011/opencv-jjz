from custom.tableWidget import *
from config import tables

#最右侧显示已经被执行的操作
class StackedWidget(QStackedWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        for table in tables:
            self.addWidget(table(parent=parent))
        self.setMinimumWidth(200)
