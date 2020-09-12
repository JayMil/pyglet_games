import pyglet
from pyglet.window import key
import math
import resources

# Show bounding boxes
DEBUG = True

class Game:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window

        self.main_batch = pyglet.graphics.Batch()

        self.create_background()
        self.create_labels()
        self.hero = Hero(start_pos=(40, self.window.height-100),
                        window_width=self.window.width, window_height=self.window.height,
                        batch=self.main_batch)
        self.window.push_handlers(self)
        self.window.push_handlers(self.hero)

        self.enviornment_objs = self.create_enviornment_bounds()

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
        self.bg = pyglet.sprite.Sprite(img=resources.background_image, 
                                batch=self.main_batch,
                                x=self.window.width//2, y=self.window.height//2)

    def create_labels(self):
        # labels not showing...
        self.title = pyglet.text.Label('Walking Example',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=self.window.height-30,
                                    anchor_x='center', batch=self.main_batch)


        pyglet.text.Label('Move with direction keys',
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-60,
                                    batch=self.main_batch)

        pyglet.text.Label("Move fast with 'f' key",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-90,
                                    batch=self.main_batch)

    def handle_enviornment_collisions(self):
        """ Detect and handle collisions with hero and enviornment"""
        for obj in self.enviornment_objs:
            if obj.collides_with(self.hero.hit_box):
                if self.hero.is_moving_up():
                    self.hero.hit_box.y -= self.hero.speed
                elif self.hero.is_moving_down():
                    self.hero.hit_box.y += self.hero.speed
                elif self.hero.is_moving_left():
                    self.hero.hit_box.x += self.hero.speed
                elif self.hero.is_moving_right():
                    self.hero.hit_box.x -= self.hero.speed
                else:
                    print("Unhandled Collision!")


    def draw_env_bounds(self):
        ''' Show the environment bounds '''
        for obj in self.enviornment_objs:
            rectangle = pyglet.shapes.Rectangle(obj.x, obj.y, obj.width, obj.height, color=(0, 0, 255))
            rectangle.opacity = 150
            rectangle.draw()


    def draw(self):
        ''' Main draw method '''
        self.window.clear()
        self.bg.draw()          # batch not working for drawing background... have to manually draw
        self.title.draw()       # drawing labels is not working...
        self.main_batch.draw()



    def update(self, dt):
        self.hero.update(dt)
        self.handle_enviornment_collisions()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

class HeroImages():
    ''' Image References for Hero Sprite '''
    def __init__(self):
        self.walk_up = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_up, duration=0.1,loop=True)
        self.walk_down = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_down, duration=0.1,loop=True)
        self.walk_left = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_left, duration=0.1,loop=True)
        self.walk_right = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_right, duration=0.1,loop=True)

        self.face_up = resources.character_seq_face_up
        self.face_down = resources.character_seq_face_down
        self.face_left = resources.character_seq_face_left
        self.face_right = resources.character_seq_face_right

class CollisionObject(object):
    ''' Rectangular collision object
        Used for calculating collisions between objects
    '''
    def __init__(self, x, y, width, height, window_width, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window_width = window_width
        self.window_height = window_height
        self.position = (self.x, self.y)

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


class Hero(PhysicalSpriteObject):
    ''' Hero Sprite Class '''
    def __init__(self, start_pos=(20, 200), hero_images=HeroImages(), *args, **kwargs):
        super().__init__(img=hero_images.face_down, x=start_pos[0], y=start_pos[1], *args, **kwargs)
        self.hero_images = hero_images

        # adjust hit box height
        self.hit_box.height -= 55
        
        self.speed = 2

        self.character_keys = dict(up=False, down=False, 
                                    left=False, right=False,
                                    fast=False)

    def is_moving_up(self):
        return self.character_keys['up']

    def is_moving_down(self):
        return self.character_keys['down']

    def is_moving_left(self):
        return self.character_keys['left']

    def is_moving_right(self):
        return self.character_keys['right']

    def update(self, dt):
        if self.character_keys['fast']:
            self.speed = 4
        else:
            self.speed = 2

        if self.is_moving_up():
            if self.image != self.hero_images.walk_up:
                self.image = self.hero_images.walk_up
            self.hit_box.y += self.speed
        elif self.is_moving_down():
            if self.image != self.hero_images.walk_down:
                self.image = self.hero_images.walk_down
            self.hit_box.y -= self.speed
        elif self.is_moving_left():
            if self.image != self.hero_images.walk_left:
                self.image = self.hero_images.walk_left
            self.hit_box.x -= self.speed
        elif self.is_moving_right():
            if self.image != self.hero_images.walk_right:
                self.image = self.hero_images.walk_right
            self.hit_box.x += self.speed
        else:
            # if not moving, set to still image
            if self.image == self.hero_images.walk_up:
                self.image = self.hero_images.face_up
            elif self.image == self.hero_images.walk_down:
                self.image = self.hero_images.face_down
            elif self.image == self.hero_images.walk_left:
                self.image = self.hero_images.face_left
            elif self.image == self.hero_images.walk_right:
                self.image = self.hero_images.face_right

        # prevent going out of border
        min_x = 0
        min_y = 0
        max_x = self.window_width
        max_y = self.window_height

        if self.hit_box.x < min_x:
            self.hit_box.x = min_x
        elif (self.hit_box.x+self.hit_box.width) > max_x:
            self.hit_box.x = (max_x - self.hit_box.width)
        if self.hit_box.y < min_y:
            self.hit_box.y = min_y
        elif (self.hit_box.y+self.hit_box.height) > max_y:
            self.hit_box.y = (max_y - self.hit_box.height)

        self.x = self.hit_box.x
        self.y = self.hit_box.y

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_keys['up'] = True
        elif symbol == key.DOWN:
            self.character_keys['down'] = True
        elif symbol == key.LEFT:
            self.character_keys['left'] = True
        elif symbol == key.RIGHT:
            self.character_keys['right'] = True
        elif symbol == key.F:
            self.character_keys['fast'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_keys['up'] = False
        elif symbol == key.DOWN:
            self.character_keys['down'] = False
        elif symbol == key.LEFT:
            self.character_keys['left'] = False
        elif symbol == key.RIGHT:
            self.character_keys['right'] = False
        elif symbol == key.F:
            self.character_keys['fast'] = False


if __name__ == '__main__':
    pass
    
#window = pyglet.window.Window(1080, 768)
window = pyglet.window.Window(768, 576)
game = Game(window)
pyglet.clock.schedule_interval(game.update, 1/120.0)

@window.event
def on_draw():
    game.draw()

pyglet.app.run()


