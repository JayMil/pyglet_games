import pyglet
from pyglet.window import key
import math
import resources

import menu
import game
import dead_screen

# Show bounding boxes
DEBUG = False

class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window
        self.active_env = None
        self.menu_env = menu.MainMenu(self.start_game, self.exit, window)
        self.level_env = game.Level(self.start_menu, self.start_dead_screen, self.window)
        self.dead_screen_env = dead_screen.DeadScreen(self.window)
        self.start_menu()

    def start_menu(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.menu_env
        self.window.push_handlers(self.active_env)

    def start_game(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.level_env
        self.window.push_handlers(self.active_env)

    def start_dead_screen(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.dead_screen_env
        self.window.push_handlers(self.active_env)        

    def exit(self):
        pyglet.app.exit()

    def draw(self):
        ''' Main draw method '''
        self.window.clear()
        if self.active_env:
            self.active_env.draw()

    def update(self, dt):
        if self.active_env:
            self.active_env.update(dt)

    
# 21 x 15
window = pyglet.window.Window(1080, 768)
window.set_location(400, 50)
gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1/120.0)

@window.event
def on_draw():
    gameController.draw()

pyglet.app.run()


