import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 


def sir(initial_values, t, a,b):

    s,i,r = initial_values

    dsdt = -a*s*i
    didt = a*s*i - b*i
    drdt = b*i
    return [dsdt, didt, drdt]


ndays = 500
initial_values = [1000,5,0]
a,b = [0.0001,0.02]
t = np.linspace(0, ndays, ndays)

final_values = odeint(sir, initial_values, t, args=(a,b))
temp = [0]*ndays
susceptible = final_values[:,0]
infected = final_values[:,1]
recovered = final_values[:,2]

plt.plot(t,susceptible, label='susceptible')
plt.plot(t,infected, label='infected')
plt.plot(t,recovered, label='recovered')
plt.plot(t,temp, label='Zero Line')
plt.grid()
plt.legend()
plt.show()