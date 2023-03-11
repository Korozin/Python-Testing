import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout

class CalendarApp(QCalendarWidget):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle('Calendar App')
        self.resize(500, 400)

        # Set visible grid
        self.setGridVisible(True)
        
""" Man, this was WAY too easy """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = CalendarApp()
    cal.show()
    sys.exit(app.exec_())