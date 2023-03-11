import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTimeEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QTime, QTimer

class AlarmClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Alarm Clock')
        self.setGeometry(100, 100, 400, 150)
        layout = QVBoxLayout()

        # Time selection
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat('hh:mm')
        self.time_edit.setTime(QTime.currentTime())
        layout.addWidget(QLabel('Set Alarm Time:'))
        layout.addWidget(self.time_edit)

        # Alarm button
        self.alarm_button = QPushButton('Set Alarm', self)
        self.alarm_button.clicked.connect(self.set_alarm)
        layout.addWidget(self.alarm_button)

        # Snooze button
        self.snooze_button = QPushButton('Snooze', self)
        self.snooze_button.clicked.connect(self.snooze_alarm)
        self.snooze_button.setEnabled(False)
        layout.addWidget(self.snooze_button)

        # Message label
        self.message_label = QLabel('', self)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_alarm)

        self.show()

    def set_alarm(self):
        alarm_time = self.time_edit.time().toString('hh:mm')
        self.alarm_button.setEnabled(False)
        self.time_edit.setEnabled(False)
        self.snooze_button.setEnabled(True)
        self.message_label.setText(f'Alarm set for {alarm_time}')

        self.alarm_triggered = False
        self.alarm_time = QTime.fromString(alarm_time, 'hh:mm')
        self.timer.start(1000)

    def snooze_alarm(self):
        snooze_time = self.alarm_time.addSecs(300)  # Snooze for 5 minutes
        self.time_edit.setTime(snooze_time)
        self.set_alarm()

    def check_alarm(self):
        current_time = QTime.currentTime()
        if current_time.hour() == self.alarm_time.hour() and current_time.minute() == self.alarm_time.minute() and not self.alarm_triggered:
            self.alarm_triggered = True
            QMessageBox.information(self, 'Alarm', 'Wake up!')
            self.reset_alarm()

    def reset_alarm(self):
        self.alarm_button.setEnabled(True)
        self.time_edit.setEnabled(True)
        self.snooze_button.setEnabled(False)
        self.message_label.setText('')
        self.alarm_triggered = False
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    alarm_clock = AlarmClock()
    sys.exit(app.exec_())