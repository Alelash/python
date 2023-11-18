import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
IMAGE_BALL = "ball.png"
IMAGE_RAKETKA = "paddle.png"
BALL_SCALE = 0.05

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball(IMAGE_BALL, BALL_SCALE)

    def on_draw(self):
        self.clear()
        arcade.set_background_color((70, 249, 100))
        self.ball.draw()

    def setup(self):
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_x = 5
        
    def on_update(self , deltatime = 1/60):
        self.ball.update()
      
class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
            if self.left < 0:
                self.change_x *= -1
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ping-Pong')
window.setup()
arcade.run()
