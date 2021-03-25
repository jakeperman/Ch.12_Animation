import arcade
import random
import timeit
import math
import numpy as np

# set screen width and height
SH = 600
SW = 1000


def maze():
    pass


class Pacman:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.dx = 3
        self.dy = 0
        self.size = size
        self.mouth_top = 60
        self.mouth_bottom = 300
        self.change = -5
        self.rotation = 0
        self.edge_x = self.x + (self.size/2)
        self.edge_y = self.y + (self.size/2)
        # edge vectors [right[st_x, st_y, , up, left, down]
        self.vector = np.array([[self.x, self.y], [self.x+self.size, self.y]])
        self.edge_east = [self.x + self.size, self.y]


    def draw(self):
        arcade.draw_arc_filled(self.x, self.y, self.size, self.size, arcade.color.YELLOW, self.mouth_top, self.mouth_bottom, self.rotation)


    def update(self, objects):
        self.edge = (self.x + (self.size / 2), self.y + (self.size / 2))
        self.edge_x = self.x + (self.size/2)
        self.edge_y = self.y + (self.size / 2)
        if self.mouth_top == 60 or self.mouth_top == 0:
            self.change *= -1
        self.mouth_top -= self.change
        self.mouth_bottom += self.change
        self.x += self.dx
        self.y += self.dy
        # if self.edge_x >= SW or self.edge_x <= 0:
        #     print(self.edge_x)
        #     self.x -= self.dx + 1
        #     self.dx = 0
        #     self.rotate()
        #     self.dy = 3
        # elif self.edge_y >= SH or self.edge_y <= 0:
        #     self.y -= self.dy + 1
        #     self.rotate()
        #     self.dy = 0
        #     self.dx = -3
            
    def rotate(self):
        self.rotation += 90
        
    def edge(self):
        y = self.y + (self.size / 2)
        x = self.x + (self.size / 2)
            
        
        



class Wall:
    def __init__(self, x, y, size, shape=""):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape

    def create(self):
        ln = arcade.create_rectangle_filled(self.x, self.y, self.size, self.size, arcade.color.BLUE)
        return ln


# Window class
class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        # initialize variables for timing
        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None
        self.pac = Pacman(300, 500, 50)
        self.obst = Wall(600, 500, 60)
        self.barriers = ((SW, ))

    # move objects on update
    def on_update(self, delta_time: float):
        # start update timer
        start_time = timeit.default_timer()
        self.pac.update(self.barriers)
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
        self.obst.create().draw()
        self.pac.draw()




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
    window = Window(SW, SH, "Title")
    arcade.run()


if __name__ == "__main__":
    main()
