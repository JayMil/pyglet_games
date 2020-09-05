import pyglet
from pyglet.window import key

from gameobjects import GameEnviornment
from gameobjects import CollisionObject
from hero import Hero

class Level(GameEnviornment):
    def __init__(self, window):
        super().__init__(window)

        self.bg_group = pyglet.graphics.OrderedGroup(0)
        self.fg_group = pyglet.graphics.OrderedGroup(1)

        self.create_labels()
        self.hero = Hero(start_pos=(40, self.window.height-150),
                        window_width=self.window.width, window_height=self.window.height,
                        batch=self.batch, group=self.fg_group)

        self.window.push_handlers(self.hero)

        self.create_background()
        #self.grid = self.generate_grid(21, 15)
        #self.enviornment_objs = self.create_enviornment_bounds()


    def generate_grid(self, width, height):
        x = 0
        y = 0
        color=(100, 100, 100)
        grid = []
        for w in range(width):
            grid.append([])
            for h in range(height):
                #grid[w].append(CollisionObject(x+50, y, 50, 50, self.window.width, self.window.height))
                # set corners to different colors r, g, b, y
                if h == 0 and w == 0:
                    color = (255, 0, 0)
                elif h == 0 and w == width-1:
                    color = (0, 255, 0)
                elif h == height-1 and w == 0:
                    color = (0, 0, 255)
                elif h == height-1 and w == width-1:
                    color = (255, 255, 0)

                grid[w].append(pyglet.shapes.Rectangle(x, y, 50, 50, color=color,
                                                    batch=self.batch, group=self.bg_group))
                y += 50
                color=(100, 100, 100)

            y = 0
            x += 50


        return grid

    def create_enviornment_bounds(self):
        ''' Create bounding boxes for enviornment background '''
        objs = []

        hole = CollisionObject(25, 420, 60, 50, self.window.width, self.window.height)
        top_group1 = CollisionObject(155, 440, 180, 135, self.window.width, self.window.height)
        top_group1_1 = CollisionObject(185, 410, 70, 45, self.window.width, self.window.height)
        top_group2 = CollisionObject(345, 490, 100, 85, self.window.width, self.window.height)
        top_group3 = CollisionObject(415, 450, 150, 85, self.window.width, self.window.height)
        top_group4 = CollisionObject(575, 490, 60, 85, self.window.width, self.window.height)
        top_group5 = CollisionObject(635, 440, 60, 85, self.window.width, self.window.height)
        right_group1 = CollisionObject(700, 50, 60, 385, self.window.width, self.window.height)
        water1 = CollisionObject(0, 240, 535, 75, self.window.width, self.window.height)
        water2 = CollisionObject(460, 100, 75, 145, self.window.width, self.window.height)
        water3 = CollisionObject(460, 0, 75, 35, self.window.width, self.window.height)
        
        objs.append(hole)
        objs.append(top_group1)
        objs.append(top_group1_1)
        objs.append(top_group2)
        objs.append(top_group3)
        objs.append(top_group4)
        objs.append(top_group5)
        objs.append(right_group1)
        objs.append(water1)
        objs.append(water2)
        objs.append(water3)


        return objs

    def create_background(self):
        ''' Create sprite for the background image '''
        self.rectangle = pyglet.shapes.Rectangle(0, 0,
                                            self.window.width, self.window.height,
                                            color=(0, 100, 25), 
                                            batch=self.batch, group=self.bg_group)

    def create_labels(self):
        ''' Create helper lables '''
        self.title = pyglet.text.Label('Walking Example',
                                    font_name='Times New Roman',
                                    font_size=24,
                                    x=self.window.width//2, y=self.window.height-30,
                                    anchor_x='center', batch=self.batch,
                                    group=self.fg_group)


        pyglet.text.Label('Move with direction keys',
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-60,
                                    batch=self.batch, group=self.fg_group)

        pyglet.text.Label("Move fast with 'f' key",
                                    font_name='Times New Roman',
                                    font_size=16,
                                    x=20, y=self.window.height-90,
                                    batch=self.batch, group=self.fg_group)

    def handle_enviornment_collisions(self):
        """ Detect and handle collisions with hero and enviornment"""
        for obj in self.enviornment_objs:
            if obj.collides_with(self.hero.hit_box):
                if self.hero.is_moving_up():
                    self.hero.hit_box.y -= self.hero.speed
                elif self.hero.is_moving_down():
                    self.hero.hit_box.y += self.hero.speed
                elif self.hero.is_moving_left():
                    self.hero.hit_box.x += self.hero.speed
                elif self.hero.is_moving_right():
                    self.hero.hit_box.x -= self.hero.speed
                else:
                    print("Unhandled Collision!")

    def draw_env_bounds(self):
        ''' Show the environment bounds '''
        for obj in self.enviornment_objs:
            rectangle = pyglet.shapes.Rectangle(obj.x, obj.y, obj.width, obj.height, color=(0, 0, 255))
            rectangle.opacity = 150
            rectangle.draw()

    def draw_background(self):
        for row in self.grid:
            for cell in self.grid[row]:
                rectangle = pyglet.shapes.Rectangle(cell.x, cell.y, cell.width, cell.height, color=cell.color,
                                                    batch=self.batch, group=self.bg_group)
                rectangle.opacity = 150
                rectangle.draw()

    def update(self, dt):
        self.hero.update(dt)



