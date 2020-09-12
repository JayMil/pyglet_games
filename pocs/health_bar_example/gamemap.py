import pyglet

import gameobjects
from gameobjects import CollisionObject
from gameobjects import HealthPotion

class Map():
    def __init__(self, window, batch, group, group2):
        self.window = window
        self.batch = batch
        self.group = group
        self.group2 = group2
        self.create_background()
        self.create_items()
        # self.enviornment_objs = self.create_enviornment()
        self.enviornment_objs = []
        self.items = self.create_items()


    def create_enviornment(self):
        goalbox = gameobjects.box(400, 400, 100, 10, self.window, self.batch, self.group)

        return goalbox

    def create_items(self):

        items = []
        health_potion1 = gameobjects.HealthPotion(start_pos=(320, 320), window_width=32, window_height=32, batch=self.batch, group=self.group2)
        health_potion2 = gameobjects.HealthPotion(start_pos=(192, 512), window_width=32, window_height=32, batch=self.batch, group=self.group2)
        health_potion3 = gameobjects.HealthPotion(start_pos=(480, 288), window_width=32, window_height=32, batch=self.batch, group=self.group2)
        health_potion4 = gameobjects.HealthPotion(start_pos=(288, 352), window_width=32, window_height=32, batch=self.batch, group=self.group2)           
        health_potion5 = gameobjects.HealthPotion(start_pos=(544, 512), window_width=32, window_height=32, batch=self.batch, group=self.group2)
        items.append(health_potion1)
        items.append(health_potion2)
        items.append(health_potion3)
        items.append(health_potion4)
        items.append(health_potion5)

        return items

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
                if hero.is_moving_up():
                    hero.item
                elif hero.is_moving_down():
                    hero.hit_box.y += hero.speed
                elif hero.is_moving_left():
                    hero.hit_box.x += hero.speed
                elif hero.is_moving_right():
                    hero.hit_box.x -= hero.speed
                else:
                    print("Unhandled Collision!")

    def handle_item_collisions(self, hero):
        """ Detect and handle collisions with object and items"""
        items_to_delete = []
    
        for obj in self.items:
            if obj.collides_with(hero.hit_box):
                hero.change_potion_count(1)
                items_to_delete.append(obj)

        if items_to_delete != []:
            for obj in items_to_delete:
                self.items.remove(obj)
           



    def draw_env_bounds(self):
        ''' Show the environment bounds '''
        for obj in self.enviornment_objs:
            rectangle = pyglet.shapes.Rectangle(obj.x, obj.y, obj.width, obj.height, color=(0, 0, 255))
            rectangle.opacity = 150
            rectangle.draw()

    def update(self, dt, hero):
        self.handle_item_collisions(hero)

