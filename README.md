# gravity_simulator
# Author -Vedang Ratnaparkhi

Newtonian gravity for n particles in a system.
Calculated by grid simulation method and vector operations.

The math used is newton's gravitational vector formula differentiated with time.
Runs a loop per dt to calculate forces and consequently the position change.

Of course the simulation cannot be infinitely accurate since i can only calculate for a finite dt, but the variable dt can be changed for more accuracy.
(Default dt = 1/30)