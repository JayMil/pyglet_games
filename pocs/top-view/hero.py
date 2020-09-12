from enum import Enum
import pyglet
from pyglet.window import key

import resources
from gameobjects import PhysicalSpriteObject



HERO_IMAGES = resources.HeroImages()

class Hero(PhysicalSpriteObject):
    ''' Hero Sprite Class '''
    def __init__(self,handle_sword_collisions, start_pos=(20, 200), *args, **kwargs):
        super().__init__(img=HERO_IMAGES.face_down, x=start_pos[0], y=start_pos[1], *args, **kwargs)

        self.facing = Facing.DOWN
        self.moving = []

        self.handle_sword_collisions = handle_sword_collisions

        self.sword = Sword(self, self.batch, self.underlay_group, self.overlay_group)
        self.window.push_handlers(self.sword)


        # adjust hit box height
        # print(self.height)
        self.hit_box.height -= 55
        
        self.speed = 2
        self.fast = False



    def update(self, dt):
        if self.fast:
            self.speed = 4
        else:
            self.speed = 2

        if self.moving:
            if self.facing == Facing.UP:
                if self.image != HERO_IMAGES.walk_up:
                    self.image = HERO_IMAGES.walk_up
                self.hit_box.y += self.speed
            elif self.facing == Facing.DOWN:
                if self.image != HERO_IMAGES.walk_down:
                    self.image = HERO_IMAGES.walk_down
                self.hit_box.y -= self.speed
            elif self.facing == Facing.LEFT:
                if self.image != HERO_IMAGES.walk_left:
                    self.image = HERO_IMAGES.walk_left
                self.hit_box.x -= self.speed
            elif self.facing == Facing.RIGHT:
                if self.image != HERO_IMAGES.walk_right:
                    self.image = HERO_IMAGES.walk_right
                self.hit_box.x += self.speed
        else:
            # if not moving, set to still image
            if self.image == HERO_IMAGES.walk_up:
                self.image = HERO_IMAGES.face_up
            elif self.image == HERO_IMAGES.walk_down:
                self.image = HERO_IMAGES.face_down
            elif self.image == HERO_IMAGES.walk_left:
                self.image = HERO_IMAGES.face_left
            elif self.image == HERO_IMAGES.walk_right:
                self.image = HERO_IMAGES.face_right



        # prevent going out of border
        min_x = 0
        min_y = 0
        max_x = self.window.width
        max_y = self.window.height

        if self.hit_box.x < min_x:
            self.hit_box.x = min_x
        elif (self.hit_box.x+self.hit_box.width) > max_x:
            self.hit_box.x = (max_x - self.hit_box.width)
        if self.hit_box.y < min_y:
            self.hit_box.y = min_y
        elif (self.hit_box.y+self.hit_box.height) > max_y:
            self.hit_box.y = (max_y - self.hit_box.height)

        xdiff = self.x - self.hit_box.x
        ydiff = self.y - self.hit_box.y
        self.x = self.hit_box.x
        self.y = self.hit_box.y
        self.sword.update(dt, self.moving, self.facing, xdiff, ydiff)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.append(Facing.UP)
            self.facing = Facing.UP

        if symbol == key.DOWN:
            self.moving.append(Facing.DOWN)
            self.facing = Facing.DOWN

        if symbol == key.LEFT:
            self.moving.append(Facing.LEFT)
            self.facing = Facing.LEFT

        if symbol == key.RIGHT:
            self.moving.append(Facing.RIGHT)
            self.facing = Facing.RIGHT

        if symbol == key.F:
            self.fast = True


    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.moving.remove(Facing.UP)

        if symbol == key.DOWN:
            self.moving.remove(Facing.DOWN)

        if symbol == key.LEFT:
            self.moving.remove(Facing.LEFT)

        if symbol == key.RIGHT:
            self.moving.remove(Facing.RIGHT)
            
        if symbol == key.F:
            self.fast = False

