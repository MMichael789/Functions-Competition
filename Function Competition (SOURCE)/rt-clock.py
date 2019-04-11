#!/usr/bin/env python2.7
# A program that uses Tkinter, time and datetime to show the date with a real-time clock
# Made by Michael S David, Ethan Kissoon and Kurt Pondevida

from Tkinter import *
from datetime import date, time, datetime
import time

# Initialize window
root = Tk()
root.title("Real-Time Date and Clock Display")
root.configure(background="#94d7ff")

# Initialize global variables
date_today = date.today().strftime("%A, %B %d, %Y")
time1 = ""

# Initialize widgets
clock = Label(root, font=("arial", 42, "bold"), bg="#94d7ff", fg="black")
clock.place(relx=0.5, rely=0.7, anchor=CENTER)
current_date = Label(root, font=("arial", 21), text=date_today, bg="#94d7ff", fg="black")
current_date.place(relx=0.5, rely=0.3, anchor=CENTER)

# Function for placing the window on the center of the screen
def center_window(width=300, height=200):
    '''
    DOCSTRING: Display function that gets screen's
    width and height and centers the window in the middle of it 
    '''
    # Gets screen's width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculates the position for the "x" and "y" coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

center_window(500, 400)

# Function for updating time displayed
def clock_tick():
    '''
    DOCSTRING: Clock function that gets system time, 
    converts it to 12-hour time and updates the display
    '''
    global time1
    time2 = ""

    # Get current local system time
    sys_time = time.strftime('%H:%M:%S')
    select_time = int(sys_time[:2])

    # System time is in 24-hour time, so the following "if" series converts it to 12-hour time
    if select_time > 12:
        time2 = "%d%s PM" % (select_time - 12, sys_time[2:])
    elif select_time == 0:
        time2 = "%d%s AM" % (12, sys_time[2:])
    else:
        time2 = "%s AM" % (sys_time)

    # If the time string has changed, update it on the GUI
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    # Function calls itself every 200 milliseconds to update the time displayed on the GUI as needed (Recursive function)
    clock.after(200, clock_tick)

clock_tick()
root.mainloop()
