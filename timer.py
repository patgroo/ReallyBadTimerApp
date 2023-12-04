import tkinter as tk


class TimerApp:
    def __init__(self, root):
        self.root = root
        ####
        self.time_var = tk.StringVar(value="00:00:00.000")
        self.continuous_time_var = tk.StringVar(value="00:00:00.000")
        self.pause_time_var = tk.StringVar(value="00:00:00.000")

        self.running = False
        self.stopped = False
        self.milliseconds_elapsed = 0
        self.continuous_milliseconds_elapsed = 0
        self.pause_milliseconds_elapsed = 0
        ###
        # List of colors to switch between
        self.colors_starttimer = ['black', 'green']
        # List of colors to switch between
        self.colors_stoptimer = ['red', 'black']
        self.current_color_index = 0    # Index to keep track of the current color
        ###
        self.continuous_label = tk.Label(
            root, textvariable=self.continuous_time_var, font=("Arial", 24))
        self.continuous_label.pack()

        self.pause_timer_label = tk.Label(
            root, textvariable=self.pause_time_var, font=("Arial", 24))
        self.pause_timer_label.pack()

        self.label = tk.Label(
            root, textvariable=self.time_var, font=("Arial", 48))
        self.label.pack()

        self.start_button = tk.Button(
            root, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.start_button = tk.Button(
            root, text="Round", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side="right", padx=10)

        self.update_timer()

    def switch_color(self):
        # Switch to the next color in the list
        self.current_color_index = (
            self.current_color_index + 1) % len(self.colors_starttimer)
        new_color = self.colors_starttimer[self.current_color_index]
        self.continuous_label.config(fg=new_color)  # Apply the new color
        self.pause_timer_label.config(fg=new_color)  # Apply the new color

    def start_timer(self):
        if self.running:
            self.stopped = True
            self.running = not self.running
        elif not self.running:
            self.stopped = False
            self.running = not self.running
        self.switch_color()  # Change text color to red
        self.start_button.config(text="Pause" if self.running else "Start")

    def start_pause_timer(self):
        self.stopped = not self.stopped
        self.switch_color()

    def reset_timer(self):
        self.milliseconds_elapsed = 0
        self.time_var.set("00:00:00.000")

    def update_timer(self):
        if self.running:
            self.milliseconds_elapsed += 10
            self.continuous_milliseconds_elapsed += 10
        if self.stopped:
            self.pause_milliseconds_elapsed += 10

        self.update_time_str(self.milliseconds_elapsed, self.time_var)
        self.update_time_str(
            self.continuous_milliseconds_elapsed, self.continuous_time_var)
        self.update_time_str(
            self.pause_milliseconds_elapsed, self.pause_time_var)

        self.root.after(10, self.update_timer)  # Update every 10 ms

    def update_time_str(self, milliseconds, time_var):
        hours, remainder = divmod(milliseconds // 1000, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = milliseconds % 1000
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        time_var.set(time_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
