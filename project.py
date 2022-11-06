############
#Axolotl face
############

from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.rw = 150 
    app.rh = 90

def keyPressed(app, event):
    pass

def drawAxolotl(app, canvas, cx, cy, rw, rh):
    #face
    canvas.create_oval(cx-rw, cy-rh, cx+rw, cy+rh, outline = 'black', width = 3, 
                        fill = 'lavenderblush')
    
    #eyeL
    # canvas.create_oval(0.55*cx, 0.95*cy, 0.65*cx, cy, outline = 'black', fill = 'black')
    # canvas.create_oval(0.6*cx, 0.97*cy, 0.64*cx, 0.99*cy, outline = 'black', fill = 'white')
    #die
    # canvas.create_line(0.55*cx, 0.95*cy, 0.65*cx, cy, fill = 'black', width = 4)
    # canvas.create_line(0.55*cx, cy, 0.65*cx, 0.95*cy, fill = 'black', width = 4)
    #sleep
    canvas.create_line(0.55*cx, 0.975*cy, 0.65*cx, 0.975*cy, fill = 'black', width = 4)

    #eyeR
    # canvas.create_oval(1.4*cx, 0.95*cy, 1.5*cx, cy, outline = 'black', fill = 'black')
    # canvas.create_oval(1.41*cx, 0.97*cy, 1.44*cx, 0.99*cy, outline = 'black', fill = 'white')
    #die
    # canvas.create_line(1.4*cx, 0.95*cy, 1.5*cx, cy, fill = 'black', width = 4)
    # canvas.create_line(1.4*cx, cy, 1.5*cx, 0.95*cy, fill = 'black', width = 4)
    #sleep
    canvas.create_line(1.4*cx, 0.975*cy, 1.5*cx, 0.975*cy, fill = 'black', width = 4)


    #mouth 
    #smiling
    # canvas.create_line(0.47*cx, 1.1*cy, cx, 1.3*cy, 1.53*cx, 1.1*cy, 
    #                     fill="black", width = 3, smooth = True)
    # canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
    #                     fill="black", width = 3, smooth = True)
    # # #mid 
    # canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
    #                     fill="black", width = 3, smooth = True)
    # #frown
    # canvas.create_line(0.47*cx, 1.1*cy, cx, cy, 1.53*cx, 1.1*cy, 
    #                     fill="black", width = 3, smooth = True)
    # canvas.create_line(0.47*cx, 1.1*cy, 1.53*cx, 1.1*cy, 
    #                     fill="black", width = 3, smooth = True)
    #sleep
    canvas.create_oval(cx-0.2*rw,1.1*cy,cx+0.2*rw,1.2*cy-2, outline = 'black', fill = 'salmon', width = 3)

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

def redrawAll(app, canvas):
    drawAxolotl(app, canvas, app.cx, app.cy, app.rw, app.rh)

runApp(width = 440, height = 680)