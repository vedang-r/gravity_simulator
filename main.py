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
        self.valid = True

# Mathematical and physical values
simulator_speed = 30
time_coefficient = 1
mass_coefficient = 1
collision_coefficient = 0.06
pi = math.pi
origin = [0, 0]
dt = 1 * time_coefficient / simulator_speed 
# dt = 1
gravitational_constant = 1.5

# temp values
numobjects = 5
particle_array = []

# assigning random values to range(numobjects) different particles

for i in range(numobjects):
    particle_array.append(Particle(random.randrange(50, 300), random.randrange(100, 900), random.randrange(100, 900), random.randrange(-5, 5) * 0.1, random.randrange(-5, 5) * 0.1)) # random.randrange(-5, 5) * 0.1, random.randrange(-5, 5) * 0.1

# Pygame Values
box_len = 1000
box_height = 1000
particle_color = (36, 218, 255) # sky blue
background_color = (0, 0, 0) # black
timer = pygame.time.Clock()
surface = pygame.display.set_mode((box_len, box_height))
display_style = pygame.font.SysFont("agencyfb", 30, "italic")

# Functions

def velocity_calculate(current_particle, other_particle):
    old_velocity = np.array(current_particle.velocity)
    magnitude = (gravitational_constant * other_particle.mass * mass_coefficient / math.dist(current_particle.position, other_particle.position) ** 2) # Essentially Gm/r^2
    direction = (np.array(np.array(current_particle.position) - np.array(other_particle.position)) / math.dist(current_particle.position, other_particle.position)) * -1 # Unit vector in the direction of other particle
    new_velocity = old_velocity + magnitude * direction # Calculating new velocity
    return new_velocity

def collision_detect(particle1, particle2):
    if math.dist(particle1.position, particle2.position) < (particle1.mass + particle2.mass) * collision_coefficient: # collision_coefficient determines how close the particles should be to count as a collision
        return True
    else:
        return False
    
def average(x, y): # avg of 2 values
    avg = (x + y) / 2
    return avg

def combine_particles(particle1, particle2):
    new_particle_velocity = (np.array(particle1.velocity) * particle1.mass + np.array(particle2.velocity) * particle2.mass) / (2 * (particle1.mass + particle2.mass))
    new_particle = Particle(particle1.mass + particle2.mass, average(particle1.position[0], particle2.position[0]), average(particle1.position[1], particle2.position[1]), new_particle_velocity[0], new_particle_velocity[1])
    return new_particle

def start_simulation():
    
    stop_simulation = False
    velocity_sum = np.array([0, 0])
    object_count = numobjects

    while not stop_simulation:
        
        for event in pygame.event.get(): # if key 'q' is pressed, simulation will stop next tick
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stop_simulation = True
                        sim_close = False
                    if event.key == pygame.K_c:
                        sim_close == True
         
        surface.fill(background_color)
        
        for i in range(object_count): # current particle
            
            velocity_sum = np.array([0, 0])
            if particle_array[i].valid == True:
                for j in range(object_count): # other particle
                    if particle_array[j].valid == True:
                        if i == j: # current particle is not other particle
                            pass
                        elif collision_detect(particle_array[i], particle_array[j]) == True: # If collision is detected
                            particle_array[i] = combine_particles(particle_array[i], particle_array[j])
                            particle_array[j].valid = False
                            pass
                        else: # Satisfies all conditions for gravity to take effect
                            new_velocity = np.array(velocity_calculate(particle_array[i], particle_array[j]))
                            velocity_sum = velocity_sum + new_velocity
                            particle_array[i].velocity = new_velocity
                particle_array[i].position = particle_array[i].position + velocity_sum # adds the new position and updates current position
                
                pygame.draw.circle(surface, particle_color, particle_array[i].position, particle_array[i].mass/12)
            
        pygame.display.update()
        timer.tick(simulator_speed)
        
        """
        PSEUDO CODE:
        
        for every particle in the list of all particles(i):
            if particle is valid:
                for every other particle(j):
                    if particle is valid:
                        if the two particles are the same (i == j), pass
                        
                        elif collision is detected, combine particles
                        
                        else calculate new velocity for particle(i)
            
            use velocity to calculate new position, and update attribute position of that particle
            draw the particle
        
        # The above for loop loops over all particles in the simulator, and compares each one to every other particle in the simulator.
        # As long as both particles are valid and not the same particle, it checks if they are colliding and runs the collision algorithm if they do.
        # If they are not colliding means that their gravity is acting on each other. So per tick, it calculates the velocity and position change per differential of time.
        # Draws the particle after new position is calculated.
            
        update the screen
        wait until next tick
        
        # By default this loop runs 30 times a second
        
        """
        
start_simulation()
