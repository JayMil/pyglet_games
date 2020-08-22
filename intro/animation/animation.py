import pyglet
from pyglet.window import key
import resources

window = pyglet.window.Window()
main_batch = pyglet.graphics.Batch()



label = pyglet.text.Label('Animation Example',
                            font_name='Times New Roman',
                            font_size=24,
                            x=window.width//2, y=window.height-30,
                            anchor_x='center', batch=main_batch)



exp1_ani = pyglet.image.Animation.from_image_sequence(resources.explosion_seq1, duration=0.1,loop=False)
exp2_ani = pyglet.image.Animation.from_image_sequence(resources.explosion_seq2, duration=0.1,loop=False)

character_walk_up_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_up, duration=0.1,loop=True)
character_walk_down_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_down, duration=0.1,loop=True)
character_walk_left_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_left, duration=0.1,loop=True)
character_walk_right_ani = pyglet.image.Animation.from_image_sequence(resources.character_seq_walk_right, duration=0.1,loop=True)

character_keys = dict(up=False, down=False, left=False, right=False)
character = pyglet.sprite.Sprite(img=character_walk_down_ani, batch=main_batch, x=20, y=240)

def update(dt):
    if character_keys['up']:
        if character.image != character_walk_up_ani:
            character.image = character_walk_up_ani
        character.y += 1
    elif character_keys['down']:
        if character.image != character_walk_down_ani:
            character.image = character_walk_down_ani
        character.y -= 1
    elif character_keys['left']:
        if character.image != character_walk_left_ani:
            character.image = character_walk_left_ani
        character.x -= 1
    elif character_keys['right']:
        if character.image != character_walk_right_ani:
            character.image = character_walk_right_ani
        character.x += 1
    else:
        if character.image == character_walk_up_ani:
            character.image = resources.character_seq_face_up
        elif character.image == character_walk_down_ani:
            character.image = resources.character_seq_face_down
        elif character.image == character_walk_left_ani:
            character.image = resources.character_seq_face_left
        elif character.image == character_walk_right_ani:
            character.image = resources.character_seq_face_right
    
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.J:
        exp1 = pyglet.sprite.Sprite(img=exp1_ani, batch=main_batch, x=20, y=240)
    elif symbol == key.K:
        exp1 = pyglet.sprite.Sprite(img=exp2_ani, batch=main_batch, x=20, y=240)
    elif symbol == key.UP:
        character_keys['up'] = True
    elif symbol == key.DOWN:
        character_keys['down'] = True
    elif symbol == key.LEFT:
        character_keys['left'] = True
    elif symbol == key.RIGHT:
        character_keys['right'] = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        character_keys['up'] = False
    elif symbol == key.DOWN:
        character_keys['down'] = False
    elif symbol == key.LEFT:
        character_keys['left'] = False
    elif symbol == key.RIGHT:
        character_keys['right'] = False


@window.event
def on_draw():
    window.clear()
    main_batch.draw()

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
