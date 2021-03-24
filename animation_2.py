import arcade
import random
import timeit

# set screen width and height
SH = 600
SW = 1000

def maze():
    pass

class Pacman:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def create(self):


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
        # arcade.draw_line()

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
