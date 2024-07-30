#modules
import pygame
import random
import math

#initialises the pygame window and creates the fps clock
pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0] #gets the resolution of the display

class exitbutton:
    def __init__(self):
        self.hovered = False
        self.xpos = resolution[0]-(resolution[0]//26)
        self.ypos = resolution[1]//14
        self.fontsize = 50
        self.writex = resolution[0]-(resolution[0]//50)
        self.writey = resolution[0]//50

    def update(self):
        writetext("X",self.fontsize,self.writex,self.writey)
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > self.xpos and mousepos[1] < self.ypos:
            self.hovered = True
        else:
            self.hovered = False
        if self.hovered and pygame.mouse.get_pressed(num_buttons=3)[0]:
            return False
        return True
    
def writetext(text,size,x,y):
    #takes a text input and position and size arguments to render text on the screen
    font = pygame.font.Font('freesansbold.ttf', size)
    textRect = font.render(text, True, (0,0,0)).get_rect()
    textRect.center = (x, y)
    screen.blit(font.render(text, True, (0,0,0)), textRect)

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Particle Pressure Simulation')

button = exitbutton()

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    running = button.update()

    pygame.display.update()
    clock.tick(60)
quit()