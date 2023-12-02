import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
IMAGE_BALL = "C:/Users/andromeda/Documents/ball.png"
IMAGE_PLATFORM = "C:/Users/andromeda/Documents/paddle.png"
BALL_SCALE = 0.05

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball(IMAGE_BALL, BALL_SCALE)
        self.platform = Platform(IMAGE_PLATFORM, 0.4)

    def on_draw(self):
        self.clear()  
        arcade.set_background_color((60, 179, 113))
        self.ball.draw()
        self.platform.draw()
        
    def setup(self):
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        self.ball.change_y = 5
        self.ball.change_angle = 5
        
    def on_update(self, deltatime = 1/60):
        self.ball.update()
       
class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x *= -1
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y *= -1
class Platform(arcade.Sprite):
    def update(self):


        
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ping-Pong')
window.setup()
arcade.run()
