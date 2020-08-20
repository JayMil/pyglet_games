import pyglet
from pyglet.window import key

# local imports
import resources
import load
import player
import asteroid, bullet

game_window = pyglet.window.Window(800, 600)


class Game:
    def __init__(self, gwindow):
        self.game_window = gwindow
        self.game_window.push_handlers(self)
        self.main_batch = pyglet.graphics.Batch()
        self.score_label = pyglet.text.Label(text="Score: 0", x=10, y=580, batch=self.main_batch)
        self.level_label = pyglet.text.Label(text="Asteroids",
                                        x=self.game_window.width//2, y=580,
                                        anchor_x='center', batch=self.main_batch)
        self.debug_label = pyglet.text.Label(text="Debug", x=10, y=560, batch=self.main_batch)
        self.game_over_label = pyglet.text.Label(text="", 
                                                    x=self.game_window.width//2, y=self.game_window.height//2, 
                                                    anchor_x='center', anchor_y='center',
                                                    color=(255,0,0,255), font_size=40,
                                                    batch=self.main_batch)

        self.restart_label= pyglet.text.Label(text="", 
                                                    x=self.game_window.width//2, y=self.game_window.height//4, 
                                                    anchor_x='center', anchor_y='center',
                                                    color=(200,200,200,255), font_size=20,
                                                    batch=self.main_batch)


        self.game_over_score_label = pyglet.text.Label(text="", 
                                                        x=self.game_window.width//2, y=self.game_window.height//3, 
                                                        anchor_x='center', anchor_y='center',
                                                        color=(50,250,50,255), font_size=30,
                                                        batch=self.main_batch)

        self.__initialize_game()

    def __initialize_game(self):
        self.score = 0
        self.game_over = False
        self.game_over_label.text = ""
        self.restart_label.text = ""
        self.game_over_score_label.text = ""

        self.player_ship = self.__create_new_player_ship()
        self.asteroids = load.asteroids(4, self.player_ship.position, batch=self.main_batch)
        self.player_lives = load.player_lives(3, batch=self.main_batch)
        self.game_objects = [self.player_ship] + self.asteroids


    def __game_over(self):
        self.game_over = True
        # remove all game_objects
        self.__kill_game_objects()
        self.__remove_dead_game_objects()
        # Show game over label and score big
        self.game_over_label.text = "Game Over"
        self.game_over_score_label.text = f"Score: {self.score}"
        self.restart_label.text = "Press Space to Restart"

    def __create_new_player_ship(self):
        player_ship = player.Player(x=400, y=300, batch=self.main_batch)
        self.game_window.push_handlers(player_ship)
        self.game_window.push_handlers(player_ship.key_handler)
        return player_ship


    def __check_player_death(self):
        if self.player_ship.dead:
            if len(self.player_lives) > 0:
                self.player_lives.pop()
                self.player_ship = self.__create_new_player_ship()
                self.game_objects.append(self.player_ship)
            else:
                self.__game_over()

    def __check_win(self):
        if len(self.game_objects) == 1 and not self.player_ship.dead:
            self.__game_over()

    def __update_game_objects(self, dt):
        """ Call update on each game object and return list of child objects """
        # update game objects
        new_objects = []
        for obj in self.game_objects:
            obj.update(dt)
            new_objects.extend(obj.new_objects)
            obj.new_objects = []

        return new_objects

    def __kill_game_objects(self):
        for obj in self.game_objects:
            obj.dead = True

    def __remove_dead_game_objects(self):
        """ Remove dead game objects """
        for to_remove in [obj for obj in self.game_objects if obj.dead]:
            to_remove.delete()
            self.game_objects.remove(to_remove)


    def __handle_game_object_collisions(self):
        """ Detect and handle collisions """
        for i in range(len(self.game_objects)):
            for j in range(i+1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                
                if not obj_1.dead and not obj_2.dead:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

                        # if bullet collided with astroid get point
                        if ((type(obj_1) is bullet.Bullet and type(obj_2) is asteroid.Asteroid) 
                            or (type(obj_1) is asteroid.Asteroid and type(obj_2) is bullet.Bullet)):
                            self.score += 1
                        


    def __update_labels(self):
        #self.debug_label.text=f"Game Objects {len(self.game_objects)}"
        self.debug_label.text=f"Game Over Height: {self.game_over_label.height}"
        self.score_label.text=f"Score {self.score}"

    def on_key_press(self, symbol, modifiers):
        if self.game_over and symbol == key.SPACE:
            self.__initialize_game()
        
    def on_key_release(self, symbol, modifiers):
        pass


    def update(self, dt):
        """ Update Game Elements """
        self.__update_labels()

        to_add = self.__update_game_objects(dt)

        self.__remove_dead_game_objects()
        self.__handle_game_object_collisions()

        self.game_objects.extend(to_add)

        self.__check_player_death()

        self.__check_win()


    def draw(self):
        self.main_batch.draw()


@game_window.event
def on_draw():
    game_window.clear()
    game.draw()

def main():
    pass

game = Game(game_window)
pyglet.clock.schedule_interval(game.update, 1/120.0)
pyglet.app.run()

