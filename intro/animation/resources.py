import pyglet

def center_image(image):
    """ Sets an image's anchor point to its center """
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['resources']
pyglet.resource.reindex()



explosion_image = pyglet.resource.image("small/explosion.png")
explosion_seq = pyglet.image.ImageGrid(explosion_image, 4, 5)
explosion_seq1 = explosion_seq[5:9] + explosion_seq[:4]
explosion_seq2 = explosion_seq[15:] + explosion_seq[11:14]

size = "medium"

character_image = pyglet.resource.image(f"{size}/character1.png")
character_seq = pyglet.image.ImageGrid(character_image, 8, 12)
character_seq_walk_down = character_seq[84:86]
character_seq_face_down = character_seq[85]
character_seq_walk_up = character_seq[48:50]
character_seq_face_up = character_seq[49]
character_seq_walk_right = character_seq[60:62]
character_seq_face_right = character_seq[61]
character_seq_walk_left = character_seq[72:74]
character_seq_face_left = character_seq[73]


background_image = pyglet.resource.image("fantasy_background1.png")
#background_image = pyglet.resource.image("asteroid.png")
center_image(background_image)


