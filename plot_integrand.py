from order_statistic_functions import *
import matplotlib.pyplot as plt
import numpy as np



n = 50
k = 50
u = 3
mu = 10**(0)
q = 1
K = 2
delay = 1

delay *= 1/(k-u)
mu *= (k-u)


#t = np.linspace(delay,delay + 7*q/(K*mu),200)


t = np.linspace(delay,delay + 1*q/(K*mu),200)



pdfEval = [0]*t.size
for i in range(t.size):
	pdfEval[i] = t[i]*pdf_overall(t[i],n,k,K,q,mu*(k-u),delay)
#cdf = pdf_q_order_statistic_in_group(t,q,K,mu,delay)
#for i in range(t.size):
#	cdf[i] = cdf_q_order_statistic_in_group(t[i]*(k-u),q,K,mu,delay=1)
print(pdfEval)

plt.plot(t,pdfEval)
plt.show()

