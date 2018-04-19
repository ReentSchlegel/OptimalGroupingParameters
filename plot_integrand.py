from order_statistic_functions import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.integrate import quad

#################
# Parameters	#
#################

# Input
N = 10
u = 3
mu = 0.1
delay = 10

# Output
n = 5
k = 5
K = 2
q = 2


#################
# PDF Overall 	#
#################

# Nonzero time
t = np.linspace(delay*1./(k-u),delay*1./(k-u) + q*7./(K*mu*(k-u)),200)

pdfEval = [0]*t.size		# Allocate memory

for i in range(1,t.size):	# Evaluate integrand
	pdfEval[i] = t[i]*pdf_overall(t[i],n,k,K,q,mu*(k-u),delay*1./(k-u))


print(simps(pdfEval,t))	# Calculate and print expected waiting time
plt.plot(t[1:-2],pdfEval[1:-2])	# plot pdf


#################
# PDF in group 	#
#################

# Adjust runtime distrbution 
delay *= 1./(k-u)
mu *= (k-u)

# Nonzero time
t = np.linspace(delay, delay + q*(K-q+10)*5./(q*K*mu*(K-q+1)),200)

plt.plot(t,pdf_q_order_statistic_in_group(t,q,K,mu,delay))	# Plot PDF


#################
# CDF in group 	#
#################

cdfEval = [0]*t.size		# Allocate memory

for i in range(1,t.size):	# Evaluate CDF
	cdfEval[i] = cdf_q_order_statistic_in_group(t[i],q,K,mu,delay)

plt.plot(t,cdfEval)			# Plot CDF


#################
# Show plot 	#
#################

plt.show()



