import pyglet
from pyglet.window import key
import math
import resources

import menu
import game

# Show bounding boxes
DEBUG = False

class GameController:
    ''' Main Game Object to handle overall game logic '''
    def __init__(self, window):
        self.window = window
        self.active_env = None
        self.menu_env = menu.MainMenu(self.start_game, self.exit, window)
        self.level_env = game.Level(self.start_menu, self.window)
        self.start_menu()

    def start_menu(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.menu_env
        self.window.push_handlers(self.active_env)

    def start_game(self):
        self.window.remove_handlers(self.active_env)
        self.active_env = self.level_env
        self.window.push_handlers(self.active_env)

    def exit(self):
        pyglet.app.exit()

    def draw(self):
        ''' Main draw method '''
        self.window.clear()
        if self.active_env:
            self.active_env.draw()

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

    def update(self, dt):
        if self.active_env:
            self.active_env.update(dt)

    
# 21 x 15
window = pyglet.window.Window(1080, 768)
#window = pyglet.window.Window(768, 576)
gameController = GameController(window)
pyglet.clock.schedule_interval(gameController.update, 1/120.0)

@window.event
def on_draw():
    gameController.draw()

pyglet.app.run()


