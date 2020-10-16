import pyglet
import math
import resources
from pyglet import shapes

class CollisionObject(object):
    ''' Rectangular collision object
        Used for calculating collisions between objects
    '''
    def __init__(self, x, y, width, height, window_width, window_height, batch, group, color = (0, 0, 255)):
        self.x = x - 6 
        self.y = y
        self.batch = batch
        self.group = group
        self.width = 20
        self.height = 12
        self.window_width = window_width
        self.window_height = window_height
        self.position = (self.x, self.y)
        self.color = color
        self.box = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, self.batch, self.group)
    
    def update(self):
        self.box.x = self.x
        self.box.y = self.y

    def collides_with(self, other_object):
        # rectangle collision
        x1 = self.x
        y1 = self.y
        x2 = other_object.x
        y2 = other_object.y

        if (x1 < x2 + other_object.width and
           x1 + self.width > x2 and
           y1 < y2 + other_object.height and
           y1 + self.height > y2):
            return True
        else:
            return False




class EnvironmentRect(pyglet.shapes.Rectangle):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window




class PhysicalSpriteObject(pyglet.sprite.Sprite):
    ''' A physical sprite object '''
    def __init__(self, window_width, window_height, batch2, group2, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window_width = window_width
        self.window_height = window_height
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.hit_box = CollisionObject(self.x, self.y, self.width, self.height, self.window_width, self.window_height, batch=batch2, group=group2)


class HealthPotion(PhysicalSpriteObject):
    ''' Potion Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.health_potion, x=start_pos[0], y=start_pos[1], *args, **kwargs)

    def collides_with(self, other_object):
        # rectangle collision
        x1 = self.x
        y1 = self.y
        x2 = other_object.x
        y2 = other_object.y

        if (x1 < x2 + other_object.width and
           x1 + self.width > x2 and
           y1 < y2 + other_object.height and
           y1 + self.height > y2):
            return True
        else:
            return False


class GameEnvironment():
    ''' A game environment - menu screen - level - etc.. '''
    def __init__(self, name, window):
        self.name = name
        self.window = window
        self.batch = pyglet.graphics.Batch()

    def draw(self):
        self.batch.draw()

    def update(self):
        pass

def box(x, y, length, thickness, window, batch, group):        
    box = []
    box_bottom = EnvironmentRect(window, x, y,
                                    length, thickness,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_left = EnvironmentRect(window, x, y,
                                    thickness, length,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_right = EnvironmentRect(window, x+length, y,
                                    thickness, length,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_top = EnvironmentRect(window, x, y+length,
                                    length+thickness, thickness,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box.append(box_bottom)
    box.append(box_left)
    box.append(box_right)
    box.append(box_top)

    return box

