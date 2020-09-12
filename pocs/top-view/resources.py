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

crystal1 = pyglet.resource.image("crystal1.png")
crystal2 = pyglet.resource.image("crystal2.png")
crystal3 = pyglet.resource.image("crystal3.png")

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

slash_image = pyglet.resource.image("weapons_1.png")
#slash_image_flip = slash_image.get_transform(rotate=180)
slash_seq = pyglet.image.ImageGrid(slash_image, 7, 5)
#slash_seq1 = slash_seq[6:10]
slash_seq1 = slash_seq[6:10]


sword_image = pyglet.resource.image("sword.png")
sword_image_blue = pyglet.resource.image("sword_blue.png")
sword_image_gold = pyglet.resource.image("sword_gold.png")
sword_image_pink = pyglet.resource.image("sword_pink.png")



center_image(sword_image)

sword_image = pyglet.resource.image("sword2.png")
sword_image_blue = pyglet.resource.image("sword2_blue.png")
sword_image_gold = pyglet.resource.image("sword2_gold.png")
sword_image_pink = pyglet.resource.image("sword2_pink.png")


sword_seq = pyglet.image.ImageGrid(sword_image, 1, 2)
sword_seq_blue = pyglet.image.ImageGrid(sword_image_blue, 1, 2)
sword_seq_gold = pyglet.image.ImageGrid(sword_image_gold, 1, 2)
sword_seq_pink = pyglet.image.ImageGrid(sword_image_pink, 1, 2)

sword_still = sword_seq[0]
sword_still_blue = sword_seq_blue[0]
sword_still_gold = sword_seq_gold[0]
sword_still_pink = sword_seq_pink[0]

background_image = pyglet.resource.image("fantasy_background1.png")
#background_image = pyglet.resource.image("asteroid.png")
center_image(background_image)

class HeroImages():
    ''' Image References for Hero Sprite '''
    def __init__(self):
        self.walk_up = pyglet.image.Animation.from_image_sequence(character_seq_walk_up, duration=0.1,loop=True)
        self.walk_down = pyglet.image.Animation.from_image_sequence(character_seq_walk_down, duration=0.1,loop=True)
        self.walk_left = pyglet.image.Animation.from_image_sequence(character_seq_walk_left, duration=0.1,loop=True)
        self.walk_right = pyglet.image.Animation.from_image_sequence(character_seq_walk_right, duration=0.1,loop=True)

        self.face_up = character_seq_face_up
        self.face_down = character_seq_face_down
        self.face_left = character_seq_face_left
        self.face_right = character_seq_face_right

        self.slash = pyglet.image.Animation.from_image_sequence(slash_seq1, duration=0.05,loop=False)

        #self.sword = sword_image
        self.sword = pyglet.image.Animation.from_image_sequence(sword_seq, duration=0.1,loop=True)
        self.sword_blue = pyglet.image.Animation.from_image_sequence(sword_seq_blue, duration=0.1,loop=True)
        self.sword_gold = pyglet.image.Animation.from_image_sequence(sword_seq_gold, duration=0.1,loop=True)
        self.sword_pink = pyglet.image.Animation.from_image_sequence(sword_seq_pink, duration=0.1,loop=True)

        self.sword_still = sword_still
        self.sword_still_blue = sword_still_blue
        self.sword_still_gold = sword_still_gold
        self.sword_still_pink = sword_still_pink

