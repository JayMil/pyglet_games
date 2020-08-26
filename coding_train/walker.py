'''
    Walker program to draw a path that moves in random directions

'''
import random
import pyglet
from pyglet.shapes import Rectangle

window = pyglet.window.Window(1080, 768)
main_batch = pyglet.graphics.Batch()

x = window.width // 2
y = window.height // 2

def update(dt):
    global x, y
    r = random.randrange(4)
    if r == 0:
        x += 1
    elif r == 1:
        x -= 1
    elif r == 2:
        y += 1
    elif r == 3:
        y -= 1


@window.event
def on_draw():
    #window.clear()
    #main_batch.draw()
    rec = Rectangle(x, y, 1, 1)
    rec.draw()

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
