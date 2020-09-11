import pyglet
from pyglet.window import key

import gamemap
import gameobjects
from gameobjects import GameEnviornment
from gameobjects import CollisionObject
from gameobjects import EnviornmentRect
from hero import Hero


class Level(GameEnviornment):
    def __init__(self, on_exit, window):
        super().__init__("Level", window)

        self.on_exit = on_exit

        self.backroung_layer = pyglet.graphics.OrderedGroup(0)
        self.background_overlay_layer = pyglet.graphics.OrderedGroup(1)
        self.foreground_underlay_layer = pyglet.graphics.OrderedGroup(2)
        self.foreground_layer = pyglet.graphics.OrderedGroup(3)
        self.foreground_overlay_layer = pyglet.graphics.OrderedGroup(4)
        self.fg_overlay_group = pyglet.graphics.OrderedGroup(2)

        self.create_labels()
        self.hero = Hero(start_pos=(40, self.window.height-200),
                        window=self.window, batch=self.batch, 
                        underlay_group=self.foreground_underlay_layer, 
                        overlay_group=self.foreground_overlay_layer,
                        group=self.foreground_layer)

        self.window.push_handlers(self.hero)
        self.map = gamemap.Map(window, self.batch, self.backroung_layer)

    def create_labels(self):
        ''' Create helper lables '''
        self.title = pyglet.text.Label('Top - View Proof of Concept',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=self.window.height-30,
                                    anchor_x='center', batch=self.batch,
                                    group=self.foreground_layer)


        pyglet.text.Label('Move with direction keys',
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-60,
                                    batch=self.batch, group=self.foreground_layer)

        pyglet.text.Label("Move fast with 'f' key",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-90,
                                    batch=self.batch, group=self.foreground_layer)

        pyglet.text.Label("Press 'q' to quit",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-120,
                                    batch=self.batch, group=self.foreground_layer)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            self.on_exit()

    def update(self, dt):
        self.hero.update(dt)
        self.map.update(dt, self.hero)

    def draw(self):
        super().draw();

        '''
        # DEBUG
        if DEBUG:
            pass
            #self.draw_env_bounds()
            # draw player pos dot
            #height = self.hero.height-14
            #rectangle = pyglet.shapes.Rectangle(self.hero.hit_box.x, self.hero.hit_box.y, self.hero.width, height, color=(255, 0, 0))
            #rectangle.opacity = 125
            #rectangle.draw()
        '''

