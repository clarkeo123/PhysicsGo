#modules
import pygame
from pygame.gfxdraw import aacircle
import math

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

class source:
    def __init__(self):
        self.centre = [resolution[0]//2,resolution[1]//2]
        self.direction = 0
        self.speed = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = 0
            self.speed = sourcespeed
        elif keys[pygame.K_DOWN]:
            self.direction = 180
            self.speed = sourcespeed
        elif keys[pygame.K_LEFT]:
            self.direction = -90
            self.speed = sourcespeed
        elif keys[pygame.K_RIGHT]:
            self.direction = 90
            self.speed = sourcespeed
        else:
            self.speed = 0
        raddirection = math.radians(self.direction)
        self.centre = [self.centre[0]+(math.cos(raddirection)*self.speed),self.centre[1]+(math.sin(raddirection)*self.speed)]
        pygame.draw.circle(screen, (0,0,0), self.centre, 50)


#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler Effect Simulation')

#array which all of the wave objects are stored in
wavelist = []
wavelength = 5
wavecounter = 0
wavespeed = 2
sourcespeed = 5
wavesource = source()

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    wavesource.update()

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