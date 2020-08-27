import random
from pyglet.shapes import Circle
import vector

class Mover:
    ''' Circle to move randomly around screen '''
    def __init__(self, x, y, size=32):
        self.size = size
        self.pos = vector.createVector(x, y)
        self.vel = vector.createRandomNormalizedVector(random.randrange(3) + 1)
        self.mouse = self.pos

    def update(self, dt):
        self.acc = self.mouse - self.pos
        #self.acc = vector.withMag(self.acc, 0.1)
        self.acc = vector.withMag(self.acc, 5)

        self.vel += self.acc
        self.vel = vector.limit(self.vel, 3)

        self.pos += self.vel

    def draw(self):
        c = Circle(self.pos[0], self.pos[1], self.size)
        c.opacity = 100
        c.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        ''' Capture position of mouse on mouse move '''
        self.mouse = vector.createVector(x, y)
        
