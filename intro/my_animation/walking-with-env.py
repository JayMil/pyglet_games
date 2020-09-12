import pyglet
from pyglet.window import key
import math
import resources
import random

# Show bounding boxes
DEBUG = False

class Game:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):

        self.window = window

        self.main_batch = pyglet.graphics.Batch()

        self.menu_batch = pyglet.graphics.Batch()

        self.screen = "level"
        self.create_labels()

        self.menu_option = 0
        self.create_background()
        self.won = False


        self.win_sound = pyglet.resource.media('win_sound.wav', streaming=False)
        self.key_pickup_sound = pyglet.resource.media('key_pickup.wav', streaming=False)
        self.switch_down_sound = pyglet.resource.media('switch_down.wav', streaming=False)
        self.switch_up_sound = pyglet.resource.media('switch_up.wav', streaming=False)


        self.menu_option0 = pyglet.text.Label('Start Game',
                                    font_size=24, color=(255, 255, 0, 255),
                                    x=self.window.width//2, y=self.window.height-90, anchor_x="center", batch=self.menu_batch)
        self.menu_option1 = pyglet.text.Label('Quit Game',
                            font_size=24,
                            x=self.window.width//2, y=self.window.height-136, anchor_x="center", batch=self.menu_batch)
 

        self.hero = Hero(start_pos=(384, 400),
                        window_width=self.window.width, window_height=self.window.height,
                        batch=self.main_batch)

        self.enemy = Enemy(start_pos=(110, 240), window_width=32, window_height=32, batch=self.main_batch)
                        
        self.window.push_handlers(self)
        self.window.push_handlers(self.hero)

        self.enviornment_objs = self.create_enviornment_bounds()
        self.create_items()

        self.key_unlocked = False
        self.key_picked_up = False

        self.collision_floor = CollisionObjectGlitched(0, 0, 786, 300, self.window.width, self.window.height)


    def create_enviornment_bounds(self):
        ''' Create bounding boxes for enviornment background '''
        objs = []

        # co1 = CollisionObject(0, 208, 128, 16, self.window.width, self.window.height)
        # co2 = CollisionObject(112, 144, 16, 64, self.window.width, self.window.height)
        # co3 = CollisionObject(112, 0, 16, 96, self.window.width, self.window.height)


        # objs.append(co1)
        # objs.append(co2)
        # objs.append(co3)
        

        return objs

    def create_items(self):
        ''' Create items in game '''

        # self.switch = Switch(start_pos=(512, self.window.height-224), window_width=32, window_height=32,
        #                 batch=self.main_batch)  
        # self.box = Box(start_pos=(288, self.window.height-224), window_width=32, window_height=32,
        #                 batch=self.main_batch)
        # self.key = Key(start_pos=(480, 60), window_width=32, window_height=32)
 
        # self.key_door = Key_door(start_pos=(112, 96), window_width=16, window_height=48,
        #                 batch=self.main_batch)
        # self.win_tile = Win_tile(start_pos=(32, 64), window_width=32, window_height=32,
        #                 batch=self.main_batch)


    def create_background(self):
        ''' Create sprite for the background image '''
        self.bg = pyglet.sprite.Sprite(img=resources.background_image, 
                                batch=self.main_batch,
                                x=self.window.width//2, y=self.window.height//2)
                     

    def create_labels(self):
        # labels not showing...
        self.title = pyglet.text.Label('Example',
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
        if self.collision_floor.collides_with(self.hero.hit_box):

            glitch_chance = math.floor((self.hero.y/5)) + 20

            if random.randint(0,glitch_chance) > glitch_chance - 2:
                number1 = -32 + math.floor((self.hero.y/10))
                number2 = 32 - math.floor((self.hero.y/10))
                self.hero.y += random.randint(number1 , number2)
                if random.randint(0,2) > 1:
                    self.hero.x += random.randint(number1 , number2)

        # if self.key_door.collides_with(self.hero.hit_box):
        #     if self.key_picked_up == False:
        #         if self.hero.is_moving_up():
        #             self.hero.hit_box.y -= self.hero.speed
        #         elif self.hero.is_moving_down():
        #             self.hero.hit_box.y += self.hero.speed
        #         elif self.hero.is_moving_left():
        #             self.hero.hit_box.x += self.hero.speed
        #         elif self.hero.is_moving_right():
        #             self.hero.hit_box.x -= self.hero.speed
        #         else:
        #             print("Unhandled Collision!")
        #     else:
        #         self.key_door.x = 5000
        #         self.key_door.y = 5000
        

        # if self.box.collides_with(self.hero.hit_box):
        #     if self.hero.is_moving_up():
        #         self.hero.hit_box.y -= self.hero.speed * 0.8
        #         self.box.y += self.hero.speed * 0.2
        #     elif self.hero.is_moving_down():
        #         self.hero.hit_box.y += self.hero.speed * 0.8
        #         self.box.y -= self.hero.speed * 0.2
        #     elif self.hero.is_moving_left():
        #         self.hero.hit_box.x += self.hero.speed * 0.8
        #         self.box.x -= self.hero.speed * 0.2
        #     elif self.hero.is_moving_right():
        #         self.hero.hit_box.x -= self.hero.speed * 0.8
        #         self.box.x += self.hero.speed * 0.2
        #     else:
        #         print("Unhandled Collision!")    

        # if self.box.collides_with(self.switch):
        #     if self.key_unlocked == False:
        #         self.key_unlocked = True 
        #         self.switch_down_sound.play()
        # else:
        #     if self.key_unlocked == True:
        #         self.key_unlocked = False 
        #         self.switch_up_sound.play()

        # if self.key.collides_with(self.hero.hit_box) and self.key_unlocked == True:
        #     if self.key_picked_up == False:
        #         self.key_picked_up = True
        #         self.key_pickup_sound.play()
        #         self.title.text = "You got the key!"

        # if self.win_tile.collides_with(self.hero.hit_box):
        #     if self.won == False:
        #         self.won = True
        #         self.win_sound.play()
        #         self.title.text = "You Win!"


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
        if DEBUG:
            self.draw_env_bounds()



    def update(self, dt):
        self.hero.update(dt)
        self.enemy.update(dt)
        self.handle_enviornment_collisions()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        if self.screen == "menu":
            if symbol == key.ENTER:
                if self.menu_option == 0:
                    self.screen = "level"
                elif self.menu_option == 1:
                    self.window.close()
            elif symbol == key.DOWN:
                if self.menu_option == 0:
                    self.menu_option = 1
                    self.menu_option0.color = (255, 255, 255, 255)
                    self.menu_option1.color = (255, 255, 0, 255)
            elif symbol == key.UP:
                if self.menu_option == 1:
                    self.menu_option = 0
                    self.menu_option0.color = (255, 255, 0, 255)
                    self.menu_option1.color = (255, 255, 255, 255)


        

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

class CollisionObjectGlitched(object):
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


class Box(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.box, x=start_pos[0], y=start_pos[1], *args, **kwargs)

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

    def update(self, dt):
        pass


class Win_tile(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.win_tile, x=start_pos[0], y=start_pos[1], *args, **kwargs)

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

    def update(self, dt):
        pass


class Key_door(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.key_door, x=start_pos[0], y=start_pos[1], *args, **kwargs)

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

    def update(self, dt):
        pass


class Switch(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.switch, x=start_pos[0], y=start_pos[1], *args, **kwargs)

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

    def update(self, dt):
        pass

class Key(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.key, x=start_pos[0], y=start_pos[1], *args, **kwargs)

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

    def update(self, dt):
        pass

class Enemy(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.box, x=start_pos[0], y=start_pos[1], *args, **kwargs)

        self.moving_forward = True
        self.glitch_time = 400
        self.glitch_time_left = 4

    def update(self, dt):
        if self.glitch_time > 0:
            if self.moving_forward == True:
                if self.x < 400:
                    self.x+=2
                else: 
                    self.moving_forward = False
            else:
                if self.x > 100:
                    self.x-=2
                else:
                    self.moving_forward = True
            self.glitch_time -= 1
            if self.glitch_time < 1:
                if random.randint(0,2) < 1:
                    self.x += random.randint(10,50)
                    self.y -= random.randint(10,50)
                else:
                    self.x -= random.randint(10,50)
                    self.y += random.randint(10,50)
        else:
            if self.glitch_time_left < 0:
                self.glitch_time_left -= 1
            else:
                self.glitch_time_left = 4
                self.y = 240
                self.x = 120
                self.glitch_time = random.randint(200,400)

class Enemy2(PhysicalSpriteObject):
    ''' Power Up Sprite Class '''
    def __init__(self, start_pos, *args, **kwargs):
        super().__init__(img=resources.box, x=start_pos[0], y=start_pos[1], *args, **kwargs)

        self.moving_forward = True
        self.glitch_time = 400
        self.glitch_time_left = 4

    def update(self, dt):
        if self.glitch_time > 0:
            if self.moving_forward == True:
                if self.x < 400:
                    self.x+=2
                else: 
                    self.moving_forward = False
            else:
                if self.x > 100:
                    self.x-=2
                else:
                    self.moving_forward = True
            self.glitch_time -= 1
            if self.glitch_time < 1:
                if random.randint(0,2) < 1:
                    self.x += random.randint(10,50)
                    self.y -= random.randint(10,50)
                else:
                    self.x -= random.randint(10,50)
                    self.y += random.randint(10,50)
        else:
            if self.glitch_time_left < 0:
                self.glitch_time_left -= 1
            else:
                self.glitch_time_left = 4
                self.y = 320
                self.x = 120
                self.glitch_time = random.randint(200,400)        

                    
                    

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
window = pyglet.window.Window(768, 512)
game = Game(window)
pyglet.clock.schedule_interval(game.update, 1/120.0)

@window.event
def on_draw():
    game.draw()

pyglet.app.run()



