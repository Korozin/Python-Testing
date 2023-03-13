import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('270x300')
        self.display = tk.Entry(width=20, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['CLEAR']
        ]
        for i, row in enumerate(buttons, start=1):
            for j, button_label in enumerate(row):
                button = tk.Button(text=button_label, width=4, height=2, font=('Arial', 14))
                button.grid(row=i, column=j)
                button.bind('<Button-1>', self.buttonClicked)

    def buttonClicked(self, event):
        button = event.widget
        if button['text'] == '=':
            expression = self.display.get()
            try:
                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Error')
        elif button['text'] == 'CLEAR':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, button['text'])

if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
