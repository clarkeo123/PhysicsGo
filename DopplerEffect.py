import pygame
from pygame.gfxdraw import aacircle

pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0]

class wave:
    def __init__(self):
        self.centre = pygame.mouse.get_pos()
        self.radius = 50
        self.opacity = 250

    def update(self):
        aacircle(screen, self.centre[0], self.centre[1], self.radius, (0,0,0,self.opacity))
        self.radius += 1
        self.opacity -= 1

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler test and that')

wavelist = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    wavelist.append(wave())
    
    for obj in wavelist:
        if obj.radius > 300:
            wavelist.remove(obj)
        else:
            obj.update()

    pygame.display.update()
    clock.tick(60)