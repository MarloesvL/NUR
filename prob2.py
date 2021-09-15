import numpy as np 
import matplotlib.pyplot as plt
from numpy import random
import time

facs = [1.]

for i in np.arange(1,1000):
	facs.append(facs[-1]*i)

def sinc(x):
	return np.sin(x)/x

def sinc_ps(x,n):
	n_list = np.arange(0,n)
	sinc = [1.]*len(x) ; mp = -1 ; n2 = 2*(n_list+1)
	for n in n_list:
		sinc += mp*x**n2[n]/facs[int(n2[n]+1)]
		mp *= -1
	return np.array(sinc)#,dtype=np.float32)

def err(x,n):
	return(sinc(x)-sinc_ps([x],n)[0])

m = np.random.normal(10**6,10**5,1000.)
c=3*10**5 #kms
g = 4.3*10**-3 #pc kms2 M_sun
c2=1./(c*c)

start = time.time()
rs = 2*g*m/c2
print(time.time()-start)
