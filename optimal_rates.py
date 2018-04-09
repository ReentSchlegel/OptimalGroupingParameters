from order_statistic_functions import pdf_q_order_statistic_in_group
from scipy.integrate import simps
import numpy as np


def find_optimal_rate(n,u,mu,rs):
	# Input:
	#
	# n 	: code length
	# u 	: security level
	# mu	: straggling parameter
	# rs	: dimension of A  
	#
	# Output (k,Topt):
	# k 	: code dimension (k/n is optimal coderate)
	# Topt	: optimal expected waiting time

	u = int(u)					# Change data type
	n = int(n)					# Change data type
	
	T = [0]*(n-u-1)				# Allocate memory


	# Define a function for the integrand
	def expected_value_function(t,k):
		return t*(k-u)*pdf_q_order_statistic_in_group((k-u)*t,k,n,mu)				# Integrand is t*pdf(t), where t -> (k-u)*t


	for k in range(u+1,n):		# For all k in the range of u < k < n
		t = np.linspace(1./(k-u), k*(n-k+10)*5./((k-u)*n*mu*(n-k+1))+1./(k-u),200)	# Define 200 evaluation points where the integrand is not zero 
		T[k-u-1] = simps(expected_value_function(t,k),t)*(1 + ((n**2*(n-k-1)*(k-u))/(rs*k)))	# Integrate over expected_value_function + decoding time
	
	Topt = min(T)				# Optimal expected waiting time
	k = T.index(Topt) + u + 1	# Code dimension corresponding to Topt 
	return (k,Topt)


