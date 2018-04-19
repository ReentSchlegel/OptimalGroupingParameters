from order_statistic_functions import pdf_q_order_statistic_in_group
from scipy.integrate import simps
import numpy as np


def find_optimal_rate(K,mu,rs,delay = 1):
	'''Input:
	
	K 		: code length (number of workers in the grpup)
	mu		: straggling parameter of one worker performing the whole task for the group
	rs		: dimension of matrix assigned to the group
	delay	: delay of one worker performing the whole task assigned to the group  
	
	Output:
	code dimension q (q/K is optimal code rate)'''

	K = int(K)					# Change data type
	
	T = [np.inf]*K					# Allocate memory


	# Define a function for the integrand
	def expected_value_function(t,q):
		return t*pdf_q_order_statistic_in_group(t,q,K,mu,delay)				# Integrand is t*pdf(t)


	for q in range(1,K+1):	# For all k in the range of u < k <= n
		t = np.linspace(delay, delay + q*(K-q+10)*5./(q*K*mu*(K-q+1)),200)	# Define 200 evaluation points where the integrand is not zero
		if q == K:			# No decoding needed
			T[q-1] = simps(expected_value_function(t,q),t) 					# Integrate over expected_value_function
		else:				# With decoding
			#T[q-1] = simps(expected_value_function(t,q),t)*(1 + ((K**2*(K-q-1)*q)/(rs*q)))	# Integrate over expected_value_function + decoding time
			T[q-1] = simps(expected_value_function(t,q),t)

	Topt = min(T)			# Optimal expected waiting time
	q = T.index(Topt) + 1	# Code dimension corresponding to Topt 
	return q 				# Return optimal code dimension


