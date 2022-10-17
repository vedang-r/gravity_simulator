# Gravity simulator (24/09/2022) Author - Vedang Ratnaparkhi

import numpy as np
# from numpy import array
import math
# import matplotlib.pyplot as plt
import pygame

# time differential:
dt = 1

# constants:
G = 1 # actual value = 6.67408 * 10**-11

# How to use magnitude of vector using numpy
# x = np.array([3, 4])
# y = np.linalg.norm(x)
# print(y)

# r = np.array([3, 4])
# y = r / np.linalg.norm(r)
# print(y)

velocity_vectorX = []
velocity_vectorY = []
sum = np.array([0, 0])

# <TEMPORARY VALUES>
particle_mass =[5, 5]
particle_velocity =[]
particle_posX = [20, 980, 20, 980]
particle_posY = [980, 20, 980, 20]
# </TEMPORARY VALUES>

# need to add a distance and velocity calculator so that single_object_force() can have necessary attributes 
# or maybe not

# DISTANCE IS JUST THE COORDINATES OF THE OTHER OBJECT
# Force of one particle on selected particle
def single_object_force(Velocity, mass, Distance):
    acceleration_magnitude = G * mass / (np.linalg.norm(Distance))**2 * dt #(scalar)
    Acceleration_direction = Distance / np.linalg.norm(Distance) #(vector)
    Total_acceleration = acceleration_magnitude * Acceleration_direction #(vector)
    Velocity += Total_acceleration #(vector)
    velocity_vectorX.append(Velocity(0))
    velocity_vectorY.append(Velocity(1))
    # <ADD IDENTIFIER TO AVOID CALCULATING GRAVITY OF ITSELF AGAINST ITSELF>

def faltu_net_force(velocity_vectorX, velocity_vectorY):
    accX = np.array(velocity_vectorX)
    accY = np.array(velocity_vectorY)
    # for i in velocity_vectorX:
    #     for i in velocity_vectorY:
    #         final_movement.append(accX(i) + accY(i))
    sum_vector = accX + accY
    return(sum_vector)

def net_force():
    addarray = np.array([])
    # addarray2 = np.array([])
    sum.append(velocity_vectorX(0), velocity_vectorY(0))
    for i in velocity_vectorX:
        addarray = np.append(addarray, velocity_vectorX(i+1), velocity_vectorY(i+1))
        # addarray2 = np.append(addarray2, velocity_vectorX(i+1), velocity_vectorY(i+1))
        sum = addarray + sum
    return(sum)

# <only for testing purposes>
tempvelocity = []
tempmass = []
tempdistance = []

        

x = [3, 4]
y = [5, 12]
a = net_force(x, y)
print(a)



box_len = 1000
box_height = 1000

# EXECUTION:

# pygame.init()

# surface = pygame.display.set_mode((box_len, box_height))
# pygame.display.set_caption("GRAVITY SIM")


