import pyglet
from pyglet.window import key
import resources


class Game:
    def __init__(self, window):
        self.window = window

        self.main_batch = pyglet.graphics.Batch()

        self.create_background()
        self.create_labels()
        self.hero = Hero(start_pos=(40, self.window.height-100), batch=self.main_batch)
        self.window.push_handlers(self)
        self.window.push_handlers(self.hero)

    def create_background(self):
        self.bg = pyglet.sprite.Sprite(img=resources.background_image, 
                                batch=self.main_batch,
                                x=self.window.width//2, y=self.window.height//2)

    def create_labels(self):
        pyglet.text.Label('Walking Example',
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

    def draw(self):
        self.window.clear()
        self.bg.draw()
        self.main_batch.draw()

    def update(self, dt):
        self.hero.update(dt)

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


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False

        self.new_objects = []

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()

    def check_bounds(self):
        min_x = -self.width / 2
        min_y = -self.height / 2
        max_x = 800 + self.width / 2
        max_y = 600 + self.height / 2

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object):
        collision_distance = self.width/2 + other_object.width/2
        actual_distance = util.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)


    def handle_collision_with(self, other_object):
        if other_object.__class__ == self.__class__:
            self.dead = False
        else:
            self.dead = True

class Hero(PhysicalObject):
    def __init__(self, start_pos=(20, 200), hero_images=HeroImages(), *args, **kwargs):
        super().__init__(img=hero_images.face_down, x=start_pos[0], y=start_pos[1], *args, **kwargs)
        self.hero_images = hero_images
        
        self.speed = 2

        self.character_keys = dict(up=False, down=False, 
                                    left=False, right=False,
                                    fast=False)

    def update(self, dt):
        if self.character_keys['fast']:
            self.speed = 4
        else:
            self.speed = 2

        if self.character_keys['up']:
            if self.image != self.hero_images.walk_up:
                self.image = self.hero_images.walk_up
            self.y += self.speed
        elif self.character_keys['down']:
            if self.image != self.hero_images.walk_down:
                self.image = self.hero_images.walk_down
            self.y -= self.speed
        elif self.character_keys['left']:
            if self.image != self.hero_images.walk_left:
                self.image = self.hero_images.walk_left
            self.x -= self.speed
        elif self.character_keys['right']:
            if self.image != self.hero_images.walk_right:
                self.image = self.hero_images.walk_right
            self.x += self.speed
        else:
            if self.image == self.hero_images.walk_up:
                self.image = self.hero_images.face_up
            elif self.image == self.hero_images.walk_down:
                self.image = self.hero_images.face_down
            elif self.image == self.hero_images.walk_left:
                self.image = self.hero_images.face_left
            elif self.image == self.hero_images.walk_right:
                self.image = self.hero_images.face_right

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


