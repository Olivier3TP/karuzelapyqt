import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.image.setPixmap(QPixmap('./pies.jpg'))
        self.ui.pushButton.clicked.connect(self.prev)
        self.ui.pushButton_2.clicked.connect(self.next)
        self.images = ['pies.jpg', 'pies2.jpg', 'pies3.jpg']
        self.index = 0
        self.show()

    def prev(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.images) - 1
        self.ui.image.setPixmap(QPixmap(self.images[self.index]))

    def next(self):
        self.index += 1
        if self.index == len(self.images):
            self.index = 0
        self.ui.image.setPixmap(QPixmap(self.images[self.index]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())