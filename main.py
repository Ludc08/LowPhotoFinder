import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QIcon, QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUi()
        
    def initUi(self):
        
        QToolTip.setFont(QFont('TimesNewRoman', 10))
        
        self.setToolTip('Need <b>some pictures<b>?')
        
        btn = QPushButton('Button', self)
        btn.setToolTip
        
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images.png'))
        
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    