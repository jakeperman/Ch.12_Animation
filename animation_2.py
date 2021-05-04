import arcade
import random
import timeit
import math
import numpy as np

# set screen width and height
SH = 400
SW = 600

def incoord(p1, p2):
    # p1_x = [x for x in range(p1[0] - 2, p1[0] + 3)]
    # p1_y = [x for x in range(p1[1] - 2, p1[1] + 3)]
    p2_x = [x for x in range(int(p2[0]) - 2, int(p1[0]) + 3)]
    p2_y = [x for x in range(int(p2[1]) - 2, int(p2[1]) + 3)]
    if p1[0] in p2_x and p1[1] in p2_y:
        return True
    return False

def maze():
    pass

class Pacman:
    def __init__(self, x, y, size, obstacles):
        self.x = x
        self.obstacles = obstacles
        self.y = y
        self.dx = 3
        self.dy = 0
        self.size = size
        self.mouth_top = 60
        self.mouth_bottom = 300
        self.change = -5
        self.rotation = 0
        self.edge_x = self.x + (self.size/2)
        self.edge_y = self.y - (self.size/2)
        self.edge_x2 = self.x + (self.size/2)
        self.edge_y2 = self.y - (self.size/2)
        self.count = 0
        # edge vectors [right[st_x, st_y, , up, left, down]
        self.vector = np.array([[self.x, self.y], [self.x+self.size, self.y]])
        self.edge_east = [self.x + self.size, self.y]
        self.edge = self.edge_x
        start = arcade.load_sound("pac_start.mp3")
        arcade.play_sound(start)



    def draw(self):
        arcade.draw_arc_filled(self.x, self.y, self.size, self.size, arcade.color.YELLOW, self.mouth_top, self.mouth_bottom, self.rotation)



    def update(self):
        # self.edge = (self.x + (self.size / 2), self.y + (self.size / 2))
        self.count += 1
        # if self.count > 100:
        #     r = random.randint(0, 1)
        #     if r:
        #         self.rotate()
        #         self.count = 0

        self.edge_x = self.x + (self.size/2)
        self.edge_y = self.y + (self.size/2)
        self.edge_x2 = self.x - (self.size/2)
        self.edge_y2 = self.y - (self.size/2)
        if self.rotation > 270:
            self.rotation = 0
        if self.mouth_top == 60 or self.mouth_top == 0:
            self.change *= -1
        self.mouth_top -= self.change
        self.mouth_bottom += self.change
        self.x += self.dx
        self.y += self.dy
        # if self.edge_x in self.obstacles:
        #     self.rotate()
        #     self.x -= 10
        self.edge = (self.edge_x, self.y)
        objs = [list(x) for x in self.obstacles]
        rotate = True
        # for points in self.obstacles:
        #     if incoord(self.edge, points):
        #         self.rotate()

        if rotate:
            # self.rotate()
            pass
        if self.edge_x >= SW -25:
            self.x -= 10 + self.dx
            self.rotate()
        elif self.edge_y >= SH:
            self.y -= 10
            self.rotate()
        elif self.edge_x2 <= 3:
            self.x += 10 + self.dx
            self.rotate()
        elif self.edge_y2 <= 4:
            self.y += 10 + self.dx
            self.rotate()

        # if self.edge[0] >= SW-25:
        #     self.x -= 8
        #     self.rotate()



        if self.rotation == 0:
            self.dx = 3
            self.dy = 0
            self.edge = (self.edge_x, self.y)
        elif self.rotation == 90:
            self.dx = 0
            self.dy = 3
            self.edge = (self.x, self.edge_y)
        elif self.rotation == 180:
            self.dx = -3
            self.dy = 0
            self.edge = (self.edge_x2, self.y)
        elif self.rotation == 270:
            self.dx = 0
            self.dy = -3
            self.edge = (self.x, self.edge_y2)


    def rotate(self):
        self.rotation += 90

    # def edge(self):
    #     y = self.y + (self.size / 2)
    #     x = self.x + (self.size / 2)


class Barrier:
    def __init__(self):
        self.edge = None

    def rectangle(self, x, y, width, height, rotation=None):
        if rotation == "horizontal":
            self.edge = (x, y - height)
            edge_dict = {"y_min": self.edge[1], "y_max": self.edge[1] + width}
        elif rotation == "vertical":
            self.edge = (x - width/2, y)
            edge_dict = {"x_min": self.edge[0], "x_max": self.edge[0] + width}
        else:
            edge_dict = None
        return edge_dict, arcade.create_rectangle_filled(x, y, width, height, arcade.color.BLUE)

    def rect_outline(self, x, y, width, height, thick):
        return arcade.create_rectangle_outline(x, y, width, height, arcade.color.BLUE, thick)

    def random(self):
        x = random.randint(0, SW)
        y = random.randint(0, SH)
        rotation = random.choice(["horizontal", "vertical"])
        height, width = random.randint(10,50), random.randint(10,50)
        if rotation == "horizontal":
            self.edge = np.array([x, y - height])
        elif rotation == "vertical":
            self.edge = (x - width/2, y)
        self.edge = [x, y - height]
        return self.edge, arcade.create_rectangle_filled(x, y, width, height, arcade.color.BLUE)



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
        self.obstacles = []
        self.barriers = arcade.ShapeElementList()
        barrier = Barrier()
        edge, self.obst = barrier.rectangle(SW - 12.5, SH/2, 25, SH, "vertical")
        edge, self.obst = barrier.rectangle(SW - 12.5, SH / 2, 25, SH, "horizontal")
        # self.edges()
        self.obstacles.append(edge)
        self.set_mouse_visible(True)
        # for i in range(50):
        #     obst = barrier.random()
        #     self.obstacles.append(np.array(obst[0]))
        #     self.barriers.append(obst[1])
        # edge, self.wall = barrier.rectangle(SW/2, SH-50, 10, 50, 'vertical')
        # self.obstacles.append(edge)
        # self.box = arcade.create_rectangle_outline(SW/2, SH/2, 300, 200, arcade.color.BLUE, 20)

        self.pac = Pacman(SW / 2, SH / 2, 30, self.obstacles)


    # move objects on update
    def on_update(self, delta_time: float):
        # start update timer
        start_time = timeit.default_timer()
        self.pac.update()
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
        self.obst.draw()
        self.pac.draw()

        arcade.draw_circle_filled(self.pac.edge[0], self.pac.edge[1], 4, arcade.color.WHITE)
        # self.barriers.draw()

        # Display Timings & FPS
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SH - 20, arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SH - 40, arcade.color.WHITE, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, SH - 60, arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        print(f"X: {x}")
        print(f"Y: {y}")
        # arcade.draw_text(f"X:{x}", SW-50, SH-50, (255,255,255), 25)







def main():
    window = Window(SW, SH, "Title")
    arcade.run()


if __name__ == "__main__":
    main()
