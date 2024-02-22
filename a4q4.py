#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:11:46 2020

COIS 2310H Assignment 3 Question 4

@author: davidstothers
"""

import q4lib
import numpy as np
import matplotlib.pyplot as plt

N=15001

t = np.linspace(0,100,N)
m=1
L=9.81

theta01=0.2
theta02=0.2

th1,o1 = q4lib.pendulum_EC(t,mass=m,Length=L,forceq=0.5,driveamp=1.4,theta0=theta01,drivefreq=2.0/3)
th2,o2 = q4lib.pendulum_EC(t,mass=m,Length=L,forceq=0.5,driveamp=1.5,theta0=theta02,drivefreq=2.0/3)

plt.figure(0)
plt.clf()
plt.plot(th1,o1,'b',label="FD = 1.4")
plt.plot(th2,o2,'g',label="FD = 1.5")
plt.title("Speed Vs. Angle of Two Chaotic Pendulums")
plt.xlabel("Angle (rad)")
plt.ylabel("Speed (rad/s)")
plt.legend()
plt.show()

plt.figure(1)
plt.clf()
plt.plot(t,th1,'b',label="FD = 1.4")
plt.plot(t,th2,'g',label="FD = 1.5")
plt.title("Angle Vs. Time of Two Chaotic Pendulums")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.show()

plt.figure(2)
plt.clf()
dth = np.abs(th2[:]-th1[:])
plt.plot(t,dth,'b')
plt.title('dtheta vs t')

print(str(np.argmax(q4lib.lyapunov(t[2:],th1[2:],th2[2:]))))