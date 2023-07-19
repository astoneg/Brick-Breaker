import pygame

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 8

class Paddle:
    COLOR = BLACK
    VELOCITY = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, left=True):
        if left:
            self.x -= self.VELOCITY
        else: 
            self.x += self.VELOCITY

class Ball:
    MAX_VEL = 5
    COLOR = BLACK

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = 0
        self.y_velocity = 5

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

def draw(win, paddle, ball):
    win.fill(WHITE)

    paddle.draw(win) 

    ball.draw(win)

    pygame.display.update()

def collision(ball, paddle):
    if ball.x + ball.radius >= WIDTH:
        ball.x_velocity *= -1
    elif ball.x - ball.radius <= 0:
        ball.x_velocity *= -1

    if ball.y_velocity < 0:
        if ball.y - ball.radius <= 0:
            ball.y_velocity *= -1
    else:
        if ball.y + ball.radius >= paddle.y:
            if ball.x >= paddle.x and ball.x <= paddle.x + paddle.width:
                ball.y_velocity *= -1

                middle_x = paddle.x + paddle.height/2
                difference_x = middle_x - ball.x
                reduction_factor = (paddle.width/2) / ball.MAX_VEL
                x_vel = difference_x / reduction_factor
                ball.x_velocity = -1 * x_vel

def paddle_movement(keys, paddle):
    if keys[pygame.K_LEFT] and paddle.x - paddle.VELOCITY >= 0:
        paddle.move(left=True)
    if keys[pygame.K_RIGHT] and paddle.x + paddle.width + paddle.VELOCITY <= WIDTH:
        paddle.move(left=False)

def main():
    run = True
    clock = pygame.time.Clock()

    paddle = Paddle(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, paddle, ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    break
            
        keys = pygame.key.get_pressed()
        paddle_movement(keys, paddle)

        ball.move()
        collision(ball, paddle)
    
    pygame.quit()

if __name__ == '__main__':
     main()
