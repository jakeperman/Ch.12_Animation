'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
import arcade
import random
import timeit

WH = 600
WW = 600
FLAKE_COUNT = 10000


class Snow:
    def __init__(self, rad, x, y, dy, color=arcade.color.WHITE):
        self.rad = rad
        self.x = x
        self.y = y
        self.dy = dy
        self.color = color
        while self.dy == 0:
            self.dy = random.randint(-4, -1)
        # self.flake_list = arcade.ShapeElementList()

    # creates the vertex buffer for a snowflake and returns the value
    def create_flake(self):
        snow = arcade.create_ellipse_filled(self.x, self.y, self.rad, self.rad, self.color)
        return snow

    def update_snow(self, lst):
        self.y += self.dy

        if lst.center_y < WH/2:
            x = random.randint(0 + self.rad, WW - self.rad)
            y = random.randint(600, 700)
            return [x, y]
        else:
            return None


class Prgm(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DENIM)
        self.flake_list = arcade.ShapeElementList()
        self.lst = []
        self.flakes = []
        self.flakes2 = None
        self.vals = [-1, -2, -3, -4]
        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def setup(self):
        flake_s_4 = arcade.ShapeElementList()
        flake_s_3 = arcade.ShapeElementList()
        flake_s_2 = arcade.ShapeElementList()
        flake_s_1 = arcade.ShapeElementList()
        flake_s2_4 = arcade.ShapeElementList()
        flake_s2_3 = arcade.ShapeElementList()
        flake_s2_2 = arcade.ShapeElementList()
        flake_s2_1 = arcade.ShapeElementList()
        self.flakes = [flake_s_1, flake_s_2, flake_s_3, flake_s_4]
        self.flakes2 = [flake_s2_1, flake_s2_2, flake_s2_3, flake_s2_4]

        for s in range(FLAKE_COUNT):
            x = random.randint(0, WW)
            y = random.randint(0, WH)
            rad = random.randint(1, 3)
            dy = random.randint(-4, -1)
            color = arcade.color.WHITE
            flake = Snow(rad, x, y, dy, color).create_flake()
            for speed in self.flakes:
                if self.vals[self.flakes.index(speed)] == dy:
                    speed.append(flake)
                    self.flakes2[self.flakes.index(speed)].append(flake)
        for each in self.flakes2:
            each.center_y += 600

    def on_update(self, delta_time: float):
        start_time = timeit.default_timer()
        for each in self.flakes:
            each.center_y += self.vals[self.flakes.index(each)]
            if each.center_y <= -600:
                each.center_y = 600
        for them in self.flakes2:
            them.center_y += self.vals[self.flakes2.index(them)]
            if them.center_y < -600:
                them.center_y = 600

        self.processing_time = timeit.default_timer() - start_time

    def on_draw(self):
        draw_start_time = timeit.default_timer()

        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

        arcade.start_render()
        for each in self.flakes:
            each.draw()
            self.flakes2[self.flakes.index(each)].draw()

        # for each in self.lst:
        #     each.draw()
        # for mine in self.flakes2:
        #     mine.draw()
        #     print(mine.center_y)

        arcade.draw_line(WW / 2, WH, WW / 2, 0, arcade.color.BLACK, 10)
        arcade.draw_line(WW, WH / 2, 0, WH / 2, arcade.color.BLACK, 10)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, WH - 20, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, WH - 40, arcade.color.BLACK, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, WH - 60, arcade.color.BLACK, 16)

        self.draw_time = timeit.default_timer() - draw_start_time





def main():
    window = Prgm(WW, WH, "Snowfall")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
