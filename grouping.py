import numpy as np
from optimal_rates import find_optimal_rate
from order_statistic_functions import pdf_overall
from scipy.integrate import simps
from scipy.integrate import quad


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

def find_grouping(N,u,mu,delay,rs,app):
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

	app.setMeter("Progress",0)			# Initialize progress meter

	# Type conversion
	u = int(u)
	N = int(N)

	# Allocate memory
	Topt = []
	kopt = []
	qOverall = []

	# Obtain numbers of groups
	div = np.array(find_divisors(N))	# Find the divisors of N (possible numbers of groups)
	div = div[u<div]					# Keep feasible number of groups (those that are more than u)
	
	# Calculate the total number of loops for progress update
	totalLoops = 0		# Initialize total number of loops
	loop = 0			# Initialize loop counter
	for n in div:		# For all numbers of groups n
		totalLoops += n-u	# n-u loops have to be evaluated

	# Search for optimum
	for n in div:		# For all numbers of groups
		K = N/n 		# Number of workers per group
		
		# Allocate memory
		T = [np.inf]*(n-u)				
		q = [0]*(n-u)


		for k in range(u+1,n+1):		# For all code dimensions over the groups
			q[k-u-1] = find_optimal_rate(K,mu*(k-u),rs*1./(k-u),delay*1./(k-u))	# Numer of servers to wait for in group
			# Expected waiting time and accuracy
			T[k-u-1], dummy = quad(lambda t: t*pdf_overall(t,n,k,K,q[k-u-1],mu*(k-u),delay*1./(k-u)),delay/(q[k-u-1]*(k-u)),np.inf)
			if k < n: 	# Decoding is needed (No decoding for k == n)
				T[k-u-1] *= (1 + ((n**2*(n-k-1)*(k-u))/(rs*k)))	# Add decoding time
			
			loop += 1 	# Update loop counter
			app.setMeter("Progress",100*loop/totalLoops)	# Update progress meter

			
		Topt += [min(T)]					# local optimal expected waiting time
		kopt += [T.index(Topt[-1]) + u + 1]	# Code dimension over groups corresponding to Topt
		qOverall += [q[T.index(Topt[-1])]]	# Code dimension in groups corresponding to Topt
	ToptOverall = min(Topt)						# Global optimal expected waiting time
	koptOverall = kopt[Topt.index(ToptOverall)]	# Corresponding code dimension over groups
	qopt = qOverall[Topt.index(ToptOverall)]	# Corresponding code dimension in groups
	nopt = div[Topt.index(ToptOverall)]			# Corresponding code length over groups

	


	return nopt, koptOverall, qopt, ToptOverall
