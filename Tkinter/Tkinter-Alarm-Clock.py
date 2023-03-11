import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime, time

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm Clock')
        self.geometry('400x150')

        # Time selection
        self.time_var = tk.StringVar(value=datetime.now().strftime('%H:%M'))
        self.time_edit = tk.Entry(self, textvariable=self.time_var, font=('Arial', 20))
        self.time_edit.pack(pady=10)

        # Alarm button
        self.alarm_button = tk.Button(self, text='Set Alarm', font=('Arial', 14), command=self.set_alarm)
        self.alarm_button.pack()

        # Snooze button
        self.snooze_button = tk.Button(self, text='Snooze', font=('Arial', 14), command=self.snooze_alarm, state=tk.DISABLED)
        self.snooze_button.pack()

        # Message label
        self.message_label = tk.Label(self, font=('Arial', 14))
        self.message_label.pack()

        # Timer
        self.alarm_triggered = False
        self.timer = None

    def set_alarm(self):
        try:
            alarm_time = datetime.strptime(self.time_var.get(), '%H:%M').time()
        except ValueError:
            messagebox.showerror('Error', 'Invalid time format')
            return

        current_time = datetime.now().time()
        if alarm_time <= current_time:
            messagebox.showwarning('Warning', 'Alarm time must be in the future')
            return

        self.alarm_button.config(state=tk.DISABLED)
        self.time_edit.config(state=tk.DISABLED)
        self.snooze_button.config(state=tk.NORMAL)
        self.message_label.config(text=f'Alarm set for {alarm_time.strftime("%H:%M")}')

        self.alarm_triggered = False
        self.timer = self.after(1000, self.check_alarm, alarm_time)

    def snooze_alarm(self):
        snooze_time = (datetime.combine(datetime.now().date(), self.alarm_time) + timedelta(minutes=5)).time()
        self.time_var.set(snooze_time.strftime('%H:%M'))
        self.set_alarm()

    def check_alarm(self, alarm_time):
        current_time = datetime.now().time()
        if current_time >= alarm_time and not self.alarm_triggered:
            self.alarm_triggered = True
            messagebox.showinfo('Alarm', 'Wake up!')
            self.reset_alarm()
        else:
            self.timer = self.after(1000, self.check_alarm, alarm_time)

    def reset_alarm(self):
        self.alarm_button.config(state=tk.NORMAL)
        self.time_edit.config(state=tk.NORMAL)
        self.snooze_button.config(state=tk.DISABLED)
        self.message_label.config(text='')
        self.alarm_triggered = False
        self.after_cancel(self.timer)

if __name__ == '__main__':
    alarm_clock = AlarmClock()
    alarm_clock.mainloop()