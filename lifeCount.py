#################################################
# Axolotl Viewer
#################################################

from cmu_112_graphics import *

def appStarted(app):
    # Change location later
    app.lives = [(100, 300),(170, 300),(240,300)]
    app.heartR = 5
    app.minFood = 10
    app.threshold = 30
    app.foodCollected = 20

def drawLives(app, canvas, foodCollected):
    if foodCollected < app.minFood:
        app.lives.pop(0)
    elif foodCollected > app.threshold and len(app.lives) < 3:
        life = app.lives[0] 
        app.lives.insert(0,(life[0] - 70, 300))
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
                              cx, cy*1.05, fill = "red")

def redrawAll(app, canvas):
    drawLives(app, canvas, app.foodCollected)

def runAxolotlViewer():
    runApp(width=440, height=680)

#################################################
# Main
#################################################
def main():
    runAxolotlViewer()

if (__name__ == '__main__'):
    main()
