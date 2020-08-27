import random
from pyglet.shapes import Circle
import vector
from vector import X, Y

class Mover:
    ''' Circle to move randomly around screen '''
    def __init__(self, x, y, window, radius=16):
        self.radius = radius
        self.window = window
        self.pos = vector.createVector(x, y)
        self.vel = vector.createRandomNormalizedVector(random.randrange(3) + 1)
        self.acc = vector.createVector(0, 0)
        self.mouse = dict(pressed=False, pos=self.pos)

    def applyForce(self, force):
        self.acc += force

    def handleEdgeCollision(self):
        if self.pos[Y] <=  self.radius:
            self.pos[Y] =  self.radius
            self.vel[Y] *= -1

        if self.pos[X] <= 0 + self.radius:
            self.pos[X] = 0 + self.radius
            self.vel[X] *= -1
        elif self.pos[X] >= self.window.width - self.radius:
            self.pos[X] = self.window.width - self.radius
            self.vel[X] *= -1

    def update(self, dt):

        self.vel += self.acc
        #self.vel = vector.limit(self.vel, 3)
        self.pos += self.vel
        self.acc = vector.createVector(0, 0)
        self.handleEdgeCollision()

    def draw(self):
        c = Circle(self.pos[X], self.pos[Y], (self.radius*2))
        c.opacity = 100
        c.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        ''' Capture position of mouse on mouse move '''
        self.mouse['pos'] = vector.createVector(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        ''' Capture mouse press '''
        self.mouse['pressed'] = True

    def on_mouse_release(self, x, y, button, modifiers):
        ''' Capture mouse release '''
        self.mouse['pressed'] = False

        
