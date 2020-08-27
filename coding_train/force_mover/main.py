'''
    Mover program to move a circle around the screen with random velocity
    Aapply a gravity force constantly. 
    Apply a wind force when mouse is pressed
    This makes the ball act like a ball

'''
import random
import pyglet
import vector

from mover import Mover

FPS = 120.0
#FPS = 1.0
#FPS = 20.0

window = pyglet.window.Window(1080, 768)

mover = Mover(window.width // 2, window.height // 2, window)
window.push_handlers(mover)

@window.event
def on_draw():
    window.clear()

    if mover.mouse['pressed']:
        wind = vector.createVector(-0.08, 0)
        mover.applyForce(wind)

    grav = vector.createVector(0, -0.1)
    mover.applyForce(grav)

    mover.draw()



pyglet.clock.schedule_interval(mover.update, 1/FPS)
pyglet.app.run()
