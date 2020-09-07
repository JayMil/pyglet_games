import pyglet

class CollisionObject(object):
    ''' Rectangular collision object
        Used for calculating collisions between objects
    '''
    def __init__(self, x, y, width, height, window_width, window_height, color=(100, 100, 100)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height
        self.position = (self.x, self.y)
        self.color = color

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

class EnviornmentRect(pyglet.shapes.Rectangle):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window

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


class PhysicalSpriteObject(pyglet.sprite.Sprite):
    ''' A physical sprite object '''
    def __init__(self, window_width, window_height, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window_width = window_width
        self.window_height = window_height
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.hit_box = CollisionObject(self.x, self.y, self.width, self.height, self.window_width, self.window_height)

class GameEnviornment():
    ''' A game enviornment - menu screen - level - etc.. '''
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
    box_bottom = EnviornmentRect(window, x, y,
                                    length, thickness,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_left = EnviornmentRect(window, x, y,
                                    thickness, length,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_right = EnviornmentRect(window, x+length, y,
                                    thickness, length,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box_top = EnviornmentRect(window, x, y+length,
                                    length+thickness, thickness,
                                    color=(0, 25, 100), 
                                    batch=batch, group=group)

    box.append(box_bottom)
    box.append(box_left)
    box.append(box_right)
    box.append(box_top)

    return box

