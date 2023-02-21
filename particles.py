import pygame, sys, random

class particle_principal:
    def __init__(self):
        self.particles = []

    def emit(self):
        if self.particles:
            self.delete_particle()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),particle[0],int(particle[1]))

    def add_particle(self):
        posx = pygame.mouse.get_pos()[0]
        posy = pygame.mouse.get_pos()[1]
        radius = 10
        directionx = random.randint(-3,3)
        directiony = random.randint(-3,3)
        particle_circle = [[posx,posy],radius,[directionx,directiony]]
        self.particles.append(particle_circle)

    def delete_particle(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


pygame.init()
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

particle1 = particle_principal()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,15)
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particle()
            particle1.add_particle()
            particle1.add_particle()
            particle1.add_particle()
            particle1.add_particle()
            particle1.add_particle()
            particle1.add_particle()

    screen.fill((30,30,30))
    particle1.emit()
    pygame.display.update()
    clock.tick(60)
