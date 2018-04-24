from order_statistic_functions import pdf_q_order_statistic_in_group
from scipy.integrate import quad
import numpy as np


def find_optimal_rate(K,mu,r,s,p,delay = 1):
	'''Input:
	
	K 		: code length (number of workers in the grpup)
	mu		: straggling parameter of one worker performing the whole task for the group
	r		: number of rows in Matrix assigned to group
	s		: number of columns in Matrix assigned to group
	p 		: number of bits per number (2^p is the field size)
	delay	: delay of one worker performing the whole task assigned to the group  
	
	Output:
	code dimension q (q/K is optimal code rate)'''

	K = int(K)					# Change data type
	
	T = [np.inf]*K				# Allocate memory


	for q in range(1,K+1):	# For all q in the range of 0 < q <= K
		# Integrate over expected_value_function (t*pdf(t))
		T[q-1], dummy = quad(lambda t: t*pdf_q_order_statistic_in_group(t,q,K,mu,delay),delay/q,np.inf)
		if q < K:			# With decoding (no decoding for q == K)
			T[q-1] += K*((K-q-1)*np.log(p)+K-q)*(delay+1/mu)/(r*(s*np.log(p)+s-1))	# Add decoding time

	Topt = min(T)			# Optimal expected waiting time
	q = T.index(Topt) + 1	# Code dimension corresponding to Topt 
	return q 				# Return optimal code dimension


