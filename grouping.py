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
		




		T = [0]*(n-u)				# Allocate memory


		for k in range(u+1,n+1):		# For all k in the range of u < k <= n
			delay = 1/(k-u)
			q, dummy = find_optimal_rate(K,0,mu*(k-u),rs/(k-u),delay)	# Numer of servers to wait for in group
			t = np.linspace(delay,delay + 7*q/(K*mu*(k-u)),200)	# Define 200 evaluation points where the integrand is not zero
			pdfEval = [0]*(t.size-1)
			for i in range(1,t.size):
				pdfEval[i-1] = t[i]*pdf_overall(t[i],n,k,K,q,mu*(k-u),delay)
			T[k-u-1] = simps(pdfEval,t[1:])*(1 + ((n**2*(n-k-1)*(k-u))/(rs*k)))	# Integrate over expected_value_function + decoding time
		Topt = min(T)				# Optimal expected waiting time
		k = T.index(Topt) + u + 1	# Code dimension corresponding to Topt
		print(Topt,k,n)


	return

find_grouping(100,3,1,200)