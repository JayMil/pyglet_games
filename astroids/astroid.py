import pyglet

# local imports
import resources
import load

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=580, batch=main_batch)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width//2, y=580,
                                anchor_x='center', batch=main_batch)

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300, batch=main_batch)

asteroids = load.asteroids(3, player_ship.position, batch=main_batch)


@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()


