from cmu_112_graphics import *
import tkinter as tk
from tkinter import simpledialog 
import random
from cmu_112_graphics import *
import math, copy
import time

# helper function
def mean(x,y):
    return (x+y)/2

def appStarted(app):
    app.bubbles = []
    app.cols = 20
    app.rows = 40
    app.radius = 0
    app.margin = 0
    app.timerDelay = 50
    app.totalTime=0
    app.count = 0
    #axolotl face
    app.cx, app.cy = app.width/2, app.height/2
    app.rw = 150 
    app.rh = 90
    #lives 
    app.lives = [(320, 30),(360, 30),(400,30)]
    app.heartR = 5
    app.minOil = 5
    app.threshold = 10
    app.mood = 'happy'
    # timer
    # app.timeInSeconds = None    # this is the secondary 30s timer
    app.timerConfigState = None
    app.timerDuration = None
    app.timeFormatted = None
    app.timerCoords = (0.60*app.cx, 1.4*app.cy, 1.4*app.cx, 1.6*app.cy)

def mousePressed(app, event):
    for (row, col, speed, radius) in app.bubbles:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        if (event.x >= x0-radius and event.x <= x1+radius) and (event.y >= y0-radius and event.y <= y1+radius):
            app.bubbles.remove((row, col, speed, radius))
            app.count+=1
            # popBubble(app, (row, col, speed))

    if app.timerConfigState == None and event.x <= app.timerCoords[2] and event.x >= app.timerCoords[0] \
        and event.y <= app.timerCoords[3] and event.y >= app.timerCoords[1]:
        app.timerDuration = simpledialog.askstring("Timer duration input", 
        "Enter desired timer duration")
        if app.timerDuration != None and int(app.timerDuration)>0:
            app.timerDuration = int(app.timerDuration)*60
            mins, secs = app.timerDuration // 60, app.timerDuration % 60
            app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
            app.timerConfigState = True

def drawBubbles(app, canvas):
    for (row, col, speed, radius) in app.bubbles:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0-radius, y0-radius, x1+radius, y1+radius, fill='black')
        
    
def moveBubbleUp(app):
    newLocations = []
    # speed = random.randint(0, 3)

    for (row, col, speed, radius) in app.bubbles:
        newCol = col
        newRow = row-speed
        if (newRow < app.rows) and (newRow>=0):
            newLocations.append((newRow, newCol, speed, radius))
    app.bubbles = newLocations
    
def createBubble(app):
    row = app.rows-1
    col = random.randint(0, app.cols-1)
    speed = random.randint(1, 3)*0.2
    radius = random.randint(5, 25)
    app.bubbles.append((row, col, speed, radius))
    
def getCellBounds(app, row, col):
    colWidth = (app.width-2*app.margin) / app.cols
    rowHeight = (app.height-2*app.margin) / app.rows
    x0 = app.margin + col * colWidth
    x1 = app.margin + (col+1)* colWidth
    y0 = app.margin + row * rowHeight
    y1 = app.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

def timerFired(app):
    print(f"app.totalTime:{app.totalTime}")
    if app.timerConfigState == False:
        app.totalTime+=app.timerDelay
        if app.totalTime%500 == 0 and app.totalTime<=30000:
            createBubble(app) 
        moveBubbleUp(app)
        if app.totalTime > 30000: app.totalTime = 0
    if app.totalTime%1 == 0 and app.timerDuration != None:  # change delay here
        mins, secs = app.timerDuration // 60, app.timerDuration % 60
        app.timeFormatted = '{:02d}:{:02d}'.format(mins, secs)
        app.timerDuration -= 1
    
    if app.timerDuration == 0: 
        app.timerConfigState = False
        app.totalTime = 0
        app.timerDuration = None

    if app.totalTime == 30000 and app.timerConfigState == False: 
        app.timerConfigState = None

    if len(app.lives) == 3:
        app.mood = 'happy'
    elif len(app.lives) == 2:
        app.mood = 'neutral'
    else:
        app.mood = 'frown'

    if app.totalTime == 29950 and app.timerConfigState == False:
        changeLives(app, app.count)
        app.count = 0

def checkMood(app, canvas):
    if len(app.lives) == 3:
        app.mood = 'happy'
    elif len(app.lives) == 2:
        app.mood = 'neutral'
    elif len(app.lives) == 1:
        app.mood = 'frown'
    elif app.timerConfigState==True:
        app.mood = 'sleep'

def drawTimer(app, canvas):
    timeInSeconds = 30-app.totalTime//1000
    if timeInSeconds<0:
        timeInSeconds = 0
    if timeInSeconds > 10:
        canvas.create_text(app.width/2, app.height-640, text=f'{timeInSeconds} seconds left', fill='black', font='TimesNewRoman 12 bold')
    else: 
        canvas.create_text(app.width/2, app.height-640, text=f'Only {timeInSeconds} seconds left!', fill='red', font='TimesNewRoman 12 bold')

def drawCount(app, canvas):
    canvas.create_text(app.width/2, app.height-40, text=f'Score: {app.count}!', fill='red', font='TimesNewRoman 12 bold')

