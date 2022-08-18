from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys


class UI_browser(QMainWindow):
    def __init__(self) -> None:
        super(UI_browser, self).__init__()
        uic.loadUi("browser.ui", self)
        self.setWindowTitle("my own browser")
        self.webEngineView.setUrl(QUrl("https://www.google.com/"))
        self.lineEdit.setText("https://www.google.com/")
        self.lineEdit.installEventFilter(self)
        self.showMaximized()
        self.show()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and
                source is self.lineEdit):
            if (event.key() == Qt.Key_Return):
                self.set_url()
        return super(UI_browser, self).eventFilter(source, event)

    def set_url(self):
        self.webEngineView.setUrl(QUrl(self.lineEdit.text()))


app = QApplication(sys.argv)
window = UI_browser()
app.exec_()
