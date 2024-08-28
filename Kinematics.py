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
        self.weight = 1000
        self.speed = 0
        self.thrust = 0
        self.drag = 0
        self.dragcoefficient = 10

    def update(self):
        self.drag = self.speed * self.dragcoefficient
        self.speed += (self.thrust - self.drag)/self.weight
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
    
class exitbutton:
    def __init__(self):
        #initial attributes
        self.hovered = False
        self.xpos = resolution[0]-(resolution[0]//26)
        self.ypos = resolution[1]//14
        self.fontsize = 50
        self.writex = resolution[0]-(resolution[0]//50)
        self.writey = resolution[0]//50

    def update(self):
        #draws cross sign
        writetext("X",self.fontsize,self.writex,self.writey)
        #checks for hovers and clicks
        mousepos = pygame.mouse.get_pos()
        if mousepos[0] > self.xpos and mousepos[1] < self.ypos:
            self.hovered = True
        else:
            self.hovered = False
        if self.hovered and pygame.mouse.get_pressed(num_buttons=3)[0]:
            #returns if it is clicked or not
            return False
        return True

class forcearrow:
    def __init__(self):
        self.height = resolution[1]//2
        self.trianglesize = resolution[1]//20

    def update(self,length,pos,multiplier):
        pygame.draw.line(screen,(0,0,0),[pos,self.height],[pos+length,self.height],5)
        pygame.draw.polygon(screen,(0,0,0),[[pos+length,self.height+self.trianglesize],[pos+length,self.height-self.trianglesize],[pos+length+(self.trianglesize*multiplier),self.height]])

def writetext(text,size,x,y):
    #takes a text input and position and size arguments to render text on the screen
    font = pygame.font.Font('freesansbold.ttf', size)
    textRect = font.render(text, True, (0,0,0)).get_rect()
    textRect.center = (x, y)
    screen.blit(font.render(text, True, (0,0,0)), textRect)

#fullscreens the pygame window and gives it a title
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Kinematics Simulation')

block = object()
thrustslider = slider(resolution[0]//5,resolution[0]//(5/4),resolution[1]//(10/9),0,200)
weightslider = slider(resolution[0]//5,resolution[0]//(5/4),resolution[1]//(10/8),500,2000)
thrustarrow = forcearrow()
dragarrow = forcearrow()
button = exitbutton()

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    block.thrust = thrustslider.update()
    block.weight = weightslider.update()
    block.update()

    thrustarrow.update(block.thrust,block.rect.right,1)
    dragarrow.update((block.drag*(-1)),block.rect.left,-1)

    writetext(f"Speed: {round(block.speed,1)}",64,resolution[0]//2,resolution[1]//10)
    writetext(f"Weight: {block.weight}",64,resolution[0]//2,resolution[1]//(10/2))
    writetext(f"Thrust: {block.thrust}",32,block.rect.right+block.thrust,resolution[1]//(5/2))
    writetext(f"Drag: {round(block.drag)}",32,block.rect.left-block.drag,resolution[1]//(5/2))

    #checks if sliders are being hovered over and changes the cursor to a hand if they are
    if thrustslider.hovered or weightslider.hovered or button.hovered:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    running = button.update()

    pygame.display.update()
    clock.tick(60)
quit()