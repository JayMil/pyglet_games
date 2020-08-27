import random
from pyglet.shapes import Circle
import vector

class Mover:
    ''' Circle to move randomly around screen '''
    def __init__(self, x, y, size=5):
        self.size = size
        self.pos = vector.createVector(x, y)
        self.vel = vector.createRandomNormalizedVector(random.randrange(3) + 1)

    def update(self, dt):
        self.acc = vector.createRandomNormalizedVector()
        self.vel += self.acc
        self.vel = vector.limit(self.vel, 2)
        self.pos += self.vel

    def draw(self):
        c = Circle(self.pos[0], self.pos[1], self.size)
        c.opacity = 100
        c.draw()

        
