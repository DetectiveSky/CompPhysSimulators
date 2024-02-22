#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:41:04 2020

This is a skeleton code to solve the bike racing problem described in 
Sec. 2.1 of Giordano and Nakanishi.

@author: atkinson

Adapted for Assignment 2 on Thursday, Feb. 6, 2020 by David Stothers
"""
import numpy as np
from matplotlib import pyplot as plt

# Define important variables
m = 80  # Mass of the rider [kg]
rho = 1.29  # density of air [kg/m^3]

t_init = 0.0    # starting time of the simulation [s]
t_final = 200.0 # end time of the simulation [s]
N = 4001 # Number of time steps
t_list = np.linspace(t_init, t_final, N) # times at which we calculate v
dt = t_list[1] - t_list[0]  # time step

g = -9.81 #gravitational acceleration

# Values below obtained from G&N
P=400
C=1
A=0.33
dragconst = -(rho/2.0)*C*A

theta = 0.0 #the angle in degrees of the relevant slope

v=np.arange(N+1,dtype=float)
v[0]=4.0

F=np.arange(N,dtype=float)
Fdrag=np.arange(N,dtype=float)
Fg = float(float(m*g)*np.sin(float((theta*np.pi)/180.0))) #the force on the motion due to gravity

# Main loop
# This loop has problems that you will fix in the lab
#for i, t in enumerate(t_list):
for i in range(N):
    print(i, t_list[i])
    Fdrag[i] = dragconst*(v[i]**2) # calculate drag
    
    #Edited to account for gravity
    F[i] = (P/v[i])+Fdrag[i]+Fg #calculate net force
    
    v[i+1] = v[i]+((F[i]/m))*dt #calculate next interval's velocity

theta = float(np.arctan(0.1)) #the angle in radians of the relevant slope
Fg = float(float(m*g)*np.sin(theta)) #the force on the motion due to gravity
v2=np.arange(N+1,dtype=float)
v2[0]=4.0
F=np.arange(N,dtype=float)
Fdrag=np.arange(N,dtype=float)

for i in range(N):
    print(i, t_list[i])
    Fdrag[i] = dragconst*(v2[i]**2) # calculate drag
    
    #Edited to account for gravity
    F[i] = (P/v2[i])+Fdrag[i]+Fg #calculate net force
    
    v2[i+1] = v2[i]+((F[i]/m))*dt #calculate next interval's velocity

# Output results
plt.figure(0)
plt.clf()
plt.xlabel('time (s)')
plt.ylabel('speed (m/s)')
plt.title('Speed vs. time for a professional cyclist')

v=v[:-1]
v2=v2[:-1]

plt.plot(t_list,v,'go-', linewidth=1, markersize=2,label="Level Ground")
plt.plot(t_list,v2,'bo-', linewidth=1, markersize=2,label="10% Grade")

plt.legend()
plt.show()