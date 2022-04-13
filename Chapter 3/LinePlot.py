import pygame

pygame.init()

screen_width = 1000
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_heigth))

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
xoriginoffset = int(screen.get_width() / 2)
yoriginoffset = int(screen.get_height() / 2)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # x axis
    for x in range(-500, 500):
        screen.set_at((x + xoriginoffset, yoriginoffset), green)

    # y axis
    for y in range(-400, 400):
        screen.set_at((xoriginoffset, y + yoriginoffset), green)

    # Line
    for x in range(-500, 500):
        y = int(10 * x) - 100   # LINE EQUATION
        screen.set_at((x + xoriginoffset, y + yoriginoffset), white)

    pygame.display.update()
pygame.quit()