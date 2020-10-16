import pyglet

import gameobjects
from gameobjects import CollisionObject
from gameobjects import EnvironmentRect
import math

class Map():
    def __init__(self, window, batch, group, group2):
        self.window = window
        self.batch = batch
        self.group = group
        self.group2 = group2
        self.create_background()
        self.tile_size = 32
        self.screen_height = 768
        self.environment_matrix = self.create_environment_bounds()
        
        


    def create_environment(self):
        goalbox = gameobjects.box(400, 400, 100, 10, self.window, self.batch, self.group)

        return goalbox

    def create_environment_bounds(self):
        ''' Create environment bounds'''
        matrix = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]

        self.color = (100, 100, 100)
        self.border_boxs = []

        for y in range(0, len(matrix)):     
            for x in range(0, 30):
                if (matrix[y][x] == 1):
                    self.border_boxs.append(EnvironmentRect(self.window, x * self.tile_size, self.screen_height - 32 - y * self.tile_size, self.tile_size, self.tile_size, self.color, self.batch, self.group2))


        return matrix

    def create_background(self):
        ''' Create sprite for the background image '''
        self.rectangle = pyglet.shapes.Rectangle(0, 0,
                                            self.window.width, self.window.height,
                                            color=(0, 100, 25), 
                                            batch=self.batch, group=self.group)


    def handle_environment_collisions(self, hero):
        """ Detect and handle collisions with object and environment"""
        if hero.is_moving_up():
            matrix_y = math.floor((self.screen_height - hero.hit_box.y - hero.hit_box.height)/self.tile_size)
            matrix_x1 = math.floor(hero.hit_box.x/self.tile_size)
            matrix_x2 = math.floor((hero.hit_box.x + hero.hit_box.width)/self.tile_size)
            if (self.environment_matrix[matrix_y][matrix_x1] == 1):
                hero.hit_box.y -= hero.speed
            elif (self.environment_matrix[matrix_y][matrix_x2] == 1):
                hero.hit_box.y -= hero.speed
        elif hero.is_moving_down():
            matrix_y = math.floor((self.screen_height - hero.hit_box.y)/self.tile_size)
            matrix_x1 = math.floor(hero.hit_box.x/self.tile_size)
            matrix_x2 = math.floor((hero.hit_box.x + hero.hit_box.width)/self.tile_size)
            if (self.environment_matrix[matrix_y][matrix_x1] == 1):
                hero.hit_box.y += hero.speed
            elif (self.environment_matrix[matrix_y][matrix_x2] == 1):
                hero.hit_box.y += hero.speed
        elif hero.is_moving_left():
            matrix_x = math.floor(hero.hit_box.x/self.tile_size)
            matrix_y1 = math.floor((self.screen_height - hero.hit_box.y - hero.hit_box.height)/self.tile_size)
            matrix_y2 = math.floor((self.screen_height - hero.hit_box.y)/self.tile_size)
            if (self.environment_matrix[matrix_y1][matrix_x] == 1):
                hero.hit_box.x += hero.speed
            elif (self.environment_matrix[matrix_y2][matrix_x] == 1):
                hero.hit_box.x += hero.speed
        elif hero.is_moving_right():
            matrix_x = math.floor((hero.hit_box.x + hero.hit_box.width)/self.tile_size)
            matrix_y1 = math.floor((self.screen_height - hero.hit_box.y - hero.hit_box.height)/self.tile_size)
            matrix_y2 = math.floor((self.screen_height - hero.hit_box.y)/self.tile_size)
            if (self.environment_matrix[matrix_y1][matrix_x] == 1):
                hero.hit_box.x -= hero.speed
            elif (self.environment_matrix[matrix_y2][matrix_x] == 1):
                hero.hit_box.x -= hero.speed


        # if hero.is_moving_up():
        #     matrix_y = math.floor((self.screen_height - hero.hit_box.y + hero.hit_box.height)/self.tile_size)
        #     matrix_x = math.floor((self.screen_height - hero.hit_box.x + 16)/self.tile_size)
        #     print(str(matrix_x) + " " + str(matrix_y))
        #     if (self.environment_matrix[matrix_y][matrix_x] == 1):
        #         hero.hit_box.y -= hero.speed
            
        # elif hero.is_moving_down():
        #     matrix_y = math.floor((self.screen_height - hero.hit_box.y)/self.tile_size)
        #     matrix_x = math.floor((self.screen_height - hero.hit_box.x + 16)/self.tile_size)
        #     print(str(matrix_x) + " " + str(matrix_y))
        #     if (self.environment_matrix[matrix_y][matrix_x] == 1):
        #         hero.hit_box.y += hero.speed
        # elif hero.is_moving_left():
        #     pass
        #     # hero.hit_box.x += hero.speed
        # elif hero.is_moving_right():
        #     pass
        #     # hero.hit_box.x -= hero.speed

    def draw_env_bounds(self):
        ''' Show the environment bounds '''
        for obj in self.environment_objs:
            rectangle = pyglet.shapes.Rectangle(obj.x, obj.y, obj.width, obj.height, color=(0, 0, 255))
            rectangle.opacity = 150
            rectangle.draw()

    def update(self, dt, hero):
        self.handle_environment_collisions(hero)

