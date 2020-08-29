'''
    Drop two balls of different mass
    Apply a gravity force constantly. 
    Apply a wind force when mouse is pressed

'''
import random
import pyglet
import vector

from mover import Mover

FPS = 120.0
WIND = vector.createVector(-0.08, 0)
GRAVITY = vector.createVector(0, -0.1)

window = pyglet.window.Window(1080, 768)


#mover = Mover(window.height // 2, window.height // 2, window, mass=4)
mover = Mover(window.height // 2, 50, window, mass=4)
window.push_handlers(mover)

@window.event
def on_draw():
    global WIND, GRAVITY
    window.clear()
    mover.draw()

    if mover.mouse['pressed']:
        mover.applyForce(WIND)

    weight = mover.mass * GRAVITY
    mover.applyForce(weight)

    mover.friction()
    mover.handleEdgeCollision()


def update(dt):
    mover.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)
pyglet.app.run()
