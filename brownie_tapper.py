import arcade

SH = 800
SW = 800










class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.brownie = arcade.create_rectangle_filled(SW/2, SH/2, 225, 225, arcade.color.BROWN)
        arcade.set_background_color(arcade.color.CREAM)

    def on_draw(self):
        arcade.start_render()
        self.brownie.draw()



    # def on_update(self, delta_time: float):
    #     pass

def main():
    window = Game(SW, SH, "Brownie Clicker")
    arcade.run()

if __name__ == "__main__":
    main()