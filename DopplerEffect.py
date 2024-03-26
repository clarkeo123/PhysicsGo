import pygame

pygame.init()
clock = pygame.time.Clock()
resolution = pygame.display.get_desktop_sizes()[0]

class wave:
    def __init__(self):
        self.centre = pygame.mouse.get_pos()
        self.radius = 50

    def update(self):
        pygame.draw.circle(screen, (0,0,0), self.centre, self.radius, 1)
        self.radius += 1

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Doppler test and that')

wavelist = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    wavelist.append(wave())
    
    for obj in wavelist:
        obj.update()
        if obj.radius > 300:
            wavelist.remove(obj)

    pygame.display.update()
    clock.tick(60)