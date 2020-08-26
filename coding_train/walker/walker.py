from pyglet.shapes import Rectangle
from numpy import array as vector
import random

class Walker:
    def __init__(self, x, y):
        self.pos = vector([x, y])
        self.vel = vector([1, -1])

    def update(self, dt):
        self.pos += self.vel

    def draw(self):
        Rectangle(self.pos[0], self.pos[1], 5, 5).draw()

