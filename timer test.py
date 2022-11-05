import tkinter as tk
from tkinter import simpledialog 
from cmu_112_graphics import *
import math, copy
import time

appWindow = tk.Tk() 
ans = simpledialog.askstring("Input", "Enter desired duration",
                                parent=appWindow)

def mean(x,y):
    return (x+y)/2

def appStarted(app):
    app.cx, app.cy = app.width/2, app.height/2
    app.timer = int(ans)*60
    mins, secs = divmod(app.timer, 60)
    app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
    app.timerCoords = (0.9*app.cx, 1.4*app.cy, 1.1*app.cx, 1.6*app.cy)

def timerFired(app):
    app.timerDelay = 1000
    mins, secs = divmod(app.timer, 60)
    app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
    app.timer -= 1

# def keyPressed(app, event):

# def mousePressed(app, event):
#     if event.x == 

def drawTimer(app, canvas):
    fontSize = int((app.timerCoords[3]-app.timerCoords[1])//3)
    canvas.create_rectangle(
        app.timerCoords[0], app.timerCoords[1], 
        app.timerCoords[2], app.timerCoords[3], 
        fill='blue')
    canvas.create_text(
        app.cx, int(mean(app.timerCoords[3], app.timerCoords[1])), 
        text=f"{app.timeFormatted}", font=f'Arial {fontSize} bold')

# def drawTenMinButton(app,canvas):

# def drawTwentyMinButton(app,canvas):

# def drawCustTimerutton(app, canvas):

def redrawAll(app, canvas):
    drawTimer(app, canvas)

appWidth = 800
appHeight = (appWidth//16)*9
runApp(width=appWidth, height=appHeight)