# gravity_simulator

Author -Vedang Ratnaparkhi

This gravity simulator is coded in Python 3.9.7, using both procedural and object oriented methods.
The particles are a class, with attributes mass, position, velocity, and momentum (calculated using the mass and velocity).
All the vector quantities are stored and used as ordered arrays with the x and y coordinates.
The core structure of the simulation based on a 2 dimensional grid in a coordinate system.
The magnitude and direction of velocity is defined as a vector with
one point, assuming the first point is the origin. 
Gravity is calculated by differentiating Newton's gravitational formula, and calculating gravitational force for each particle with every other particle per
tick 'dt'. This loop runs multiple times a second, the smaller the dt the greater the precision.
This simulator can simulate gravity for any number of objects.

# Running the .exe file 
For Windows: 
Download the file "gravity_simulator.exe", and run it. 
Every time it is executed, it starts out with random values for all particles. 
Press 'q' to exit. 
Windows may show warning message saying "Windows protected your PC", in this case, click on 'more info' and 'run anyway'. 
Its safe, don't worry :)
