import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 300)
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.layout.addWidget(self.display)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['CLEAR']
        ]
        for button_row in buttons:
            row_layout = QHBoxLayout()
            for button_label in button_row:
                button = QPushButton(button_label)
                button.setFixedHeight(50)
                row_layout.addWidget(button)
                button.clicked.connect(self.buttonClicked)
            self.layout.addLayout(row_layout)
        self.setLayout(self.layout)

    def buttonClicked(self):
        button = self.sender()
        if button.text() == '=':
            self.display.setText(str(eval(self.display.text())))
        elif button.text() == 'CLEAR':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
