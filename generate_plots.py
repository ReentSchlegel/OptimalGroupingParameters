from grouping import find_grouping
import pickle
import matplotlib.pyplot as plt


#################
# Values 		#
#################


numServ = [100,250,500,750,1000]						# Different number of servers
u = 3													# Colluding service providers
mu = 0.001												# Straggling parameter
delay = 1000											# Delay	
r = 2000000												# Number of rows in A		
s = 128													# Number of columns in A
p = 32													# Bits per number


#################
# Calculations 	#
#################


for N in numServ:										# For all N
#	find_grouping(N,u,mu,delay,r,s,p,SAVE=1)			# Calculate and save runtime 
	print('Calculation for N = ' + str(N) + ' done')	# Update progress


#################
# Plot 			#
#################


for N in numServ:										# For all N
	with open(str(N) + '.pckl','rb') as f:				# Open file
		T, div = pickle.load(f)							# Load saved values
		plt.plot(div,T,marker = 'x',Label = 'N = ' + str(N))			# Plot runtime over grouping



plt.xlabel('Number of groups')							# Label x axis
plt.ylabel('Expected runtime')							# Label y axis
plt.legend()											# Include legend
plt.grid()												# Add grid

plt.show()												# Show the plot