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
        self.speed = 10
        self.direction = math.radians(random.randint(-180,180))
        self.centre = [random.randint(container.rect.left,container.rect.right),random.randint(container.rect.top,container.rect.bottom)]
        self.radius = 10

    def update(self):
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
        self.centre[0] += math.cos(self.direction)*self.speed
        self.centre[1] -= math.sin(self.direction)*self.speed
        pygame.draw.circle(screen, (0,0,0), self.centre, self.radius)

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
    
class box:
    def __init__(self):
        self.rect = pygame.Rect(resolution[0]//10,resolution[1]//10,resolution[0]//2,resolution[1]//2)

    def update(self):
        pygame.draw.rect(screen,(0,0,0),self.rect,10,5)
    
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

#main loop
running = True
while running:
    #stops the loop if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    for obj in objectlist:
        obj.update()

    container.update()

    running = button.update()

    pygame.display.update()
    clock.tick(60)
quit()