# Gravity simulator (11/10/2022) Author - Vedang Ratnaparkhi

import random
import math
import pygame

pygame.init()

pi = math.pi
origin = [0, 0]

box_len = 1000
box_height = 1000
particle_color = (0, 255, 0) # green
background_color = (0, 0, 0) # black
simulator_speed = 30
timer = pygame.time.Clock()
gravitational_constant = 1
dt = 1 / simulator_speed

surface = pygame.display.set_mode((box_len, box_height))
# class Point:
#     
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
        
        
class Particle:
    def __init__(self, mass, posX, posY, velocity, direction):
        self.mass = int(mass)
        self.posX = int(posX)
        self.posY = int(posY)
        self.velocity = float(velocity)
        self.direction = float(direction)
        
def velocity_calculate(magnitude, direction):
    return 0

# temp values
numobjects = 4
particle_array = []

# assigning random values to 4 different particles
for i in range(numobjects):
    particle_array.append(Particle(random.randrange(5, 40), random.randrange(100, 900), random.randrange(100, 900), random.randrange(1, 50), i+1))

# print(particle_array)
display_style = pygame.font.SysFont("agencyfb", 30, "italic")

def display_msg(msg, colr):
    mssg = display_style.render(msg, True, colr)
    surface.blit(mssg, [box_len / 6, box_height / 3])

def start_simulation():
    stop_simulation = False
    stop_simulation = False
    sim_close = False

    while not stop_simulation:
        '''
        while sim_close == True:
            pygame.display.update()
            display_msg("To quit press Q", (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stop_simulation = True
                        sim_close = False
                    if event.key == pygame.K_c:
                        sim_close == True
        '''
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stop_simulation = True
                        sim_close = False
                    if event.key == pygame.K_c:
                        sim_close == True
        
        for i in range(numobjects):
            pygame.draw.circle(surface, particle_color, [particle_array[i].posX, particle_array[i].posY], particle_array[i].mass)
        
        pygame.display.update()

        timer.tick(simulator_speed)


start_simulation()

