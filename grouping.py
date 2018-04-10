import numpy as np
from optimal_rates import find_optimal_rate
from order_statistic_functions import pdf_overall
from scipy.integrate import simps


def find_divisors(n):
	# hj
	out = []
	for i in range(1,int(n/2)+1):
		if n%i == 0:
			out += [i]
	out += [n]
	return out

def find_grouping(N,u,mu,rs):
	div = np.array(find_divisors(N))
	div = div[u<div]
	ToptOverall = [0]*len(div)
	qOverall = [0]*len(div)
	for n in div:
		K = N/n 	# Number of workers per group
		q, dummy = find_optimal_rate(K,0,mu,rs,n)	# Numer of servers to wait for in group




		T = [0]*(n-u-1)				# Allocate memory


		# Define a function for the integrand
		def expected_value_function(t,k):
			return t*(k-u)*pdf_overall(t*(k-u),n,k,K,q,mu)				# Integrand is t*pdf(t), where t -> (k-u)*t


		for k in range(u+1,n+1):		# For all k in the range of u < k <= n
			t = np.linspace(1./(k-u), k*(n-k+10)*5./((k-u)*n*mu*(n-k+1))+1./(k-u),200)	# Define 200 evaluation points where the integrand is not zero 
			T[k-u-1] = simps(expected_value_function(t,k),t)*(1 + ((n**2*(n-k-1)*(k-u))/(rs*k)))	# Integrate over expected_value_function + decoding time
		
		Topt = min(T)				# Optimal expected waiting time
		k = T.index(Topt) + u + 1	# Code dimension corresponding to Topt 


	return

find_grouping(100,3,1,200)