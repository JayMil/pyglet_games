import pyglet

import gameobjects
from gameobjects import CollisionObject
from hero import Facing

class Map():
    def __init__(self, window, batch, group):
        self.window = window
        self.batch = batch
        self.group = group
        self.create_background()
        self.enviornment_objs = self.create_enviornment()


    def create_enviornment(self):
        goalbox = gameobjects.box(400, 400, 100, 10, self.window, self.batch, self.group)

        return goalbox


    def create_enviornment_bounds(self):
        ''' Create bounding boxes for enviornment background '''
        objs = []

        hole = CollisionObject(25, 420, 60, 50, self.window.width, self.window.height)
        top_group1 = CollisionObject(155, 440, 180, 135, self.window.width, self.window.height)
        top_group1_1 = CollisionObject(185, 410, 70, 45, self.window.width, self.window.height)
        top_group2 = CollisionObject(345, 490, 100, 85, self.window.width, self.window.height)
        top_group3 = CollisionObject(415, 450, 150, 85, self.window.width, self.window.height)
        top_group4 = CollisionObject(575, 490, 60, 85, self.window.width, self.window.height)
        top_group5 = CollisionObject(635, 440, 60, 85, self.window.width, self.window.height)
        right_group1 = CollisionObject(700, 50, 60, 385, self.window.width, self.window.height)
        water1 = CollisionObject(0, 240, 535, 75, self.window.width, self.window.height)
        water2 = CollisionObject(460, 100, 75, 145, self.window.width, self.window.height)
        water3 = CollisionObject(460, 0, 75, 35, self.window.width, self.window.height)
        
        objs.append(hole)
        objs.append(top_group1)
        objs.append(top_group1_1)
        objs.append(top_group2)
        objs.append(top_group3)
        objs.append(top_group4)
        objs.append(top_group5)
        objs.append(right_group1)
        objs.append(water1)
        objs.append(water2)
        objs.append(water3)


        return objs

    def create_background(self):
        ''' Create sprite for the background image '''
        self.rectangle = pyglet.shapes.Rectangle(0, 0,
                                            self.window.width, self.window.height,
                                            color=(0, 100, 25), 
                                            batch=self.batch, group=self.group)


    def handle_enviornment_collisions(self, hero):
        """ Detect and handle collisions with object and enviornment"""
        for obj in self.enviornment_objs:
            if obj.collides_with(hero.hit_box):
                if hero.moving:
                    if hero.facing == Facing.UP:
                        hero.hit_box.y -= hero.speed
                    elif hero.facing == Facing.DOWN:
                        hero.hit_box.y += hero.speed
                    elif hero.facing == Facing.LEFT:
                        hero.hit_box.x += hero.speed
                    elif hero.facing == Facing.RIGHT:
                        hero.hit_box.x -= hero.speed
                    else:
                        print("Unhandled Collision!")

    def draw_env_bounds(self):
        ''' Show the environment bounds '''
        for obj in self.enviornment_objs:
            rectangle = pyglet.shapes.Rectangle(obj.x, obj.y, obj.width, obj.height, color=(0, 0, 255))
            rectangle.opacity = 150
            rectangle.draw()

    def update(self, dt, hero):
        self.handle_enviornment_collisions(hero)

