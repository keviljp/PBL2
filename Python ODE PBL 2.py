from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import optimize
from scipy import interpolate
import pandas as pd

def odes (x, t):
    #constants
    #c =  10.09e-4 
    c =  7.4e-4#kg/m
    m = .025 #kg
    g = 9.81
    X = 0
    
    # assign each ODE to a vector element
    Vx = x[0]
    Vy = x[1]
    Y = x[2]

    #define each ODE
    dVxdt = -((c*Vx)/m)*np.sqrt(Vx**2+Vy**2)
    dVydt = -g-((c*Vy)/m)*np.sqrt(Vx**2+Vy**2)
    dYdt = Vy
    
    return[dVxdt, dVydt, dYdt]

#define initial conditions for ODEs
x0 = [14.61, 3.812, 2.01]

# test defined ODEs
#print(odes(x=x0,t=0))

#declare a time vecotr
t = np.linspace(0,1.25,1000)
x = odeint(odes,x0,t)

Vx = x[:,0]
Vy = x[:,1]
Y = x[:,2]
X = np.arange(0, 1000)
F = np.arange(0, 1000)

#plot the results
plt.title('X Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('X Velocity (m/s)')
plt.plot(t, Vx)
plt.show()


plt.title('Y Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Y Velocity (m/s)')
plt.plot(t, Vy)
plt.show()


plt.xlim(0, 1.3) 
plt.ylim(0, 3) 
plt.title('Y Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Y Position (m)')
plt.plot(t, Y)
#plt.axhline(y=0, color='r', linestyle='-')
plt.show()

x = Vx*t

plt.xlim(0, 12) 
plt.ylim(0, 3) 
plt.title('Y Position vs. X Position')
plt.xlabel('X position (m)')
plt.ylabel('Y Position (m)')
#plt.axhline(y=0, color='r', linestyle='-')
plt.plot(x, Y)
plt.show()

f = interpolate.interp1d (t, Y)
y = interpolate.interp1d (t, Vy)
root = optimize.newton(f,1.2, y)
print(root)