class Sword():
    def __init__(self, parent, batch, underlay_group, overlay_group):
        self.batch = batch
        self.overlay_group = overlay_group
        self.parent = parent
        self.facing = parent.facing
        self.moving = parent.moving
        self.sword_moving_image = HERO_IMAGES.sword
        self.sword_still_image = HERO_IMAGES.sword_still

        self.slash = None

        self.sword_over = pyglet.sprite.Sprite(img=HERO_IMAGES.sword_still, 
                                            batch=batch, group=overlay_group, 
                                            x=parent.x, y=parent.y)

        self.sword_under = pyglet.sprite.Sprite(img=HERO_IMAGES.sword_still, 
                                            batch=batch, group=underlay_group, 
                                            x=parent.x, y=parent.y)

        self.sword_power_up = 0
        self.sword_down()

    def update(self, dt, moving, facing, xdiff, ydiff):
        self.moving = moving
        if moving:
            if (not self.facing == facing):
                self.facing = facing
                if facing == Facing.UP:
                    self.sword_up()
                elif self.facing == Facing.DOWN:
                    self.sword_down()
                elif self.facing == Facing.LEFT:
                    self.sword_left()
                elif self.facing == Facing.RIGHT:
                    self.sword_right()
        else:
            # if not moving, set to still image
            self.sword_under.image = self.sword_still_image
            self.sword_over.image = self.sword_still_image


        if self.facing == Facing.RIGHT or self.facing == Facing.DOWN:
            self.sword_over.opacity = 255
            self.sword_under.opacity = 0
        else:
            self.sword_over.opacity = 0
            self.sword_under.opacity = 255

        self.sword_over.x -= xdiff
        self.sword_over.y -= ydiff
        self.sword_under.x -= xdiff
        self.sword_under.y -= ydiff
        if (self.slash):
            self.slash.x -= xdiff
            self.slash.y -= ydiff

        if self.sword_power_up > 0:
            self.sword_power_up -= 1
            if self.sword_power_up == 0:
                self.sword_moving_image = HERO_IMAGES.sword
                self.sword_still_image = HERO_IMAGES.sword_still



    def sword_down(self):
        self.sword_over.opacity = 255
        self.sword_under.visibile = 0
        self.sword_over.image = self.sword_moving_image
        self.sword_over.x = self.parent.x+self.parent.width-18
        self.sword_over.y = self.parent.y+(self.parent.height//2)
        self.sword_over.scale = 0.50
        self.sword_over.rotation = 70

    def sword_up(self):
        self.sword_over.opacity = 0
        self.sword_under.opacity = 255
        self.sword_under.image = self.sword_moving_image
        self.sword_under.x = self.parent.x-20
        self.sword_under.y = self.parent.y+(self.parent.height//4)-2
        self.sword_under.scale = 0.5
        self.sword_under.rotation = 20

    def sword_right(self):
        self.sword_over.opacity = 255
        self.sword_under.opacity = 0
        self.sword_over.image = self.sword_moving_image
        self.sword_over.x = self.parent.x+self.parent.width-8
        self.sword_over.y = self.parent.y+(self.parent.height//2)
        self.sword_over.scale = 0.5
        self.sword_over.rotation = 135

    def sword_left(self):
        self.sword_over.opacity = 0
        self.sword_under.opacity = 255
        self.sword_under.image = self.sword_moving_image
        self.sword_under.x = self.parent.x+5
        self.sword_under.y = self.parent.y-10
        self.sword_under.scale = 0.5
        self.sword_under.rotation = -45

    def slash_finish(self):
        ''' Slash animation callback when slash animation is finished '''
        self.slash = None


    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.slash = pyglet.sprite.Sprite(img=HERO_IMAGES.slash, 
                                            batch=self.batch, group=self.overlay_group, 
                                            x=self.parent.x-15, y=self.parent.y)

            self.slash.on_animation_end=self.slash_finish

            if (self.facing == Facing.RIGHT):
                self.slash.x += 10
                self.slash.y -= 5
        
            elif(self.facing == Facing.LEFT):
                self.slash.rotation = 180
                self.slash.x += self.slash.width - 15
                self.slash.y += self.slash.height - 10
             
            elif(self.facing == Facing.DOWN):
                self.slash.rotation = 90
                self.slash.y += self.slash.height - 20
                
            elif(self.facing == Facing.UP):
                self.slash.rotation = 270
                self.slash.x += self.slash.width
                self.slash.y += 10
                

            crystal_hit_check = self.parent.handle_sword_collisions(self.slash)
            if crystal_hit_check != 0:
                if crystal_hit_check == 1:
                    self.sword_moving_image = HERO_IMAGES.sword_blue
                    self.sword_still_image = HERO_IMAGES.sword_still_blue
                    self.sword_power_up = 500
                elif crystal_hit_check == 2: 
                    self.sword_moving_image = HERO_IMAGES.sword_gold
                    self.sword_still_image = HERO_IMAGES.sword_still_gold
                    self.sword_power_up = 500
                elif crystal_hit_check == 3: 
                    self.sword_moving_image = HERO_IMAGES.sword_pink
                    self.sword_still_image = HERO_IMAGES.sword_still_pink
                    self.sword_power_up = 500
                    
class Facing(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

