from pyglet.shapes import Rectangle
from numpy import array as vector
import random

class Walker:
    def __init__(self, x, y):
        self.pos = vector([x, y])

    def update(self, dt):
        self.pos[0] += (random.randrange(3) - 1)     # range -1 through 1
        self.pos[1] += (random.randrange(3) - 1)     # range -1 through 1

    def draw(self):
        Rectangle(self.pos[0], self.pos[1], 1, 1).draw()

