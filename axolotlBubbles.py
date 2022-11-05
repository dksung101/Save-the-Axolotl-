from cmu_112_graphics import *
import random

def appStarted(app):
    app.bubbles = []
    app.cols = 20
    app.rows = 40
    app.radius = 0
    app.margin = 0
    app.timerDelay = 50
    app.totalTime=0
    app.count = 0

def mousePressed(app, event):
    for (row, col, speed, radius) in app.bubbles:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        if (event.x >= x0-radius and event.x <= x1+radius) and (event.y >= y0-radius and event.y <= y1+radius):
            app.bubbles.remove((row, col, speed, radius))
            app.count+=1
            # popBubble(app, (row, col, speed))

def drawBubbles(app, canvas):
    for (row, col, speed, radius) in app.bubbles:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0-radius, y0-radius, x1+radius, y1+radius, width=1.5)
        
# def popBubble(app):
#     for 
    
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
    app.totalTime+=app.timerDelay
    if app.totalTime%500 == 0:
        createBubble(app)
    moveBubbleUp(app)

def drawCount(app, canvas):
    canvas.create_text(app.width/2, app.height-40, text=f'Score: {app.count}!', fill='red', font='TimesNewRoman 12 bold')

def redrawAll(app, canvas):
    drawBubbles(app, canvas)
    drawCount(app, canvas)

runApp(width=400, height=800)