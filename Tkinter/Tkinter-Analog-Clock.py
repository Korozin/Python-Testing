import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()
        self.time_label = tk.Label(self.master, font=('Arial', 24))
        self.time_label.pack()
        self.draw_clock()
        self.update_clock()

    def draw_clock(self):
        # Draw the clock face
        self.canvas.create_oval(50, 50, 250, 250, width=2)

        # Draw the hour markers
        for i in range(12):
            angle = math.radians(30*i-90)
            x1 = 150 + 100*math.cos(angle)
            y1 = 150 + 100*math.sin(angle)
            x2 = 150 + 120*math.cos(angle)
            y2 = 150 + 120*math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=3)

        # Draw the minute markers
        for i in range(60):
            angle = math.radians(6*i-90)
            x1 = 150 + 100*math.cos(angle)
            y1 = 150 + 100*math.sin(angle)
            x2 = 150 + 110*math.cos(angle)
            y2 = 150 + 110*math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=1)

        # Draw the hour hand
        self.hour_hand = self.canvas.create_line(150, 150, 150, 100, width=4)

        # Draw the minute hand
        self.minute_hand = self.canvas.create_line(150, 150, 150, 80, width=2)

        # Draw the second hand
        self.second_hand = self.canvas.create_line(150, 150, 150, 60, width=1, fill='red')

    def update_clock(self):
        # Get the current time
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Calculate the angles of the hands
        hour_angle = math.radians(30*hour + minute/2 - 90)
        minute_angle = math.radians(6*minute - 90)
        second_angle = math.radians(6*second - 90)

        # Rotate the hands
        self.canvas.coords(self.hour_hand, 150, 150, 150 + 60*math.cos(hour_angle), 150 + 60*math.sin(hour_angle))
        self.canvas.coords(self.minute_hand, 150, 150, 150 + 80*math.cos(minute_angle), 150 + 80*math.sin(minute_angle))
        self.canvas.coords(self.second_hand, 150, 150, 150 + 90*math.cos(second_angle), 150 + 90*math.sin(second_angle))

        # Update the time label
        time_str = time.strftime('%I:%M:%S %p', current_time)
        self.time_label.config(text=time_str)

        # Update the clock every second
        self.master.after(1000, self.update_clock)

root = tk.Tk()
root.title("Analog Clock")
clock = AnalogClock(root)
root.mainloop()