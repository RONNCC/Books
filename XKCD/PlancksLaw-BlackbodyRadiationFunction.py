import numpy as np
import matplotlib.pyplot as mp
"""
 B_l(t) = (2*h*c^2/l^5)*(1/(e^(h*c/(l*k_b*t))-1))
 t = absolute temperature, v = frequency
 fv=c
 h = planck's constant, k_b = Boltzmann Constant
"""
h=6.26*10**-34
c=299792458
k_b=1.381*10**(-23)
l_num = 20000000; l_min = 5*10**(-8); l_max = 3*10**(-6); lspace = np.linspace(l_min,l_max,l_num);
trange=np.linspace(1000,20000,10)
B_l = np.vectorize(lambda t,l: 2*h*c**2/l**5 *1./(np.exp((h*c)/(l*k_b*t))-1) )
[mp.plot(lspace,B_l(t,lspace)) for t in trange]
mp.show()
#print a
