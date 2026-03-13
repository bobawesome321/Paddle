import pygame
import sys


pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brick Smash 2")

WHITE = (255,255,255)
BLUE = (0,150,255)

clock = pygame.time.Clock()


class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((120,20))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT - 20

        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH



class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((15,15))
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        self.speed_x = 5
        self.speed_y = -5

    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off left/right walls
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.speed_x *= -1

        # Bounce off top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1



paddle = Paddle()
ball = Ball()

paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

paddle_group.add(paddle)
ball_group.add(ball)



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    paddle_group.update()
    ball_group.update()

    
    if pygame.sprite.spritecollide(ball, paddle_group, False):
        ball.speed_y *= -1

    
    screen.fill((0,0,0))

    paddle_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
