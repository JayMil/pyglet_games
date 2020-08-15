import pyglet
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

game_window = pyglet.window.Window(800, 600)

player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")

#score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)
score_label = pyglet.text.Label(text="Score: 0", x=10, y=580)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=game_window.width//2, y=580,
                                anchor_x='center')

def main():
    center_image(player_image)
    center_image(bullet_image)
    center_image(asteroid_image)



def center_image(image):
    """ Sets an image's anchor point to its center """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()

if __name__ == '__main__':
    pyglet.app.run()
    main()
