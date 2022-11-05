import tkinter as tk
from tkinter import simpledialog 
from cmu_112_graphics import *
import math, copy
import time
  
# define the countdown func.
# def countdown(t):
#     t *= 60
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         # print(timer, end="\r")
#         time.sleep(1)   # delays execution by 1s
#         t -= 1
      
    # print('Tap to feed Kimchee')

# def feeding():  
  
# input time in seconds
# t = input("Enter the time in minutes: ")
  
# # function call
# countdown(int(t))

appWindow = tk.Tk() 
ans = simpledialog.askstring("Input", "Enter desired duration",
                                parent=appWindow)

def appStarted(app):
    app.cx, app.cy = app.width/2, app.height/2
    app.timer = int(ans)*60
    mins, secs = divmod(app.timer, 60)
    app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)

def timerFired(app):
    app.timerDelay = 1000
    mins, secs = divmod(app.timer, 60)
    app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
    app.timer -= 1


def redrawAll(app, canvas):
    fontSize = app.width//20
    canvas.create_rectangle(app.cx-100, app.cy+50, app.cx+100, app.cy+150, fill='blue')
    canvas.create_text(app.cx, app.cy+100, text=f"{app.timeFormatted}", font=f'Arial {fontSize} bold')

runApp(width=400, height=400)