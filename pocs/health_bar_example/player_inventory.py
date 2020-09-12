from pyglet import shapes
import pyglet
import resources

class InventorySprite(pyglet.sprite.Sprite):
    ''' A health bar sprite '''
    def __init__(self, x_position, y_position, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x = x_position
        self.y = y_position


class PlayerInventory():
    ''' An object for inventory item sprites and shapes '''    
    def __init__(self, batch, group1, group2, group3):

        self.batch = batch
        self.group1 = group1
        self.group2 = group2
        self.group3 = group3
        self.create_health_bar()
        self.create_health_potion_counter()


    def create_health_bar(self):

        self.health_bar = shapes.Rectangle(290, 718, 500, 28, color=(255,0, 0), batch=self.batch, group=self.group2)
        self.health_bar_container = InventorySprite(287, 715, img=resources.health_bar_container, batch=self.batch, group=self.group1)
        self.health_percent_label = pyglet.text.Label('100%',
                                    font_name='Arial',
                                    font_size=20,
                                    x=512, y=723,
                                    batch=self.batch, group=self.group3)
        self.health_bar_heart = InventorySprite(258, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)

    def create_health_potion_counter(self):

        self.health_potion_sprite = InventorySprite(896, 715, img=resources.health_potion, batch=self.batch, group=self.group2)
        self.health_potion_counter = pyglet.text.Label('0',
                                    font_name='Arial',
                                    font_size=20,
                                    x=938, y=723,
                                    batch=self.batch, group=self.group2)
        self.backpack = InventorySprite(834, 704, img=resources.backpack, batch=self.batch, group=self.group1)


    def update(self, dt):
        pass

    

    # Update the health bar to the new health. Health is assumed to be based on 100 max health.
    def update_health(self, new_health):
        self.health_bar.width = new_health * 5
        self.health_percent_label.text = str(new_health) + "%"

    def update_potions_count(self, new_potions_count):
        # print(new_potions_count)
        self.health_potion_counter.text = str(new_potions_count)
