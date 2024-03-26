import pygame

pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0]

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler test and that')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)