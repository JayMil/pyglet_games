import pyglet

# local imports
import resources
import load
import player

game_window = pyglet.window.Window(800, 600)


class Game:
    def __init__(self, gwindow):
        self.game_window = gwindow
        self.main_batch = pyglet.graphics.Batch()

        self.score = 0
        self.score_label = pyglet.text.Label(text="Score: 0", x=10, y=580, batch=self.main_batch)
        self.level_label = pyglet.text.Label(text="Asteroids",
                                        x=self.game_window.width//2, y=580,
                                        anchor_x='center', batch=self.main_batch)
        self.debug_label = pyglet.text.Label(text="Debug", x=10, y=560, batch=self.main_batch)

        self.player_ship = self.__create_new_player_ship()

        self.asteroids = load.asteroids(3, self.player_ship.position, batch=self.main_batch)

        self.player_lives = load.player_lives(3, batch=self.main_batch)
        self.game_objects = [self.player_ship] + self.asteroids

        print(len(self.player_lives))

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
                print("Game Over")


    def __update_game_objects(self, dt):
        """ Call update on each game object and return list of child objects """
        # update game objects
        new_objects = []
        for obj in self.game_objects:
            obj.update(dt)
            new_objects.extend(obj.new_objects)
            obj.new_objects = []

        return new_objects

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



    def update(self, dt):
        """ Update Game Elements """
        self.debug_label.text=f"Game Objects {len(self.game_objects)}"
        self.score_label.text=f"Score {self.score}"
        to_add = self.__update_game_objects(dt)
        self.__remove_dead_game_objects()
        self.__handle_game_object_collisions()
        self.game_objects.extend(to_add)
        self.__check_player_death()


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

