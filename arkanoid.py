import time
import sys, pygame
pygame.init()

size = width, height = 1280, 1024
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("small_ball.png")
ballrect = ball.get_rect()
speed = [10.0, 0.0]
bounce_loss = 0.90

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
        ballrect = ballrect.move([-ballrect.top, 0])
        speed[1] *= -bounce_loss
    if ballrect.bottom > height:
        ballrect = ballrect.move([0, height-ballrect.bottom])
        speed[1] *= -bounce_loss

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.02)
