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

class slider:
    def __init__(self, startx, endx, height, startvalue, endvalue):
        #sets all of the initial attributes of the slider
        self.startx = startx
        self.endx = endx
        self.height = height
        self.startvalue = startvalue
        self.endvalue = endvalue
        self.sliderx = resolution[0]//2
        self.hovered = False
        self.clicked = False
        self.slidersize = (resolution[1]//58)
        self.linesize = resolution[1]//120

    def update(self):
        #draws the line and circle which make up the slider
        pygame.draw.line(screen, (0,0,0), [self.startx,self.height], [self.endx,self.height], self.linesize)
        slider = pygame.draw.circle(screen, (0,0,0), [self.sliderx,self.height], self.slidersize)
        #checks if the slider is being hovered over by the mouse
        if slider.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False
        #checks if the slider is being cliicked on by the mouse
        if self.hovered and pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.clicked = True
        elif pygame.mouse.get_pressed(num_buttons=3)[0] == False:
            self.clicked = False
        #makes the slider move with the mouse if it is being clicked on
        if self.clicked:
            self.sliderx = pygame.mouse.get_pos()[0]
        #stops the slider from going off the line
        if self.sliderx < self.startx:
            self.sliderx = self.startx
        elif self.sliderx > self.endx:
            self.sliderx = self.endx
        #calculates the value which the slider is on based on its position, length and chosen start and end values
        return round((((self.sliderx-self.startx)/(self.endx-self.startx))*(self.endvalue-self.startvalue))+self.startvalue)

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Kinematics Simulation')

block = object()
thrustslider = slider(resolution[0]//5,resolution[0]//(5/4),resolution[1]//(10/9),0,25)

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    block.speed = thrustslider.update()
    block.update()

    pygame.display.update()
    clock.tick(60)
quit()