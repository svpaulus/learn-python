import time
import sys, pygame
pygame.init()

size = width, height = 1280, 1024
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("small_ball.png")
platform = pygame.image.load('platform.png')
platformrect = platform.get_rect()
platformrect = platformrect.move([1280//2 - platformrect.width//2, 1000])
ballrect = ball.get_rect()
ballrect = ballrect.move([1280//2, 0])
speed = [0.0, 0.0]
bounce_loss = 0.90
platform_bounce = 1.10

# platformrect = platformrect.move([400, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    speed[1] += 0.1

    if ballrect.left < 0:
        ballrect = ballrect.move([-ballrect.left, 0])
        speed[0] *= -bounce_loss
    if ballrect.right > width:
        ballrect = ballrect.move([width-ballrect.right, 0])
        speed[0] *= -bounce_loss

    if ballrect.top < 0:
        ballrect = ballrect.move([0, -ballrect.top])
        speed[1] *= -bounce_loss
    if ballrect.bottom > height:
        ballrect = ballrect.move([0, height-ballrect.bottom])
        speed[1] *= -bounce_loss

    if ballrect.bottom > platformrect.top and ballrect.left >= platformrect.left and ballrect.right <= platformrect.right:
        ballrect = ballrect.move([0, platformrect.top-ballrect.bottom])
        speed[1] *= -platform_bounce


    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(platform, platformrect)
    pygame.display.flip()
    time.sleep(0.02)
