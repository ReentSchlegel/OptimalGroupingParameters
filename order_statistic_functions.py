import math
from scipy.special import comb
from scipy.integrate import quad

def pdf_runtime_worker(t,mu,delay=1):
	# Input:
	#
	# t 	: time
	# mu	: straggling parameter
	# delay : time delay, default = 1
	#
	# Output:
	#
	# pdf of the runtime of one worker
	return mu*math.e**(-mu*(t-delay))

def cdf_runtime_worker(t,mu,delay=1):
	# Input:
	#
	# t 	: time
	# mu	: straggling parameter
	# delay : time delay, default = 1
	#
	# Output:
	#
	# cdf of the runtime of one worker
	return 1-math.e**(-mu*(t-delay))

def pdf_q_order_statistic_in_group(t,q,K,mu,delay=1):
	# Input:
	
	# t 	: time
	# q 	: qth order statistic
	# K 	: number of workers in a group
	# mu	: straggling parameter
	# delay : time delay, default = 1
	#
	# Output:
	#
	# pdf of the qth fastest worker out of K workers in one group
	return K*comb(K-1,q-1)*cdf_runtime_worker(t,mu,delay)**(q-1)*(1-cdf_runtime_worker(t,mu,delay))**(K-q)*pdf_runtime_worker(t,mu,delay)

def cdf_q_order_statistic_in_group(t,q,K,mu,delay=1):
	# Input:
	
	# t 	: time
	# q 	: qth order statistic
	# K 	: number of workers in a group
	# mu	: straggling parameter
	# delay : time delay, default = 1
	#
	# Output:
	#
	# cdf of the qth fastest worker out of K workers in one group
	cdf, precision = quad(pdf_q_order_statistic_in_group,delay,t,args=(q,K,mu,delay))
	return cdf

def pdf_overall(t,n,k,K,q,mu,delay=1):
	return n*comb(n-1,k-1)*cdf_q_order_statistic_in_group(t,q,K,mu,delay)**(k-1)*(1-cdf_q_order_statistic_in_group(t,q,K,mu,delay))**(n-k)*pdf_q_order_statistic_in_group(t,q,K,mu,delay)