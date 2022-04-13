import pygame

pygame.init()

screen_width = 960
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_heigth))

#Add a title to the display window
pygame.display.set_caption("A Beautiful Sunset")

done = False

# Load a background image
background = pygame.image.load("../images/sunset.jpg")
sprite = pygame.image.load("../images/bee-icon.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    screen.blit(sprite, (100, 100))
    pygame.display.update()
pygame.quit()