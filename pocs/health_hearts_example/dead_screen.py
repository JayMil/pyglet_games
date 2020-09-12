import pyglet
from pyglet.window import key

from gameobjects import GameEnviornment

START_GAME = 0
EXIT = 1
OPTIONS = 2

class DeadScreen(GameEnviornment):
    def __init__(self, window):
        super().__init__("Dead!", window)

        # functions to call when finished
        # self.on_start_game = on_start_game
        # self.on_exit = on_exit

        # self.active_item = START_GAME
        # self.finished = False
        self.start_game = pyglet.text.Label('You are dead!',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=(self.window.height//2)+20,
                                    anchor_x='center', anchor_y='center',
                                    batch=self.batch)

        # self.exit = pyglet.text.Label('Exit',
        #                             font_name='Times New Roman',
        #                             font_size=24,
        #                             x=self.window.width//2, y=self.window.height//2-20,
        #                             anchor_x='center', anchor_y='center',
        #                             batch=self.batch)

    def update(self, dt):
        pass


    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass




