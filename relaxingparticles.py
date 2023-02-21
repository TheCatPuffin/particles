import pygame, sys, random

class Particlething:
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            self.delete_particle()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] += 0.07
                pygame.draw.circle(screen,(200,200,255),particle[0],int(particle[1]))

    def add_particle(self):
        #posx = pygame.mouse.get_pos()[0]
        #posy = pygame.mouse.get_pos()[1]
        posx = 600
        posy = 300
        radius = 3
        directionx = random.uniform(-5,5)
        directiony = random.uniform(-5,5)
        particlecircle = [[posx,posy],radius,[directionx,directiony]]
        self.particles.append(particlecircle)

    def delete_particle(self):
        particlecopy = [particle for particle in self.particles if particle[1] < 10]
        self.particles = particlecopy


pygame.init()
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

particle1 = Particlething()

PARTICLEEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLEEVENT,135)
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLEEVENT:
            particle1.add_particle()

    screen.fill((30,30,30))
    particle1.emit()
    pygame.display.update()
    clock.tick(30)
