import tkinter as tk
from datetime import datetime

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.master.resizable(False, False)
        
        self.running = False
        self.elapsed_time = 0
        
        # Create the labels to display the elapsed time
        self.elapsed_time_var = tk.StringVar()
        self.elapsed_time_var.set("00:00:00.000")
        self.elapsed_time_label = tk.Label(master, textvariable=self.elapsed_time_var, font=("Helvetica", 32))
        self.elapsed_time_label.pack(padx=20, pady=10)
        
        # Create the start and stop buttons
        self.start_button = tk.Button(master, text="Start", command=self.start_stopwatch, font=("Helvetica", 14))
        self.start_button.pack(padx=10, pady=5, side=tk.LEFT)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_stopwatch, font=("Helvetica", 14))
        self.stop_button.pack(padx=10, pady=5, side=tk.LEFT)
        
        # Create the reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_stopwatch, font=("Helvetica", 14))
        self.reset_button.pack(padx=10, pady=5, side=tk.LEFT)
    
    def start_stopwatch(self):
        if not self.running:
            self.start_time = datetime.now()
            self.running = True
            self.update_time()
    
    def stop_stopwatch(self):
        if self.running:
            self.elapsed_time += (datetime.now() - self.start_time).total_seconds()
            self.running = False
    
    def reset_stopwatch(self):
        self.elapsed_time = 0
        self.elapsed_time_var.set("00:00:00.000")
    
    def update_time(self):
        if self.running:
            elapsed_time_secs = self.elapsed_time + (datetime.now() - self.start_time).total_seconds()
            elapsed_time_str = self.format_elapsed_time(elapsed_time_secs)
            self.elapsed_time_var.set(elapsed_time_str)
            self.master.after(10, self.update_time)
    
    def format_elapsed_time(self, elapsed_time_secs):
        minutes, seconds = divmod(elapsed_time_secs, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02.0f}:{minutes:02.0f}:{seconds:06.3f}"
        

root = tk.Tk()
app = StopwatchApp(root)
root.mainloop()