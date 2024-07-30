#modules
import pygame
import random
import math

#initialises the pygame window and creates the fps clock
pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0] #gets the resolution of the display

class particle:
    def __init__(self):
        #sets initial attributes of each particle
        self.speed = 10
        self.direction = math.radians(random.randint(-180,180))
        self.centre = [random.randint(container.rect.left,container.rect.right),random.randint(container.rect.top,container.rect.bottom)]
        self.radius = 10
        self.hitbox = pygame.Rect(self.centre[0]-self.radius,self.centre[1]-self.radius,self.radius*2,self.radius*2)

    def update(self):
        #checks for collisions with the edge of the box
        self.speed = particlespeed
        if self.centre[1] < container.rect.top + self.radius or self.centre[1] > container.rect.bottom - self.radius or self.centre[0] > container.rect.right - self.radius or self.centre[0] < container.rect.left + self.radius:
            value = 1
        else:
            value = 0
        if self.centre[1] < container.rect.top + self.radius:
            self.direction = 0-self.direction
            self.centre[1] = container.rect.top + self.radius
        if self.centre[1] > container.rect.bottom - self.radius:
            self.direction = 0-self.direction
            self.centre[1] = container.rect.bottom - self.radius
        if self.centre[0] > container.rect.right - self.radius:
            self.direction = math.pi - self.direction
            self.centre[0] = container.rect.right - self.radius
        if self.centre[0] < container.rect.left + self.radius:
            self.direction = math.pi -self.direction
            self.centre[0] = container.rect.left + self.radius
        #changes the particles position based on its speed and direction
        self.centre[0] += math.cos(self.direction)*self.speed
        self.centre[1] -= math.sin(self.direction)*self.speed
        self.hitbox = pygame.Rect(self.centre[0]-self.radius,self.centre[1]-self.radius,self.radius*2,self.radius*2)
        pygame.draw.circle(screen, (0,0,0), self.centre, self.radius)
        return value

    def rect(self):
        return self.hitbox

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
    
class box:
    def __init__(self):
        self.rect = pygame.Rect(resolution[0]//10,resolution[1]//10,resolution[0]//(10/8),resolution[1]//(10/8))
        self.cornerpos = [resolution[0]//(10/9),resolution[1]//(10/8)]
        self.hovered = False
        self.clicked = False

    def update(self):
        corner = pygame.draw.circle(screen,(0,0,0),self.cornerpos,25)
        #checks if the slider is being hovered over by the mouse
        if corner.collidepoint(pygame.mouse.get_pos()):
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
            self.cornerpos = pygame.mouse.get_pos()
        self.rect.width = max(self.cornerpos[0] - self.rect.left,20)
        self.rect.height = max(self.cornerpos[1] - self.rect.top,20)
        pygame.draw.rect(screen,(0,0,0),self.rect,10,10)
    
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
container = box()
objectlist = []
for i in range(100):
    objectlist.append(particle())
collisioncounter = 0
collisiondisplay = 0
n = 0
speedslider = slider(resolution[0]//10,resolution[0]//(10/9),resolution[1]//(20/19),1,10)
particlespeed = 10

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    for i in range(100):
        collisioncounter += objectlist[i].update()
        collisionlist = objectlist[i].hitbox.collidelistall(objectlist)
        if len(collisionlist) > 1:
            if objectlist[i].hitbox.top > objectlist[collisionlist[1]].hitbox.top and objectlist[i].hitbox.left > objectlist[collisionlist[1]].hitbox.left:
                objectlist[i].direction = math.radians(random.randint(-90,0))
                objectlist[collisionlist[1]].direction = math.radians(random.randint(90,180))
            elif objectlist[i].hitbox.top > objectlist[collisionlist[1]].hitbox.top and objectlist[i].hitbox.left < objectlist[collisionlist[1]].hitbox.left:
                objectlist[i].direction = math.radians(random.randint(-180,-90))
                objectlist[collisionlist[1]].direction = math.radians(random.randint(0,90))
            elif objectlist[i].hitbox.top < objectlist[collisionlist[1]].hitbox.top and objectlist[i].hitbox.left > objectlist[collisionlist[1]].hitbox.left:
                objectlist[i].direction = math.radians(random.randint(0,90))
                objectlist[collisionlist[1]].direction = math.radians(random.randint(-180,-90))
            elif objectlist[i].hitbox.top < objectlist[collisionlist[1]].hitbox.top and objectlist[i].hitbox.left < objectlist[collisionlist[1]].hitbox.left:
                objectlist[i].direction = math.radians(random.randint(90,180))
                objectlist[collisionlist[1]].direction = math.radians(random.randint(-90,0))
            else:
                pass
                
    if n % 60 == 0:
        collisiondisplay, collisioncounter = collisioncounter, 0
    n += 1

    writetext(f"Pressure: {collisiondisplay}", 50, resolution[0]//2, resolution[1]//20)
    writetext(f"Particle Speed: {particlespeed}", 32, resolution[0]//2, resolution[1]//(10/9))

    container.update()
    particlespeed = speedslider.update()
    running = button.update()

    pygame.display.update()
    clock.tick(60)
quit()