#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:05:17 2020

@author: davidstothers
"""

#plotting theta vs Fd using the Verlet algorithm to simulate the pendulum

import a5lib as a5
import numpy as np
import matplotlib.pyplot as plt

global g

g = 9.81
m = 1.0
L = g

dfreq = 2*np.sqrt(1.0)/3
dperiod = (2*np.pi)/dfreq
q = 0.5
inittheta=0.2

damp = np.linspace(1.35,1.5,num=150+1,dtype=float)

plt.figure(0)
plt.clf()
plt.title("Bifurcation Diagram of a Verlet Pendulum")
plt.xlabel("Driving Force Amplitude")
plt.ylabel("Angle (radians)")
print("Beginning simulations...")

for i in np.arange(damp.size):
    print("("+str(i+1)+"/"+str(damp.size)+")")
    t,th,o = a5.pendulum_verlet(L,theta0v=inittheta,forceqv=q,\
                                drivefreqv=dfreq,driveampv=damp[i])
    sth = a5.strobe_theta(th,t,dperiod)
    plotx = np.full(sth.size,damp[i])
    plt.plot(plotx,sth,'bo')

plt.show()
print("Simulations complete!")