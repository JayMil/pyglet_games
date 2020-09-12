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
        self.health_hearts = self.create_health_hearts()
        self.create_health_potion_counter()



    def create_health_hearts(self):


        self.health_holder = InventorySprite(274, 691, img=resources.heart_holder, batch=self.batch, group=self.group1)

        # Create the empty heart that will go behind the filled hearts
        self.health_heart_empty1 = InventorySprite(349, 700, img=resources.health_bar_heart_empty, batch=self.batch, group=self.group2)
        self.health_heart_empty2 = InventorySprite(429, 700, img=resources.health_bar_heart_empty, batch=self.batch, group=self.group2)
        self.health_heart_empty3 = InventorySprite(509, 700, img=resources.health_bar_heart_empty, batch=self.batch, group=self.group2)
        self.health_heart_empty4 = InventorySprite(589, 700, img=resources.health_bar_heart_empty, batch=self.batch, group=self.group2)
        self.health_heart_empty5 = InventorySprite(669, 700, img=resources.health_bar_heart_empty, batch=self.batch, group=self.group2)

        health_hearts = []

        # Create the filled hearts that represent a health point
        health_heart1 = InventorySprite(349, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)
        health_heart2 = InventorySprite(429, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)
        health_heart3 = InventorySprite(509, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)
        health_heart4 = InventorySprite(589, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)
        health_heart5 = InventorySprite(669, 700, img=resources.health_bar_heart, batch=self.batch, group=self.group3)

        health_hearts.append(health_heart1)
        health_hearts.append(health_heart2)
        health_hearts.append(health_heart3)
        health_hearts.append(health_heart4)
        health_hearts.append(health_heart5)

        return health_hearts

    def create_health_potion_counter(self):

        self.backpack = InventorySprite(890, 690, img=resources.backpack, batch=self.batch, group=self.group1)
        self.health_potion_sprite = InventorySprite(self.backpack.x + 71, self.backpack.y + 21, img=resources.health_potion, batch=self.batch, group=self.group2)
        self.health_potion_counter = pyglet.text.Label('',
                                    font_name='Arial',
                                    font_size=10,
                                    x=self.health_potion_sprite.x+28, y=self.health_potion_sprite.y-5,
                                    batch=self.batch, group=self.group2)
        self.health_potion_sprite.visible = False


    def update(self, dt):
        pass

    

    # Update the health bar to the new health. Health is assumed to be based on 100 max health.
    def update_health(self, new_health):


        # Go through all of the hearts and change the image to an empty heart for any that represent health higher than what the player has.
        for index, obj in enumerate(self.health_hearts):
            if (new_health - 1) < index:
                obj.visible = False
            else:
                obj.visible = True

    def update_potions_count(self, new_potions_count):
        # print(new_potions_count)
        self.health_potion_counter.text = str(new_potions_count)

        if new_potions_count == 0:
            self.health_potion_counter.text = ""
            self.health_potion_sprite.visible = False
        else:
            self.health_potion_sprite.visible = True   
