'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
'''
import arcade
import random
import timeit

# set screen width and height
SH = 600
SW = 1000
BRICK = 75
MULT = 1
SCALE = BRICK*MULT



class Scene:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Brick(Scene):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.size = SCALE*4
        # self.size = SCALE*.75
        self.rad = self.size/2
        rad = self.rad
        self.center_y = y
        self.center_x = x
        self.hi = 7

    def create(self):
        block = arcade.ShapeElementList()
        brick_out = arcade.create_rectangle_filled(self.x, self.y, self.size, self.size, (245,84,0))
        block.append(brick_out)
        # ratios
        width_r = 1/15
        line_dist_r = 1/4
        # from the left
        mid_line = 7/15-(self.size*.2)
        left_r = 16.5/75
        right_r = 54.5/75
        width = self.size * width_r
        ratio_y = .25
        ratio_x = .25
        dist = round(line_dist_r*self.size)
        #vertical lines
        left = self.x-self.rad
        # brick = arcade.create_line(self.x - self.rad, self.y + self.rad - (width*.8)/2, self.x + self.rad,
        #                            self.y + self.rad - (width*.8)/2,
        #                            (246, 208, 170), width*.8)
        # block.append(brick)
        top = self.y + self.rad
        bot = self.y - self.rad
        for num in range(1, 5):
            ln = arcade.create_line(self.x - self.rad, bot + (line_dist_r*self.size)*num+width/2 - (line_dist_r*self.size), self.x + self.rad,
                                    bot + (line_dist_r*self.size)*num+width/2 - (line_dist_r*self.size), (0, 0, 0), width)
            # if num in []
            block.append(ln)

        for i in range(1, 7):
            line_len = (14/75) * self.size
            line_y_start = self.center_y + self.rad
            coordx1 = left+(left_r*self.size)
            end_y = line_y_start - line_len
            # lx = arcade.create_line(left+(left_r*self.size), top - (line_dist_r*self.size)*i, left+(left_r*self.size),
            #                   top - (line_dist_r*self.size) - (line_dist_r*self.size)*i, (0, 0, 0), width)
            # lx = arcade.create_line(coordx1, line_y_start, coordx1, end_y, (0,0,0), width)
            col = (0,0,0)
            coordx1 = (self.center_x - self.rad)
            for z in range(0, 4):
                # col = random.choices((random.randint(0,255), random.randint(0,255), random.randint(0,255)), k=3)
                c = (line_len * z) + width*(.95) * z
                if z in [0, 2]:
                    print("uh")
                    x_offset = ((36/75) * self.size)
                    coordx1 = self.center_x - self.rad
                    lx = arcade.create_line(coordx1 + x_offset, line_y_start - c, coordx1 + x_offset, end_y - c, col,
                                            width)
                    block.append(lx)
                    lx = arcade.create_line(coordx1 + x_offset + x_offset, line_y_start - c, coordx1 + x_offset + x_offset, end_y - c, col,
                                            width)
                    block.append(lx)
                else:
                    x_offset = (36/75) * self.size
                    lx = arcade.create_line(coordx1 + x_offset, line_y_start - c, coordx1 + x_offset, end_y - c, col,
                                            width)
                    block.append(lx)
                    lx = arcade.create_line(coordx1 + x_offset + x_offset, line_y_start - c,
                                            coordx1 + x_offset + x_offset, end_y - c, col,
                                            width)
                    block.append(lx)
                print("c:",c)


                # for l in range(1,2):
                #     x_offset = (39/75)*self.size*l
                #     lx = arcade.create_line(coordx1 + x_offset, line_y_start - c, coordx1 + x_offset, end_y - c, col, width)
                #     block.append(lx)

        # for num in range()


        # horizontal lines
        # brick = arcade.create_line(self.x - self.rad, self.y + self.rad - (width/2), self.x + self.rad,
        #                            self.y + self.rad - (width/2),
        #                            (250, 210, 160), width)
        # block.append(brick)
        # brick = arcade.create_line(self.x - self.rad, self.y + self.size * ratio_y , self.x + self.rad,
        #                            self.y + self.size * ratio_y,
        #                            (0, 0, 0), width)
        # block.append(brick)
        # brick = arcade.create_line(self.x-self.rad, self.y + self.size * .01, self.x+self.rad,
        #                            self.y + self.size * .01, (0, 0, 0), width)
        # block.append(brick)
        # brick = arcade.create_line(self.x - self.rad, self.y - self.size * ratio_y, self.x + self.rad,
        #                            self.y - self.size * ratio_y, (0, 0, 0), width)
        # block.append(brick)
        # brick = arcade.create_line(self.x - self.rad, self.y - self.rad + (width/2), self.x + self.rad,
        #                            self.y - self.rad + (width/2), (0, 0, 0), width)
        # block.append(brick)
        return block





# Main Class for game
class Prgm(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DENIM)
        # initialize variables for timing
        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None
        self.brick_size = None

    # setup game variables
    def setup(self):
        print("")



    # move objects on update
    def on_update(self, delta_time: float):
        # start update timer
        start_time = timeit.default_timer()

        self.processing_time = timeit.default_timer() - start_time

    # initialize drawing commands
    def on_draw(self):
        # set timer for drawing time
        draw_start_time = timeit.default_timer()
        # calculate frames per second
        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1



        # start render, drawing code goes under here
        arcade.start_render()
        brick = Brick(SW/2, SH/2).create()
        brick.draw()
        pt_list = []
        with open('coordinates.txt', 'r') as coords:
            points = coords.readlines()
        print(points)
        new_points = [pt_list.append(point.strip("\n")) for point in points]
        n_lst = []
        for each in pt_list:
            nums = each.split(',')
            for i in range(len(nums)):
                p = tuple([int(x) for x in nums])
                # print(p)
            n_lst.append(p)

        print(n_lst)

        # print(pt_list)
        points = tuple(n_lst)
        arcade.create_line_strip(points, (0, 0, 0), 5).draw()
        arcade.create_polygon(points, (0,0,0)).draw()



        # Display Timings & FPS
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SH - 20, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SH - 40, arcade.color.BLACK, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, SH - 60, arcade.color.BLACK, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

def main():
    window = Prgm(SW, SH, "Mario")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
