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
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.direction = -45
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.direction = 45
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.direction = 135
        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.direction = -135
        elif keys[pygame.K_UP]:
            self.direction = -90
        elif keys[pygame.K_DOWN]:
            self.direction = 90
        elif keys[pygame.K_LEFT]:
            self.direction = 180
        elif keys[pygame.K_RIGHT]:
            self.direction = 0
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.speed = sourcespeed
        else:
            self.speed = 0
        raddirection = math.radians(self.direction) #converts the direction attribute into radians
        #uses trigonometry to convert direction and distance values into x and y position changes
        self.centre = [self.centre[0]+round(math.cos(raddirection)*self.speed),self.centre[1]+round(math.sin(raddirection)*self.speed)]
        #checks if the wavesource is outside of the screen and moves it back to the border if it is
        if self.centre[0] > resolution[0]:
            self.centre[0] = resolution[0]
        elif self.centre [0] < 0:
            self.centre[0] = 0
        if self.centre[1] > resolution[1]:
            self.centre[1] = resolution[1]
        elif self.centre [1] < 0:
            self.centre[1] = 0
        #displays the wave source
        pygame.draw.circle(screen, (0,0,0), self.centre, 50)

class slider:
    def __init__(self, startx, endx, height, startvalue, endvalue):
        #sets all of the initial attributes of the slider
        self.startx = startx #sets where the slider line starts
        self.endx = endx #sets where the slider line ends
        self.height = height #sets what the height of the slider is on the screen
        self.startvalue = startvalue #sets what value the slider should start at
        self.endvalue = endvalue #sets what value the slider should end at
        self.sliderx = resolution[0]//2 #sets the current position of the slider on the line
        self.hovered = False #shows if the slider is being hovered over by the mouse
        self.clicked = False #shows if the slider is being clicked on by the mouse

    def update(self):
        #draws the line and circle which make up the slider
        pygame.draw.line(screen, (0,0,0), [self.startx,self.height], [self.endx,self.height], 10)
        slider = pygame.draw.circle(screen, (0,0,0), [self.sliderx,self.height], 25)
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
    
def writetext(text,size,x,y):
    font = pygame.font.Font('freesansbold.ttf', size) #sets the font which the text will be rendered in
    textRect = font.render(text, True, (0,0,0)).get_rect() #creates an image of the text input
    textRect.center = (x, y) #sets the centre of the image to specified coordinates
    screen.blit(font.render(text, True, (0,0,0)), textRect) #displays the text on the screen

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler Effect Simulation')

wavelist = [] #array which all of the wave objects are stored in
wavelength = 5 #determines the distance between the wavefronts
wavecounter = 0 #keeps track of how many ticks it has been since the last wave was generated
wavespeed = 2 #determines how quickly the waves move outward
sourcespeed = 5 #determines how quickly the wave source moves
wavesource = source() #instantiates the wave source
wavelengthslider = slider(500,resolution[0]-500, resolution[1]-100, 1, 10) #instantiates the slider which controls wavelength
wavespeedslider = slider(500,resolution[0]-500, resolution[1]-250, 1, 5) #instantiates the slider which controls wave speed
sourcespeedslider = slider(500,resolution[0]-500, resolution[1]-400, 1, 10) #instantiates the slider which controls source speed

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    #updates all of the sliders    
    wavelength = wavelengthslider.update()
    wavespeed = wavespeedslider.update()
    sourcespeed = sourcespeedslider.update()

    #writes the labels for each slider
    writetext(f"Wavelength: {wavelength}",32,resolution[0]//2,resolution[1]-175)
    writetext(f"Wave Speed: {wavespeed}",32,resolution[0]//2,resolution[1]-325)
    writetext(f"Source Speed: {sourcespeed}",32,resolution[0]//2,resolution[1]-475)

    #checks if sliders are being hovered over and changes the cursor to a hand if they are
    if wavelengthslider.hovered or wavespeedslider.hovered or sourcespeedslider.hovered:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    wavesource.update()

    #creates a new wave object every set number of ticks
    if wavecounter >= wavelength:
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