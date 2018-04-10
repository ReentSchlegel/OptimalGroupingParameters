from order_statistic_functions import pdf_overall
import matplotlib.pyplot as plt
import numpy as np



n = 100
k = 1
u = 0
mu = 10**(0)
q = 7
K = 10


t = np.linspace(1./(k-u), (k+10)*(n-k+10)*5./((k-u)*n*mu*(n-k+1))+1./(k-u),500)
cdf = np.zeros(t.size)
for i in range(t.size):
	cdf[i] = t[i]*(k-u)*pdf_overall((k-u)*t[i],n,k,K,q,mu)


plt.plot(t,cdf)
plt.show()

