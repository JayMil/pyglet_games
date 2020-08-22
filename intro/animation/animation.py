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

#exp1 = pyglet.sprite.Sprite(img=exp1_ani, batch=main_batch,
                                #x=20, y=240)

#exp2 = pyglet.sprite.Sprite(img=exp2_ani, batch=main_batch,
                                #x=20, y=200)

def update(dt):
    pass
    
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.J:
        exp1 = pyglet.sprite.Sprite(img=exp1_ani, batch=main_batch,
                                    x=20, y=240)
    if symbol == key.K:
        exp1 = pyglet.sprite.Sprite(img=exp2_ani, batch=main_batch,
                                    x=20, y=240)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
