import math
import numpy as np
from scipy.special import comb
from scipy.integrate import simps

def pdf_runtime_worker(t,mu,delay=1):
	'''Input:
	
	t 		: time
	mu		: straggling parameter of one worker performing the whole task assigned to the group
	delay 	: time delay of one worker performing the whole task assigned to the group, default = 1
	
	Output:
	
	pdf of the runtime of one worker'''

	return mu*math.e**(-mu*(t-delay))

def cdf_runtime_worker(t,mu,delay=1):
	'''Input:
	
	t 	: time
	mu	: straggling parameter of one worker performing the whole task assigned to the group
	delay : time delay of one worker performing the whole task assigned to the group, default = 1
	
	Output:
	
	cdf of the runtime of one worker'''
	
	return 1-math.e**(-mu*(t-delay))

def pdf_q_order_statistic_in_group(t,q,K,mu,delay=1):
	'''Input:
	
	t 	: time
	q 	: qth order statistic
	K 	: number of workers in a group
	mu	: straggling parameter of one worker performing the whole task assigned to the group
	delay : time delay of one worker performing the whole task assigned to the group, default = 1
	
	Output:
	
	pdf of the runtime of the qth fastest worker out of K workers in one group'''
	mu *= q
	delay /= q
	return K*comb(K-1,q-1)*cdf_runtime_worker(t,mu,delay)**(q-1)*(1-cdf_runtime_worker(t,mu,delay))**(K-q)*pdf_runtime_worker(t,mu,delay)

def cdf_q_order_statistic_in_group(t,q,K,mu,delay=1):
	'''Input:
	
	t 	: time
	q 	: qth order statistic
	K 	: number of workers in a group
	mu	: straggling parameter of one worker performing the whole task assigned to the group
	delay : time delay of one worker performing the whole task assigned to the group, default = 1
	
	Output:
	
	cdf of the runtime of the qth fastest worker out of K workers in one group'''
	tau = np.linspace(delay,t,200)
	return simps(pdf_q_order_statistic_in_group(tau,q,K,mu,delay),tau)

def pdf_overall(t,n,k,K,q,mu,delay=1):
	'''Input:
	
	t 		: time
	n 		: number of groups
	k 		: number of groups to wait for (code dimension)
	K 		: number of workers in a group
	q 		: number of workers to wait for in a group (code dimension)
	mu		: straggling parameter of one worker performing the whole task assigned to a group
	delay 	: time delay of one worker performing the whole task assigned to a group, default = 1
	
	Output:
	
	pdf of the overall runtime'''
	return n*comb(n-1,k-1)*cdf_q_order_statistic_in_group(t,q,K,mu,delay)**(k-1)*(1-cdf_q_order_statistic_in_group(t,q,K,mu,delay))**(n-k)*pdf_q_order_statistic_in_group(t,q,K,mu,delay)