def drawAxolotl(app, canvas, cx, cy, rw, rh):
    #face
    canvas.create_oval(cx-rw, cy-rh, cx+rw, cy+rh, outline = 'black', width = 3, 
                        fill = 'lavenderblush')
    
    #eyeL
    canvas.create_oval(0.55*cx, 0.95*cy, 0.65*cx, cy, outline = 'black', fill = 'black')
    canvas.create_oval(0.6*cx, 0.97*cy, 0.64*cx, 0.99*cy, outline = 'black', fill = 'white')
    #eyeR
    canvas.create_oval(1.4*cx, 0.95*cy, 1.5*cx, cy, outline = 'black', fill = 'black')
    canvas.create_oval(1.41*cx, 0.97*cy, 1.44*cx, 0.99*cy, outline = 'black', fill = 'white')

    #mouth
    if app.mood == 'happy':
        canvas.create_line(0.47*cx, 1.1*cy, cx, 1.3*cy, 1.53*cx, 1.1*cy, 
                            fill="black", width = 3, smooth = True)
        canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
                            fill="black", width = 3, smooth = True)
    elif app.mood == 'neutral':
        canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
                            fill="black", width = 3, smooth = True)
    elif app.mood == 'frown':
        canvas.create_line(0.47*cx, 1.1*cy, cx, cy, 1.53*cx, 1.1*cy, 
                            fill="black", width = 3, smooth = True)
        canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
                            fill="black", width = 3, smooth = True)

    #earR1
    canvas.create_line(1.4*cx, 0.79*cy, 1.8*cx, 0.34*cy, width = 3, fill = 'black')
    canvas.create_line(1.8*cx, 0.34*cy, 1.8*cx, 0.55*cy, 1.56*cx, 0.85*cy, 
                        width = 3, fill = 'black', smooth = True)
    #earR2
    canvas.create_line(1.6*cx, 0.88*cy, 1.9*cx, 0.6*cy, width = 3, fill = 'black')
    canvas.create_line(1.9*cx, 0.6*cy, 1.8*cx, 0.85*cy, 0.99*cx + rw, 0.97*cy, 
                        width = 3, fill = 'black', smooth = True)
    #earR3
    canvas.create_line(cx + rw, cy, 1.95*cx, 0.8*cy, width = 3, fill = 'black')
    canvas.create_line(1.96*cx, 0.8*cy, 1.85*cx, cy, 0.96*cx + rw, 1.1*cy, 
                        width = 3, fill = 'black', smooth = True)

    #earL1
    canvas.create_line(0.6*cx, 0.79*cy, 0.2*cx, 0.34*cy, width = 3, fill = 'black')
    canvas.create_line(0.2*cx, 0.34*cy, 0.2*cx, 0.55*cy, 0.44*cx, 0.85*cy, 
                        width = 3, fill = 'black', smooth = True)
    #earL2
    canvas.create_line(0.4*cx, 0.88*cy, 0.1*cx, 0.6*cy, width = 3, fill = 'black')
    canvas.create_line(0.1*cx, 0.6*cy, 0.2*cx, 0.85*cy, 0.01*cx+0.45*rw, 0.97*cy, 
                        width = 3, fill = 'black', smooth = True)
    #earL3
    canvas.create_line(cx - rw, cy, 0.05*cx, 0.8*cy, width = 3, fill = 'black')
    canvas.create_line(0.05*cx, 0.8*cy, 0.15*cx, cy, 0.36*cx, 1.1*cy, 
                        width = 3, fill = 'black', smooth = True)

def changeLives(app, foodCollected):
    if foodCollected < app.minOil:
        app.lives.pop(0)
        print(app.lives)
    elif foodCollected > app.threshold and len(app.lives) < 3:
        life = app.lives[0] 
        app.lives.insert(0,(life[0] - 40, 30))
    
def drawLives(app, canvas):
    for heart in app.lives:
        cx, cy = heart[0], heart[1]
        canvas.create_arc(cx - app.heartR*2, cy - app.heartR, 
                          cx, cy + app.heartR, 
                          start=0, extent=180, fill="red", outline = "red")
        canvas.create_arc(cx, cy - app.heartR, 
                          cx + app.heartR*2, cy + app.heartR, 
                          start=0, extent=180, fill="red", outline = "red")
        canvas.create_polygon(cx - app.heartR*2, cy,
                              cx + app.heartR*2, cy,
                              cx, cy*1.25, fill = "red")

def drawMainTimer(app, canvas):
    fontSize = int((app.timerCoords[3]-app.timerCoords[1])//3)
    canvas.create_rectangle(
        app.timerCoords[0], app.timerCoords[1], 
        app.timerCoords[2], app.timerCoords[3], 
        fill='blue', width=0)
    canvas.create_text(
        app.cx, int(mean(app.timerCoords[3], app.timerCoords[1])), 
        text=f"{app.timeFormatted}", font=f'Arial {fontSize} bold', fill='white')
    
def drawCustTimerButton(app, canvas):
    fontSize = int((app.timerCoords[3]-app.timerCoords[1])//3)
    canvas.create_rectangle(
        app.timerCoords[0], app.timerCoords[1], 
        app.timerCoords[2], app.timerCoords[3], 
        fill='white')
    canvas.create_text(
        app.cx, int(mean(app.timerCoords[3], app.timerCoords[1])), 
        text=f"Set duration", font=f'Arial {fontSize} bold')

def redrawAll(app, canvas):
    drawAxolotl(app, canvas, app.cx, app.cy, app.rw, app.rh)
    drawLives(app, canvas)
    drawCount(app, canvas)
    if app.timerConfigState == False:
        drawTimer(app, canvas)
        drawBubbles(app, canvas)
    elif app.timerConfigState == True:
        drawMainTimer(app, canvas)
    elif app.timerConfigState == None:
        drawCustTimerButton(app, canvas)

runApp(width=440, height = 680)