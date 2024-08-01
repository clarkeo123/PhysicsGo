#modules
import pygame
import random
import math

#initialises the pygame window and creates the fps clock
pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0] #gets the resolution of the display

class object:
    def __init__(self):
        self.rect = pygame.Rect(resolution[0]//(20/9),resolution[1]//(20/9),resolution[0]//10,resolution[1]//10)
        self.speed = 10

    def update(self):
        if self.rect.left > resolution[0]:
            self.rect.left = 0-self.rect.width
        self.rect.left += self.speed
        pygame.draw.rect(screen,(0,0,0),self.rect)

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Kinematics Simulation')

block = object()

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    block.update()

    pygame.display.update()
    clock.tick(60)
quit()