import matplotlib.pyplot as plt
import numpy as np
import math
g = 2 * math.pi * np.arange(1000, 10000000, 10000)
z = np.linspace(0.0002, 1, 20)
perm_of_free_space = (8.85418782 * pow(10, -12))

perm_of_medium = 80 * perm_of_free_space


perm_of_particle = 2.56 * perm_of_free_space 
con_of_particle = (7 *  pow(10, -5))

for i in z:
    
    con_of_medium = i
   
    #The complex permittivity of particle is found by the formula below
    complex_perm_of_medium = ((perm_of_medium) - 1j*(con_of_medium/g))

    #The complex permittivity of particle is found by the formula below
    complex_perm_of_particle =  ((perm_of_particle) - 1j*(con_of_particle/g))
                                         
    
    #The Clausius Mossoti Factor is determined by the following formula
    cm_factor = (complex_perm_of_particle - complex_perm_of_medium)/(complex_perm_of_particle + (2*complex_perm_of_medium))
    
    x_axis = [x.real for x in cm_factor]
    y_axis = [y.imag for y in cm_factor]
    
    print(complex_perm_of_particle - complex_perm_of_medium)
    plt.xscale('log')
    
    #plt.plot(g,y_axis)
    plt.plot(g,x_axis)
    plt.xlabel("Frequency")
    plt.ylabel("CM Factor")
    #plt.show()