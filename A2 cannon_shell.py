# Import useful libraries
import numpy as np
from matplotlib import pyplot as plt

"""
Docstring goes here:
"""


def trajectory(g, B2_over_m, v0, theta, x0, y0):
    """
    The docstring for the function should tell you what the function does,
    what the input variables mean, and what the output variables mean.
    
    Input:
        g - the gravitational acceleration, taken to be positive pointing down
        B2_over_m - the drag constant translating speed-squared to acceleration, taken to be positive pointing down
        v0 - the magnitude of the initial velocity
        theta - the launch angle in radians, taken to be 0 level to the ground and increasing upwards
        x0 - the initial x position, taken to be positive pointing forwards
        y0 - the initial y position, taken to be positive pointing up
        
    Output:
        x - an array of the different x values found.
        y - an array of the different y values found.
        vx - an array of the different vx values found.
        vy - an array of the different vy values found.
        t - an array of the different t values found.
        x_range - the maximum distance the shell flies.
    """
    
    # estimated maximum time of flight for the shell, plus a little extra
    tmax_est = 180
    # Number of time steps
    N = 1001
    t = np.linspace(0, tmax_est, N, dtype=np.float)
    dt = t[1] - t[0]
    
    # define the position and velocity arrays and set their initial values
    x = np.arange(0,N,dtype=float)
    y=np.arange(0,N,dtype=float)
    vx=np.arange(0,N,dtype=float)
    vy=np.arange(0,N,dtype=float)
    v = np.arange(0,N,dtype=float)

    x[0]=x0
    y[0]=y0
    vx[0]=v0*np.cos(theta)
    vy[0]=v0*np.sin(theta)
    v[0]=v0
    
    anety = np.arange(0,N,dtype=float)
    adragy = np.arange(0,N,dtype=float) # Drag taken to be positive opposing motion
    adragx = np.arange(0,N,dtype=float)

    # iterate over times
    has_landed = False
    for i0 in np.arange(N-1):
        # calculate the position and velocity versus time here
        v[i0]=np.sqrt((vx[i0]**2) + (vy[i0]**2))
        adragy[i0] = B2_over_m*vy[i0]*v[i0]
        adragx[i0] = B2_over_m*vx[i0]*v[i0]
        anety[i0]=g+adragy[i0]
        
        vx[i0+1]=vx[i0]-(adragx[i0]*dt)
        vy[i0+1]=vy[i0]-(anety[i0]*dt)
        
        x[i0+1]=x[i0]+(vx[i0]*dt)
        y[i0+1]=y[i0]+(vy[i0]*dt)
        
        if y[i0] < 0.0:
            has_landed = True
            break

    if not(has_landed):
        print("Error:  simulation is not long enough")

    # calculate the range of the shell using interpolation
    x_range = x[i0]

    # Now return only the portion of the arrays we care about.
    return x[:i0], y[:i0], vx[:i0], vy[:i0], t[:i0], x_range


#
# Now start the main part of the program.
#
# First define constants:
v0 = 700  # initial speed in m/s
B2_over_m = 4e-5  # prefactor for the drag force in m^{-1}
g = 9.80  # gravitational acceleration in m/s^2

# No air resistance
theta1 = np.pi/4
x1, y1, vx1, vy1, t1, x1_range = trajectory(g, B2_over_m, v0, theta1, 0., 0.)
plt.figure(0)
plt.clf()
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Trajectory of a Cannon Shot (With Drag)")
plt.plot(x1, y1, 'b', label='v0 = 700, range = '+str(x1_range))
plt.legend()
print('range at theta = pi/4:  ', x1_range)
plt.show()

B2_over_m = 0*4e-5

x1, y1, vx1, vy1, t1, x1_range = trajectory(g, B2_over_m, v0, theta1, 0., 0.)
plt.figure(1)
plt.clf()
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Trajectory of a Cannon Shot (No Drag)")
plt.plot(x1, y1, 'b', label='v0 = 700, range = '+str(x1_range))
plt.legend()
print('range at theta = pi/4:  ', x1_range)
plt.show()

