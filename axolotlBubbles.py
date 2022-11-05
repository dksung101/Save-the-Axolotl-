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

def mousePressed(app, event):
    pass

def drawBubbles(app, canvas):
    for (row, col, speed) in app.bubbles:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, width=1.5)
    
def moveBubbleUp(app):
    newLocations = []
    # speed = random.randint(0, 3)

    for (row, col, speed) in app.bubbles:
        newCol = col
        newRow = row-speed
        if (newRow < app.rows) and (newRow>=0):
            newLocations.append((newRow, newCol, speed))
    app.bubbles = newLocations
    
def createBubble(app):
    row = app.rows-1
    col = random.randint(0, app.cols-1)
    speed = random.randint(1, 3)*0.2
    app.bubbles.append((row, col, speed))
    
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


def redrawAll(app, canvas):
    drawBubbles(app, canvas)

runApp(width=400, height=800)