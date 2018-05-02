from order_statistic_functions import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.integrate import quad

#################
# Parameters	#
#################

# Input
N =1000
u = 3
mu = 0.001
delay = 1000

# Output
n = 375
k = 192
K = 2
q = 1


#################
# PDF Overall 	#
#################

# Nonzero time
tlow = delay/(q*(k-u))
tup = 10*(delay/((k-u)*q) + 1/((k-u)*q*mu))
t = np.linspace(tlow, tup,2000)

pdfEval = [0]*t.size		# Allocate memory

for i in range(1,t.size):	# Evaluate integrand
	#pdfEval[i] = t[i]*pdf_overall(t[i],n,k,K,q,mu*(k-u),delay*1./(k-u))	# Expected waiting time
	pdfEval[i] = pdf_overall(t[i],n,k,K,q,mu*(k-u),delay*1./(k-u))


print(simps(pdfEval,t))	# Calculate integraql over pdf
print(quad(lambda x: 1*pdf_overall(x,n,k,K,q,mu*(k-u),delay*1./(k-u)),tlow,tup))
plt.plot(t,pdfEval)	# plot pdf


#################
# PDF in group 	#
#################

# Adjust runtime distrbution 
delay *= 1./(k-u)
mu *= (k-u)
# Nonzero time
#t = np.linspace(delay/q, delay + q*(K-q+10)*5./(q*K*mu*(K-q+1)),200)
#t = np.linspace(delay/q, delay + 1/mu,200)

plt.plot(t,pdf_q_order_statistic_in_group(t,q,K,mu,delay))	# Plot PDF
print(simps(pdf_q_order_statistic_in_group(t,q,K,mu,delay),t))


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



