import tkinter as tk
from tkinter import ttk
import threading
import time


class FunctionThread(threading.Thread):
    def __init__(self, progress_var):
        super().__init__()
        self.progress_var = progress_var

    def run(self):
        for i in range(101):
            self.progress_var.set(i)
            time.sleep(0.01)


class Example(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title("Progress Bar Example")
        self.master.geometry("250x150")

        self.button = ttk.Button(self.master, text="Start", command=self.start_function1)
        self.button.place(x=50, y=50)

        self.progress_var = tk.IntVar()
        self.progress = ttk.Progressbar(self.master, variable=self.progress_var, maximum=100, length=150)
        self.progress.place(x=50, y=100)

    def start_function1(self):
        self.button.config(state=tk.DISABLED)
        self.progress_var.set(0)

        # Call your own function here
        # For example:
        result = self.my_function()

        self.thread = FunctionThread(self.progress_var)
        self.thread.start()
        self.master.after(20, self.check_thread)

    def check_thread(self):
        if self.thread.is_alive():
            self.master.after(20, self.check_thread)
        else:
            self.function1_complete()

    def function1_complete(self):
        self.button.config(state=tk.NORMAL)
        self.progress_var.set(100)

    def my_function(self):
        # Code Here …
        print("Placeholder Code")


if __name__ == '__main__':
    root = tk.Tk()
    ex = Example(master=root)
    ex.pack()
    root.mainloop()