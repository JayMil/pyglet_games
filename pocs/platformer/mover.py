import random
import math
from pyglet.shapes import Circle
from pyglet.window import key

import vector
from vector import X, Y
import enviornment as env

SIZE_SCALE = 20

class Mover:
    ''' Circle to move randomly around screen '''
    def __init__(self, x, y, window, mass=1, radius=16):
        self.radius = math.sqrt(mass) * SIZE_SCALE
        self.window = window

        self.pos = vector.createVector(x, y+self.radius)    # bottom edge at pos?
        self.vel = vector.createVector(0, 0)
        self.acc = vector.createVector(0, 0)
        self.mass = mass
        self.jumping = False
        self.speed = 1
        self.mouse = dict(pressed=False, pos=self.pos)
        self.keys = dict(space=False, left=False, right=False)

    def applyForce(self, force):
        self.acc += force/self.mass

    def drag(self):
        drag = vector.normalize(self.vel)
        drag *= -1

        speed = vector.mag(self.vel)
        drag = vector.withMag(drag, env.DRAG_FORCE * speed * speed)
        self.applyForce(drag)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel += vector.createVector(0, 100)

    def cancel_jump(self):
        pass
        #self.jumping = False

    def handleEdgeCollision(self):
        ''' Handle collision with walls '''

        # collide with bottom
        if self.pos[Y] <=  self.radius:
            self.pos[Y] =  self.radius
            self.vel[Y] *= -1
            self.jumping = False

        # collide with left wall
        if self.pos[X] <= self.radius:
            self.pos[X] = self.radius
            self.vel[X] *= -1
            self.jumping = False
        # collide with right wall
        elif self.pos[X] >= self.window.width - self.radius:
            self.pos[X] = self.window.width - self.radius
            self.vel[X] *= -1
            self.jumping = False

    def update(self, dt):
        if self.mouse['pressed']:
            self.applyForce(env.WIND)

        weight = self.mass * env.GRAVITY
        self.applyForce(weight)

        self.drag()


        if self.keys['left']:
            self.applyForce(vector.createVector((self.speed*-1), 0))
        if self.keys['right']:
            self.applyForce(vector.createVector(self.speed, 0))

        self.handleEdgeCollision()

        self.vel += self.acc
        self.pos += self.vel
        self.acc = vector.createVector(0, 0)

    def draw(self):
        c = Circle(self.pos[X], self.pos[Y], self.radius)
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

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.SPACE:
            self.jump()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.SPACE:
            self.cancel_jump()

        
