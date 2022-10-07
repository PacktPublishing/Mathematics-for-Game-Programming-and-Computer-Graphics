import pygame

pygame.init()

screen_width = 1000
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_heigth))

done = False
white = pygame.Color(255, 255, 255)


def DrawStar(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    DrawStar(121, 320, 15)
    DrawStar(327, 324, 15)
    DrawStar(691, 431, 20)
    DrawStar(697, 317, 10)
    DrawStar(626, 246, 30)
    DrawStar(343, 212, 10)
    DrawStar(653, 165, 10)
    DrawStar(773, 102, 10)
    DrawStar(822, 153, 10)
    pygame.display.update()
pygame.quit()