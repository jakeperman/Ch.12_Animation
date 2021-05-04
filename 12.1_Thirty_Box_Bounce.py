'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black box-p-es(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''

import arcade
import random
sw = 600
sh = 600

class Box:
    def __init__(self):
        """

        @type dx: int
        """
        self.size = random.randint(10, 50)
        self.half = (self.size//2)
        self.x = random.randint((30 + self.half), (sw-30 - self.half))
        self.y = random.randint((30 + self.half), (sh-30 - self.half))
        self.dx = 0
        self.dy = 0
        while self.dx == 0:
            self.dx = random.randint(-5, 5)
        while self.dy == 0:
            self.dy = random.randint(-5,5)
        self.color = arcade.color.BLACK
        self.edge_r = self.x + self.half
        self.edge_l = self.x - self.half
        self.edge_t = self.y + self.half
        self.edge_b = self.y - self.half

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy
        self.edge_r = self.x + self.half
        self.edge_l = self.x - self.half
        self.edge_t = self.y + self.half
        self.edge_b = self.y - self.half
        # print(self.dx)
        # print(self.dy)



class Rail:
    def __init__(self, x_start, y_start, x_end, y_end, color, width, edge_x=0, edge_y=0, kind=None):
        edge_x = edge_x
        edge_y = edge_y
        if kind == "vert":
            edge = edge_x
        elif kind == "horz":
            edge = edge_y
        else:
            edge = "null"
        self.rail_right = None
        self.rail_top = None
        self.rail_bottom = None
        self.rail_left = None
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.color = color
        self.width = width
        self.edge_x = edge_x
        self.edge_y = edge_y

    def draw_rail(self):
        arcade.draw_line(self.x_start, self.y_start, self.x_end, self.y_end, self.color, self.width)







class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ALMOND)
        # self.box = Box(width/2, height/2, 3, -2, 15, arcade.color.BLEU_DE_FRANCE)
        self.boxes = []
        self.rails = []
        for i in range(0, 300):
            self.boxes.append(Box())
        # self.balls = [Box(50, 20, 3, -2, 15, arcade.color.PURPLE)]
        self.rail_right = Rail(sw - 15, sh - 30, sw - 15, 30, arcade.color.AFRICAN_VIOLET, 30,
                               edge_x=sw - 30, kind="vert")
        self.rail_top = Rail(30, sh - 15, sw - 30, sh - 15, arcade.color.BANANA_YELLOW, 30,
                             edge_y=sh - 30, kind="horz")
        self.rail_bottom = Rail(30, 15, sw - 30, 15, arcade.color.JADE, 30, edge_y=30,
                                kind="horz")
        self.rail_left = Rail(15, sh - 30, 15, 30, arcade.color.CORNFLOWER_BLUE, 30, edge_x=30,
                              kind="vert")
        self.rails = [self.rail_left, self.rail_top, self.rail_right, self.rail_bottom]


    def on_draw(self):
        arcade.start_render()
        # self.box.draw_box()
        for i in range(len(self.rails)):
            self.rails[i].draw_rail()
            print('x')
        for i in range(len(self.boxes)):
            self.boxes[i].draw_box()




        # self.balls[0].draw_ball()

    def on_update(self, delta_time: float):
        for box in self.boxes:

            if box.edge_r >= self.rail_right.edge_x:
                box.dx *= -1
                box.color = self.rail_right.color
            elif box.edge_l <= self.rail_left.edge_x:
                box.dx *= -1
                box.color = self.rail_left.color
            if box.edge_t >= self.rail_top.edge_y:
                box.dy *= -1
                box.color = self.rail_top.color
            elif box.edge_b <= self.rail_bottom.edge_y:
                box.dy *= -1
                box.color = self.rail_bottom.color
            box.update_box()

def main():
    my_window = MyGame(sw, sh, "(Insert Title)")
    arcade.run()


if __name__ == "__main__":
    main()


