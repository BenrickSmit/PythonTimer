#!usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import sys

class TimerApp():
    root = ""
    label = ""
    string_title = ""
    int_mins = 30
    int_seconds = 0
    style = ""

    def __init__(self):
        # Create the form
        self.create_widget()

        tk.mainloop()
        return None

    def style_widget(self):
        # Set Title & background
        self.root.configure(background="black")
        self.root.title(self.string_title)
        self.root.geometry("200x60+0+0")
        
        # Ensure always on top
        self.root.attributes("-topmost", True)
        return None

    def create_widget(self):
        # Create the Clock Widget
        self.string_title = "Timer"
        self.root = tk.Tk()
        
        # Create the widget style
        self.style_widget()

        # Create the Timer Label
        self.label = tk.Label(justify="center", text="00:00", font=("Liberation Mono", 36, "bold"), bg="black", fg="red")
        self.label.pack()

        # Update the timer Information
        self.onUpdate()

        return None

    def onUpdate(self):
        # Ensure proper padding
        string_mins = ""
        string_seconds = ""
        if(self.int_mins < 10):
            string_mins = "0"+str(self.int_mins)
        else:
            string_mins = str(self.int_mins)

        if(self.int_seconds < 10):
            string_seconds = "0"+str(self.int_seconds)
        else:
            string_seconds = str(self.int_seconds)

        # Update the time
        string_label = string_mins + ":" + string_seconds
        self.label.configure(text=string_label)

        # Run the funciton every few seconds
        self.decrement_time()
        self.root.after(1000, self.onUpdate)
        return None

    def decrement_time(self):
        # Will decrement the time pair by one second every time
        if (self.int_seconds == 0):
            # Can have a always on bug
            if (self.int_mins == 0):
                self.int_seconds = 0
            else:
                self.int_seconds = 59
                self.int_mins = self.int_mins -1
        else:
            self.int_seconds = self.int_seconds - 1

        if (self.int_seconds <= 0):
            self.int_seconds = 0
        if (self.int_mins <= 0):
            self.int_mins = 0

        # If the timer is at zero
        if (self.int_seconds == 0) and (self.int_mins == 0):
            self.emit_sound()

        return None

    def emit_sound(self):
        sys.stdout.write("\a")