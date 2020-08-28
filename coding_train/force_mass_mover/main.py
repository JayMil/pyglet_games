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


amount_of_movers = 2
movers = []
for i in range(amount_of_movers):
    print(i)
    mass = (i+1)**3
    print(mass)

    xpos = (i+1)**8 + 100
    print(xpos)
    
    mover = Mover(xpos, window.height // 2, window, mass=mass)
    window.push_handlers(mover)
    movers.append(mover)

@window.event
def on_draw():
    global WIND, GRAVITY
    window.clear()

    for mover in movers:
        if mover.mouse['pressed']:
            mover.applyForce(WIND)

        weight = mover.mass * GRAVITY
        mover.applyForce(weight)

        mover.draw()


def update(dt):
    for mover in movers:
        mover.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)
pyglet.app.run()
