import matplotlib.pyplot as plt
import numpy as np
import math
g = 2 * math.pi * np.arange(1000, 100000000, 10000)
z = np.linspace(0.0002, 1, 4)
perm_of_free_space = (8.85418782 * pow(10, -12))

perm_of_medium = 80 * perm_of_free_space


perm_of_particle = 2.33 * perm_of_free_space 
con_of_particle = (0.053)

for i in z:
    
    con_of_medium = i
   
    #The complex permittivity of particle is found by the formula below
    complex_perm_of_medium = ((perm_of_medium) - 1j*(con_of_medium/g))

    #The complex permittivity of particle is found by the formula below
    complex_perm_of_particle =  ((perm_of_particle) - 1j*(con_of_particle/g))
                                         
    
    #The Clausius Mossoti Factor is determined by the following formula
    cm_factor = (complex_perm_of_particle - complex_perm_of_medium)/(complex_perm_of_particle + (2*complex_perm_of_medium))
    
    cm_factor_real = [x.real for x in cm_factor]
    cm_factor_imag = [y.imag for y in cm_factor]
    
    if i==z[0]:
        try:
            zero_val_index=cm_factor_real.index(min(map(abs,cm_factor_real)))
        except:
            zero_val_index=cm_factor_real.index(-1*min(map(abs,cm_factor_real)))
    crossover=g[zero_val_index]
        
    print(complex_perm_of_particle - complex_perm_of_medium)
    plt.xscale('log')
    
    #plt.plot(g,cm_factor_imag)
    plt.plot(g,cm_factor_real)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Re(CMF[ω]")
    #plt.show()
plt.plot([crossover]*50,np.linspace(-0.9,1,50),linestyle='--')
legend=["{} S/m".format(i) for i in z]
legend.append("Crossover Frequency: {} MHz".format(round(crossover/1000000,7)))
plt.legend(legend)
plt.grid(color='r', linestyle='--', linewidth=0.3)
print("The Crossover Frequency is",crossover/1000000,"MHz")
