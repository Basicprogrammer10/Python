from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import sys
import ctypes
import time
from PyQt5.QtGui import QIcon


def window():
    myappid = 'connorcode.2b2t.queueAlert.001'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    widget = QWidget()
    layout = QVBoxLayout()
    app.setStyle('Fusion')
    app.setWindowIcon(QIcon('Icon.ico'))
    app.setStyleSheet("QLabel { color:#13a10e; }")
    app.setStyleSheet("QLabel { color:#E5AF09; }")
    textLabel = QLabel(widget)
    textLabel.setTextFormat(3)
    textLabel.setText("# Position in queue: 100")
    layout.addWidget(textLabel)
    widget.setLayout(layout)
    widget.setWindowTitle("2B2T Queue Alert | Sigma76")
    widget.show()
    time.sleep(5)
    textLabel.setText("# Position in queue: 10000")
    widget.show()
    time.sleep(5)
    textLabel.setText("# Position in queue: 10000000")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
