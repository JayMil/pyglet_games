from pyglet.window import key

import resources
from gameobjects import PhysicalSpriteObject

class Hero(PhysicalSpriteObject):
    ''' Hero Sprite Class '''
    def __init__(self, update_health, update_potions_count, start_pos=(20, 200), hero_images=resources.HeroImages(), *args, **kwargs):
        super().__init__(img=hero_images.face_down, x=start_pos[0], y=start_pos[1], *args, **kwargs)
        self.hero_images = hero_images
        self.update_health = update_health
        self.update_potions_count = update_potions_count
        # adjust hit box height
        #print(self.height)
        self.hit_box.height -= 55
        
        self.speed = 2

        self.healing_potion_count = 0

        self.health = 100

        self.character_keys = dict(up=False, down=False, 
                                    left=False, right=False,
                                    fast=False)

    def is_moving_up(self):
        return self.character_keys['up']

    def is_moving_down(self):
        return self.character_keys['down']

    def is_moving_left(self):
        return self.character_keys['left']

    def is_moving_right(self):
        return self.character_keys['right']

    def update(self, dt):
        if self.character_keys['fast']:
            self.speed = 4
        else:
            self.speed = 2

        if self.is_moving_up():
            if self.image != self.hero_images.walk_up:
                self.image = self.hero_images.walk_up
            self.hit_box.y += self.speed
        elif self.is_moving_down():
            if self.image != self.hero_images.walk_down:
                self.image = self.hero_images.walk_down
            self.hit_box.y -= self.speed
        elif self.is_moving_left():
            if self.image != self.hero_images.walk_left:
                self.image = self.hero_images.walk_left
            self.hit_box.x -= self.speed
        elif self.is_moving_right():
            if self.image != self.hero_images.walk_right:
                self.image = self.hero_images.walk_right
            self.hit_box.x += self.speed
        else:
            # if not moving, set to still image
            if self.image == self.hero_images.walk_up:
                self.image = self.hero_images.face_up
            elif self.image == self.hero_images.walk_down:
                self.image = self.hero_images.face_down
            elif self.image == self.hero_images.walk_left:
                self.image = self.hero_images.face_left
            elif self.image == self.hero_images.walk_right:
                self.image = self.hero_images.face_right

        # prevent going out of border
        min_x = 0
        min_y = 0
        max_x = self.window_width
        max_y = self.window_height

        if self.hit_box.x < min_x:
            self.hit_box.x = min_x
        elif (self.hit_box.x+self.hit_box.width) > max_x:
            self.hit_box.x = (max_x - self.hit_box.width)
        if self.hit_box.y < min_y:
            self.hit_box.y = min_y
        elif (self.hit_box.y+self.hit_box.height) > max_y:
            self.hit_box.y = (max_y - self.hit_box.height)

        self.x = self.hit_box.x
        self.y = self.hit_box.y

        # if self.health <= 0:
        #     self.hero_images = resources.player_dead

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_keys['up'] = True
        elif symbol == key.DOWN:
            self.character_keys['down'] = True
        elif symbol == key.LEFT:
            self.character_keys['left'] = True
        elif symbol == key.RIGHT:
            self.character_keys['right'] = True
        elif symbol == key.F:
            self.character_keys['fast'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.character_keys['up'] = False
        elif symbol == key.DOWN:
            self.character_keys['down'] = False
        elif symbol == key.LEFT:
            self.character_keys['left'] = False
        elif symbol == key.RIGHT:
            self.character_keys['right'] = False
        elif symbol == key.F:
            self.character_keys['fast'] = False
        elif symbol == key.T:
            self.change_health_amount(-10)
        elif symbol == key.P:
            if self.healing_potion_count >= 1 and self.health < 100:  
                 
                self.change_health_amount(25)
                self.change_potion_count(-1)
    

    def change_health_amount(self, health_change):
        if (self.health + health_change) > 100: 
            self.health = 100
            self.update_health(self.health)
        elif (self.health + health_change) < 0:
            self.health = 0
            self.update_health(self.health)
        else:
            self.health += health_change
            self.update_health(self.health)


    def change_potion_count(self, num_potions_change):
        if (self.healing_potion_count + num_potions_change) >= 0:
            self.healing_potion_count += num_potions_change
            self.update_potions_count(self.healing_potion_count)
        