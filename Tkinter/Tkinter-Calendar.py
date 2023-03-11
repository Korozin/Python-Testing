import calendar
import tkinter as tk

class CalendarApp:

    def __init__(self, master):
        self.master = master
        self.year = tk.IntVar()
        self.month = tk.IntVar()
        self.year.set(calendar.datetime.date.today().year)
        self.month.set(calendar.datetime.date.today().month)
        self.create_widgets()

    def create_widgets(self):
        self.prev_year_btn = tk.Button(self.master, text="<<", command=self.prev_year)
        self.prev_year_btn.grid(row=0, column=0)
        self.prev_month_btn = tk.Button(self.master, text="<", command=self.prev_month)
        self.prev_month_btn.grid(row=0, column=1)
        self.next_month_btn = tk.Button(self.master, text=">", command=self.next_month)
        self.next_month_btn.grid(row=0, column=5)
        self.next_year_btn = tk.Button(self.master, text=">>", command=self.next_year)
        self.next_year_btn.grid(row=0, column=6)

        self.year_lbl = tk.Label(self.master, textvariable=self.year)
        self.year_lbl.grid(row=0, column=3)
        self.month_lbl = tk.Label(self.master, text=calendar.month_name[self.month.get()], font=("TkDefaultFont", 14))
        self.month_lbl.grid(row=1, column=3)

        self.month_name_lbl = tk.Label(self.master, text=calendar.month_name[self.month.get()], font=("TkDefaultFont", 14))

        self.weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for col, weekday in enumerate(self.weekdays):
            label = tk.Label(self.master, text=weekday, bg='lightgrey', width=8)
            label.grid(row=2, column=col)

        self.update_calendar()

    def update_calendar(self):
        month_cal = calendar.monthcalendar(self.year.get(), self.month.get())
        for row, week in enumerate(month_cal):
            for col, day in enumerate(week):
                if day == 0:
                    label = tk.Label(self.master, text='', width=8)
                else:
                    label_text = str(day)
                    label = tk.Label(self.master, text=label_text, width=8)
                label.grid(row=row+3, column=col)

    def prev_year(self):
        self.year.set(self.year.get() - 1)
        self.update_calendar()

    def next_year(self):
        self.year.set(self.year.get() + 1)
        self.update_calendar()

    def prev_month(self):
        if self.month.get() == 1:
            self.year.set(self.year.get() - 1)
            self.month.set(12)
        else:
            self.month.set(self.month.get() - 1)
        self.update_calendar()
        self.month_lbl.configure(text=calendar.month_name[self.month.get()])

    def next_month(self):
        if self.month.get() == 12:
            self.year.set(self.year.get() + 1)
            self.month.set(1)
        else:
            self.month.set(self.month.get() + 1)
        self.update_calendar()
        self.month_lbl.configure(text=calendar.month_name[self.month.get()])

root = tk.Tk()
root.title("Calendar")
app = CalendarApp(root)
root.mainloop()