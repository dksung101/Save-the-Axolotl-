import tkinter as tk
from tkinter import simpledialog 
from cmu_112_graphics import *
import math, copy
import time

def mean(x,y):
    return (x+y)/2

def appStarted(app):
    app.timerConfigState = False
    app.cx, app.cy = app.width/2, app.height/2
    app.timerDuration = None
    app.timeFormatted = None
    app.timerCoords = (0.75*app.cx, 1.4*app.cy, 1.25*app.cx, 1.6*app.cy)

def timerFired(app):
    app.timerDelay = 1000
    if app.timerDuration != None:
        mins, secs = app.timerDuration // 60, app.timerDuration % 60
        app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
        app.timerDuration -= 1

def mousePressed(app, event):
    if event.x <= app.timerCoords[2] and event.x >= app.timerCoords[0] \
        and event.y <= app.timerCoords[3] and event.y >= app.timerCoords[1]:
        app.timerDuration = simpledialog.askstring("Timer duration input", 
        "Enter desired timer duration")
        if app.timerDuration != None:
            app.timerDuration = int(app.timerDuration)*60
            mins, secs = app.timerDuration // 60, app.timerDuration % 60
            app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
            app.timerConfigState = True

def drawTimer(app, canvas):
    fontSize = int((app.timerCoords[3]-app.timerCoords[1])//3)
    canvas.create_rectangle(
        app.timerCoords[0], app.timerCoords[1], 
        app.timerCoords[2], app.timerCoords[3], 
        fill='blue', width=0)
    canvas.create_text(
        app.cx, int(mean(app.timerCoords[3], app.timerCoords[1])), 
        text=f"{app.timeFormatted}", font=f'Arial {fontSize} bold', fill='white')

# def drawTenMinButton(app,canvas):
# def drawTwentyMinButton(app,canvas):

def drawCustTimerButton(app, canvas):
    fontSize = int((app.timerCoords[3]-app.timerCoords[1])//3)
    canvas.create_rectangle(
        app.timerCoords[0], app.timerCoords[1], 
        app.timerCoords[2], app.timerCoords[3], 
        fill='white')
    canvas.create_text(
        app.cx, int(mean(app.timerCoords[3], app.timerCoords[1])), 
        text=f"Custom duration", font=f'Arial {fontSize} bold')

def redrawAll(app, canvas):
    if app.timerConfigState:
        drawTimer(app, canvas)
    else: 
        drawCustTimerButton(app, canvas)

appWidth = 800
appHeight = (appWidth//16)*9
runApp(width=appWidth, height=appHeight)