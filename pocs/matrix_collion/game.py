import pyglet
from pyglet.window import key

import gamemap
import gameobjects
import resources
from gameobjects import GameEnvironment
from gameobjects import CollisionObject
from gameobjects import EnvironmentRect
from hero import Hero
import player_inventory
from player_inventory import PlayerInventory


class Level(GameEnvironment):
    def __init__(self, on_exit, on_dead, window):
        super().__init__("Level", window)

        self.on_exit = on_exit
        self.on_dead = on_dead

        self.bg_group = pyglet.graphics.OrderedGroup(0)
        self.item_group = pyglet.graphics.OrderedGroup(1)
        self.fg_group = pyglet.graphics.OrderedGroup(2)

        self.inventory_group1 = pyglet.graphics.OrderedGroup(3)
        self.inventory_group2 = pyglet.graphics.OrderedGroup(4)
        self.inventory_group3 = pyglet.graphics.OrderedGroup(5)

        self.create_labels()


        self.player_inventory = player_inventory.PlayerInventory(self.batch, self.inventory_group1, self.inventory_group2, self.inventory_group3)

        self.hero = Hero(start_pos=(40, self.window.height-200), update_health=self.player_inventory.update_health,
                update_potions_count=self.player_inventory.update_potions_count, batch2=self.batch, group2=self.item_group,
                window_width=self.window.width, window_height=self.window.height,
                batch=self.batch, group=self.fg_group)

        

        self.window.push_handlers(self.hero)
        self.map = gamemap.Map(window, self.batch, self.bg_group, self.item_group)

    def create_labels(self):
        ''' Create helper lables '''
        # self.title = pyglet.text.Label('Top - View Proof of Concept',
        #                             font_name='Times New Roman',
        #                             font_size=24,
        #                             x=self.window.width//2, y=self.window.height-30,
        #                             anchor_x='center', batch=self.batch,
        #                             group=self.fg_group)


        pyglet.text.Label('Move with direction keys',
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-60,
                                    batch=self.batch, group=self.fg_group)

        pyglet.text.Label("Move fast with 'f' key",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-90,
                                    batch=self.batch, group=self.fg_group)

        pyglet.text.Label("Press 'q' to quit",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-120,
                                    batch=self.batch, group=self.fg_group)
        pyglet.text.Label("Press 't' to lower health",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-150,
                                    batch=self.batch, group=self.fg_group)        
        pyglet.text.Label("Press 'p' to use potion",
                            font_name='Times New Roman',
                            font_size=16,
                            x=20, y=self.window.height-180,
                            batch=self.batch, group=self.fg_group)  

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            self.on_exit()

    def update(self, dt):
        self.hero.update(dt)
        self.map.update(dt, self.hero)
        if self.hero.health <= 0:
            self.on_dead()

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

