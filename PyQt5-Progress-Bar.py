import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal


class FunctionThread(QThread):
    progress_update = pyqtSignal(int)

    def run(self):
        for i in range(101):
            self.progress_update.emit(i)
            self.msleep(10)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Progress Bar Example')

        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.start_function1)
        self.button.move(50, 50)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 100, 150, 20)

    def start_function1(self):
        self.button.setEnabled(False)
        self.progress.setValue(0)

        # Call your own function here
        # For example:
        result = self.my_function()

        self.thread = FunctionThread()
        self.thread.progress_update.connect(self.update_progress_bar)
        self.thread.finished.connect(self.function1_complete)
        self.thread.start()

    def update_progress_bar(self, value):
        self.progress.setValue(value)

    def function1_complete(self):
        self.button.setEnabled(True)
        self.progress.setValue(100)
        
    def my_function(self):
        # Code Here …
        print("Placeholder Code")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
