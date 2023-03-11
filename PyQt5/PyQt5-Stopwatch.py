import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

class StopwatchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setFixedSize(300, 120)

        self.running = False
        self.elapsed_time = 0

        # Create the labels to display the elapsed time
        self.elapsed_time_label = QLabel("00:00:00.000")
        self.elapsed_time_label.setAlignment(Qt.AlignCenter)
        self.elapsed_time_label.setStyleSheet("font-size: 28pt;")

        # Create the start and stop buttons
        self.start_button = QPushButton("Start", clicked=self.start_stopwatch)
        self.start_button.setStyleSheet("font-size: 14pt;")
        self.stop_button = QPushButton("Stop", clicked=self.stop_stopwatch)
        self.stop_button.setStyleSheet("font-size: 14pt;")

        # Create the reset button
        self.reset_button = QPushButton("Reset", clicked=self.reset_stopwatch)
        self.reset_button.setStyleSheet("font-size: 14pt;")

        # Create horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)

        # Create vertical layout for the labels and buttons
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.elapsed_time_label)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def start_stopwatch(self):
        if not self.running:
            self.start_time = QDateTime.currentDateTime()
            self.running = True
            self.update_time()

    def stop_stopwatch(self):
        if self.running:
            self.elapsed_time += self.start_time.msecsTo(QDateTime.currentDateTime()) / 1000
            self.running = False

    def reset_stopwatch(self):
        self.elapsed_time = 0
        self.elapsed_time_label.setText("00:00:00.000")

    def update_time(self):
        if self.running:
            elapsed_time_secs = self.elapsed_time + self.start_time.msecsTo(QDateTime.currentDateTime()) / 1000
            elapsed_time_str = self.format_elapsed_time(elapsed_time_secs)
            self.elapsed_time_label.setText(elapsed_time_str)
            QTimer.singleShot(10, self.update_time)

    def format_elapsed_time(self, elapsed_time_secs):
        minutes, seconds = divmod(elapsed_time_secs, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopwatchApp()
    stopwatch.show()
    sys.exit(app.exec_())