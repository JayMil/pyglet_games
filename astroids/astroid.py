import pyglet

# local imports
import resources
import load

game_window = pyglet.window.Window(800, 600)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=580)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width//2, y=580,
                                anchor_x='center')

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

asteroids = load.asteroids(3, player_ship.position)


@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()
    player_ship.draw()

    for asteroid in asteroids:
        asteroid.draw()




