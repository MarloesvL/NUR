import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import time

facs = [1.]

#for i in np.arange(1,1000):
#	facs.append(facs[-1]*i)

def sinc(x):
	return np.sin(x)/x

def sinc_ps(x,n):
	n_list = np.arange(0,n)
	sinc = [1.]*len(x) ; mp = -1 ; n2 = 2*(n_list+1)
	for n in n_list:
		sinc += mp*x**n2[n]/facs[int(n2[n]+1)]
		mp *= -1
	return np.array(sinc)#,dtype=np.float32)

x = np.linspace(0.1,6.,1000)
plt.figure()

plt.plot(x,sinc_ps(x,2),label='sinc_ps, 2')
plt.plot(x,sinc_ps(x,3),label='sinc_ps, 3')
plt.plot(x,sinc_ps(x,5),label='sinc_ps, 5')
plt.plot(x,sinc_ps(x,7),label='sinc_ps, 7')
plt.plot(x,sinc(x),label='sinc')
plt.legend()
plt.ylim(-0.5,1.)
plt.savefig('1a.pdf')
