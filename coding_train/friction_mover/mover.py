import random
import math
from pyglet.shapes import Circle

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
        self.mouse = dict(pressed=False, pos=self.pos)

    def applyForce(self, force):
        self.acc += force/self.mass

    def friction(self):
        diff = (self.pos[Y] - self.radius)
        if (diff < 1):
            friction = vector.normalize(self.vel)
            friction *= -1

            normal = self.mass
            friction = vector.withMag(friction, env.MU * normal)
            self.applyForce(friction)


    def handleEdgeCollision(self):
        ''' Handle collision with walls '''

        # collide with bottom
        if self.pos[Y] <=  self.radius:
            self.pos[Y] =  self.radius
            self.vel[Y] *= -1

        # collide with left wall
        if self.pos[X] <= self.radius:
            self.pos[X] = self.radius
            self.vel[X] *= -1
        # collide with right wall
        elif self.pos[X] >= self.window.width - self.radius:
            self.pos[X] = self.window.width - self.radius
            self.vel[X] *= -1

    def update(self, dt):
        if self.mouse['pressed']:
            self.applyForce(env.WIND)

        weight = self.mass * env.GRAVITY
        self.applyForce(weight)

        self.friction()
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

        
