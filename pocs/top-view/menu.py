import pyglet
from pyglet.window import key

from gameobjects import GameEnviornment

START_GAME = 0
EXIT = 1
OPTIONS = 2

class MainMenu(GameEnviornment):
    def __init__(self, on_start_game, on_exit, window):
        super().__init__(window)

        # functions to call when finished
        self.on_start_game = on_start_game
        self.on_exit = on_exit

        self.active_item = START_GAME
        self.finished = False
        self.start_game = pyglet.text.Label('Start Game',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=(self.window.height//2)+20,
                                    anchor_x='center', anchor_y='center',
                                    batch=self.batch)

        self.exit = pyglet.text.Label('Exit',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=self.window.height//2-20,
                                    anchor_x='center', anchor_y='center',
                                    batch=self.batch)

    def update(self, dt):
        if (self.active_item == START_GAME):
            self.start_game.bold = True
            self.exit.bold = False
        else:
            self.start_game.bold = False
            self.exit.bold = True

        if (self.finished):
            if self.active_item == START_GAME:
                self.on_start_game()
            else:
                self.on_exit()


    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.active_item += 1
        elif symbol == key.DOWN:
            self.active_item -= 1
        elif symbol == key.ENTER:
            self.finished = True

        if self.active_item >= OPTIONS:
            self.active_item = 0
        elif self.active_item < 0:
            self.active_item  = 1

    def on_key_release(self, symbol, modifiers):
        pass




