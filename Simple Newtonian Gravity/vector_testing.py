# Gravity simulator (11/10/2022) Author - Vedang Ratnaparkhi

import random
import math
import pygame
import numpy as np

pygame.init()

class Particle:
    
    def __init__(self, mass, posX, posY, velocityX, velocityY):
        self.mass = int(mass)
        self.position = []
        self.position.append(float(posX))
        self.position.append(float(posY))
        # Velocity vector is one point, assuming other point is origin
        self.velocity =[]
        self.velocity.append(float(velocityX))
        self.velocity.append(float(velocityY))
        self.momentum = self.mass * np.array(self.velocity)

# Mathematical and physical values
simulator_speed = 30
time_coefficient = 1
mass_coefficient = 1
collision_coefficient = 1
pi = math.pi
origin = [0, 0]
dt = 1 * time_coefficient / simulator_speed 
# dt = 1
gravitational_constant = 1

# temp values
numobjects = 5
particle_array = []

# assigning random values to range(numobjects) different particles
for i in range(numobjects):
    particle_array.append(Particle(random.randrange(50, 400), random.randrange(100, 900), random.randrange(100, 900), 0, 0)) # random.randrange(-10, 10), random.randrange(-10, 10)

# Pygame Values
box_len = 1000
box_height = 1000
particle_color = (0, 255, 0) # green
background_color = (0, 0, 0) # black
timer = pygame.time.Clock()
surface = pygame.display.set_mode((box_len, box_height))
display_style = pygame.font.SysFont("agencyfb", 30, "italic")

def display_msg(msg, colr):
    mssg = display_style.render(msg, True, colr)
    surface.blit(mssg, [box_len / 6, box_height / 3])
    
def average(x, y):
    avg = (x + y) / 2
    return avg
   
def velocity_calculate(current_particle, other_particle):
    old_velocity = np.array(current_particle.velocity)
    magnitude = (gravitational_constant * other_particle.mass * mass_coefficient / math.dist(current_particle.position, other_particle.position) ** 2)
    direction = (np.array(np.array(current_particle.position) - np.array(other_particle.position)) / math.dist(current_particle.position, other_particle.position)) * -1
    new_velocity = old_velocity + magnitude * direction
    return new_velocity

def collision_detect(particle1, particle2):
    if math.dist(particle1.position, particle2.position) < (particle1.mass + particle2.mass) * collision_coefficient:
        return True
    else:
        return False

def combine_particles(particle1, particle2):
    new_particle_velocity = np.array(np.array(particle1.momentum) + np.array(particle2.momentum)) / (particle1.mass + particle2.mass)
    new_particle = Particle(particle1.mass + particle2.mass, average(particle1.position[0], particle2.position[0]), average(particle1.position[1], particle2.position[1]), new_particle_velocity[0], new_particle_velocity[1])
    return new_particle

def start_simulation():
    
    stop_simulation = False
    velocity_sum = np.array([0, 0])
    collision_count = int(0)
    object_count = numobjects

    while not stop_simulation:
        
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stop_simulation = True
                        sim_close = False
                    if event.key == pygame.K_c:
                        sim_close == True
         
        surface.fill(background_color)
        
        for i in range(object_count): # current particle
            
            velocity_sum = np.array([0, 0])
            if particle_array[i].mass == 0:
                pass
            else:
                for j in range(object_count): # other particle
                    if i == j: # current particle is not other particle
                        pass
                    elif collision_detect(particle_array[i], particle_array[j]) == True:
                        # new_particle = Particle(particle_array[i].mass + particle_array[j].mass, average(particle_array[i].position[0], particle_array[j].position[0]), average(particle_array[i].position[1], particle_array[j].position[1]))
                        new_particle = combine_particles(particle_array[i], particle_array[j])
                        particle_array[i].mass = 0
                        particle_array[j].mass = 0
                        particle_array.append(new_particle)
                        collision_count += 1
                        pass
                    else:
                        new_velocity = np.array(velocity_calculate(particle_array[i], particle_array[j]))
                        velocity_sum = velocity_sum + new_velocity
                        particle_array[i].velocity = new_velocity

                particle_array[i].position = particle_array[i].position + velocity_sum
                if collision_count > 0:
                    object_count = object_count + 1
                    collision_count = 0
                particle_array[i].position = particle_array[i].position + velocity_sum

                pygame.draw.circle(surface, particle_color, particle_array[i].position, particle_array[i].mass/10)
        
        pygame.display.update()
        timer.tick(simulator_speed)
        
start_simulation()
