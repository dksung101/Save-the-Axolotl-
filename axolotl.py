from cmu_112_graphics import *


def appStarted(app):
    app.level = 0
    app.r = 100
    app.rm = app.r*45/100
    app.re = app.rm/3 #radius*45/300
    app.ra = app.re*4/5 #radius*45/600
    app.cx = app.width/2
    app.cy = app.height/2 + app.r

def keyPressed(app, event):
    if event.key in ['Up', 'Right'] and app.level<5:
        app.level += 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1


def redrawAll(app, canvas):
    margin = min(app.width, app.height)//10
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')
    canvas.create_text(app.width/2, margin,
                       text = 'Use arrows to change level',
                       font = 'Arial ' + str(int(margin/4)),
                       anchor='s')
