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
        self.centre = wavesource.centre #sets the fixed centre to the current wave source position
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
        #gets keys pressed and converts them into direction values
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = -90
            self.speed = sourcespeed
        elif keys[pygame.K_DOWN]:
            self.direction = 90
            self.speed = sourcespeed
        elif keys[pygame.K_LEFT]:
            self.direction = 180
            self.speed = sourcespeed
        elif keys[pygame.K_RIGHT]:
            self.direction = 0
            self.speed = sourcespeed
        else:
            self.speed = 0
        raddirection = math.radians(self.direction) #converts the direction attribute into radians
        #uses trigonometry to convert direction and distance values into x and y position changes
        self.centre = [self.centre[0]+round(math.cos(raddirection)*self.speed),self.centre[1]+round(math.sin(raddirection)*self.speed)]
        pygame.draw.circle(screen, (0,0,0), self.centre, 50)


#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler Effect Simulation')

wavelist = [] #array which all of the wave objects are stored in
wavelength = 5 #determines the distance between the wavefronts
wavecounter = 0 #keeps track of how many ticks it has been since the last wave was generated
wavespeed = 2 #determines how quickly the waves move outward
sourcespeed = 5 #determines how quickly the wave source moves
wavesource = source() #instantiates the wave source

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