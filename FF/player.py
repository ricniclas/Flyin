
import random
import arcade
import os

SPRITE_SCALING = 1

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 448
SCREEN_TITLE = "Testeeeee"


VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):


    def __init__(self, width, height, title):

        super().__init__(width, height, title)


        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # usa para imagem de fundo
        self.background = None



        self.player_list = None
        self.coin_list = None


        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.background = arcade.load_texture ( "images/BG_tiled_.png" , )

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()


        self.player_sprite = arcade.Sprite("images/personagempng_Idle_0.png", 1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 130
        self.player_list.append(self.player_sprite)


        for x in range(200, 1650, 210):
            for y in range(0, 100, 64):

                if random.randrange(5) > 0:
                    wall = arcade.Sprite("images/box.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)





        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):



        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)



        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):


        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):


        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):



        self.physics_engine.update()



        changed = False


        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True


        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True


        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True


        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()