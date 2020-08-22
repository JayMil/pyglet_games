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


class Hero:
    def __init__(self, start_pos=(20, 200), batch=None):
        self.character_walk_up_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_up, duration=0.1,loop=True)
        self.character_walk_down_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_down, duration=0.1,loop=True)
        self.character_walk_left_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_left, duration=0.1,loop=True)
        self.character_walk_right_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_right, duration=0.1,loop=True)
        self.character = pyglet.sprite.Sprite(img=self.character_walk_down_ani, batch=batch, x=start_pos[0], y=start_pos[1])

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
            if self.character.image != self.character_walk_up_ani:
                self.character.image = self.character_walk_up_ani
            self.character.y += self.speed
        elif self.character_keys['down']:
            if self.character.image != self.character_walk_down_ani:
                self.character.image = self.character_walk_down_ani
            self.character.y -= self.speed
        elif self.character_keys['left']:
            if self.character.image != self.character_walk_left_ani:
                self.character.image = self.character_walk_left_ani
            self.character.x -= self.speed
        elif self.character_keys['right']:
            if self.character.image != self.character_walk_right_ani:
                self.character.image = self.character_walk_right_ani
            self.character.x += self.speed
        else:
            if self.character.image == self.character_walk_up_ani:
                self.character.image = resources.character_seq_face_up
            elif self.character.image == self.character_walk_down_ani:
                self.character.image = resources.character_seq_face_down
            elif self.character.image == self.character_walk_left_ani:
                self.character.image = resources.character_seq_face_left
            elif self.character.image == self.character_walk_right_ani:
                self.character.image = resources.character_seq_face_right

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


