import numpy as np
from optimal_rates import find_optimal_rate
from order_statistic_functions import pdf_overall
from scipy.integrate import simps


def find_divisors(n):
	'''Find all divisors of n
	
	Input:
	
	n 	: number of which the divisors shall be found
	
	Output:
	
	List of all divisors'''


	out = []	# Initialize list

	for i in range(1,int(n/2)+1):	# For all possible divisors except n
		if n%i == 0:				# If modulus of n/i is zero
			out += [int(i)]			# add i to the list

	out += [int(n)]					# Include n as divisor

	return out 						# Return the list

def find_grouping(N,u,mu,delay,rs):
	'''Find the optimal grouping scheme
	
	Input:
	
	N 		: number of workers
	u 		: number of colluding service providers
	mu 		: straggling parameter of one worker performing the whole task
	delay	: delay of one worker performing the whole task
	rs 		: number of entries in A
	
	Output (n,k,q,t):
	
	n 	: number of groups
	k 	: code dimension over the groups
	q 	: code dimension in the groups
	T 	: expected runtime'''

	# Type conversion
	u = int(u)
	N = int(N)

	# Allocate memory
	Topt = []
	kopt = []
	qOverall = []

	div = np.array(find_divisors(N))	# Find the divisors of N (possible numbers of groups)
	div = div[u<div]					# Keep feasible number of groups (those that are more than u)
	

	for n in div:		# For all numbers of groups
		K = N/n 		# Number of workers per group
		
		# Allocate memory
		T = [np.inf]*(n-u)				
		q = [0]*(n-u)


		for k in range(u+1,n+1):		# For all code dimensions over the groups
			q[k-u-1] = find_optimal_rate(K,mu*(k-u),rs*1./(k-u),delay*1./(k-u))	# Numer of servers to wait for in group
			t = np.linspace(delay*1./(k-u),delay*1./(k-u) + q[k-u-1]*7./(K*mu*(k-u)),200)		# Define 200 evaluation points where the integrand is not zero
			pdfEval = [0]*t.size
			for i in range(1,t.size):
				pdfEval[i] = t[i]*pdf_overall(t[i],n,k,K,q[k-u-1],mu*(k-u),delay*1./(k-u))
			if k == n:
				T[k-u-1] = simps(pdfEval,t)
			else:
				#T[k-u-1] = simps(pdfEval,t)*(1 + ((n**2*(n-k-1)*(k-u))/(rs*k)))	# Integrate over expected_value_function + decoding time
				T[k-u-1] = simps(pdfEval,t)
		Topt += [min(T)]				# Optimal expected waiting time
		kopt += [T.index(Topt[-1]) + u + 1]	# Code dimension corresponding to Topt
		qOverall += [q[T.index(Topt[-1])]]
	ToptOverall = min(Topt)
	koptOverall = kopt[Topt.index(ToptOverall)]
	qopt = qOverall[Topt.index(ToptOverall)]
	nopt = div[Topt.index(ToptOverall)]


	return nopt, koptOverall, qopt, ToptOverall
