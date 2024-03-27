#modules
import pygame
from pygame.gfxdraw import aacircle

#initialises the pygame window and creates the fps clock
pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0] #gets the resolution of the display

class wave:
    def __init__(self):
        self.centre = pygame.mouse.get_pos() #sets the fixed centre to the current mouse position
        self.radius = 50
        self.opacity = 250

    def update(self):
        aacircle(screen, self.centre[0], self.centre[1], self.radius, (0,0,0,self.opacity)) #draws a circle to represent the wave
        #increases the radius of the circle each tick and decreases its opacity
        self.radius += wavespeed
        self.opacity -= wavespeed

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler Effect Simulation')

#array which all of the wave objects are stored in
wavelist = []
wavelength = 5
wavecounter = 0
wavespeed = 2

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    #creates a new wave object every set number of ticks
    if wavecounter == wavelength:
        wavelist.append(wave())
        wavecounter = 0
    else:
        wavecounter += 1
    
    #checks each item in the wave object array
    for obj in wavelist:
        #if the wave is too large it is removed from the array
        if obj.radius > 300:
            wavelist.remove(obj)
        #otherwise it is drawn and its attributes are updated
        else:
            obj.update()

    #updates the screen and ticks the fps clock at 60 frames per second
    pygame.display.update()
    clock.tick(60)