import sys, math, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AnalogClock(QWidget):

    def __init__(self, time_label):
        super().__init__()

        self.initUI()
        self.time_label = time_label

        # Start a timer to update the clock every second
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def initUI(self):
        self.setWindowTitle('Analog Clock')
        self.setGeometry(100, 100, 300, 300)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawClock(qp)
        qp.end()

    def drawClock(self, qp):
        # Get the current time
        self.current_time = time.localtime()
        self.hours = self.current_time.tm_hour % 12
        self.minutes = self.current_time.tm_min
        self.seconds = self.current_time.tm_sec

        # Define some colors and pens
        hour_color = QColor(0, 0, 0)
        minute_color = QColor(0, 0, 0)
        second_color = QColor(255, 0, 0)
        marker_color = QColor(0, 0, 0)
        hour_pen = QPen(hour_color, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        minute_pen = QPen(minute_color, 5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        second_pen = QPen(second_color, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        marker_pen = QPen(marker_color, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        # Set the origin point and radius of the clock
        origin = self.rect().center()
        radius = min(origin.x(), origin.y()) - 10

        # Draw the clock face
        qp.setBrush(QBrush(Qt.white))
        qp.drawEllipse(origin, radius, radius)
        
        # Draw the hour markers
        marker_pen.setWidth(2)
        for i in range(12):
            angle = math.pi * i / 6
            dx1 = int((radius - 15) * math.sin(angle))
            dy1 = int(-(radius - 15) * math.cos(angle))
            dx2 = int((radius - 30) * math.sin(angle))
            dy2 = int(-(radius - 30) * math.cos(angle))
            qp.setPen(marker_pen)
            qp.drawLine(origin.x() + dx1, origin.y() + dy1, origin.x() + dx2, origin.y() + dy2)

        # Draw the minute markers
        marker_pen.setWidth(2)
        for i in range(60):
            angle = math.pi * i / 30
            dx1 = int((radius - 10) * math.sin(angle))
            dy1 = int(-(radius - 10) * math.cos(angle))
            dx2 = int((radius - 20) * math.sin(angle))
            dy2 = int(-(radius - 20) * math.cos(angle))
            qp.setPen(marker_pen)
            qp.drawLine(origin.x() + dx1, origin.y() + dy1, origin.x() + dx2, origin.y() + dy2)

        # Draw the hour hand
        hour_pen.setWidth(6)
        hour_angle = math.pi * (self.hours + self.minutes / 60) / 6
        hour_length = 0.6 * radius
        hour_dx = int(hour_length * math.sin(hour_angle))
        hour_dy = int(-hour_length * math.cos(hour_angle))
        qp.setPen(hour_pen)
        qp.drawLine(origin, QPoint(origin.x() + hour_dx, origin.y() + hour_dy))

        # Draw the minute hand
        minute_pen.setWidth(4)
        minute_angle = math.pi * (self.minutes + self.seconds / 60) / 30
        minute_length = 0.8 * radius
        minute_dx = int(minute_length * math.sin(minute_angle))
        minute_dy = int(-minute_length * math.cos(minute_angle))
        qp.setPen(minute_pen)
        qp.drawLine(origin, QPoint(origin.x() + minute_dx, origin.y() + minute_dy))

        # Draw the second hand
        second_angle = math.pi * self.seconds / 30
        second_length = 0.9 * radius
        second_dx = int(second_length * math.sin(second_angle))
        second_dy = int(-second_length * math.cos(second_angle))
        qp.setPen(second_pen)
        qp.drawLine(origin, QPoint(origin.x() + second_dx, origin.y() + second_dy))
        
        self.time_label.setText(str(time.strftime('%I:%M:%S %p')))
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set MainWindow geometry
        self.setFixedSize(300, 350)

        # Create QFont instance to resize label
        self.font = QFont()
        self.font.setPointSize(18)

        # Create a label for the displaying digital time
        self.time_label = QLabel('placeholder', self)
        self.time_label.setFont(self.font)
        self.time_label.resize(200, 20)
        self.time_label.move(80, 310)

        # Create the analog clock widget and add it to the main window
        self.clock_widget = AnalogClock(self.time_label)
        self.clock_widget.setFixedSize(300, 300)
        self.setCentralWidget(self.clock_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())