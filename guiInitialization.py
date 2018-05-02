from appJar import gui
from grouping import find_grouping

# Default values
N = 100             # Number of workers
u = 3               # Number of compromised service provieders
mu = 0.001          # Straggling parameter of one worker performing the whole task
delay = 1000        # Delay of one worker performing the whole task
r = 2000000     	# Number of rows in A
s = 128 			# Number of columns in A
p = 32 				# Number of bits per number (2^p is the field size)



def press():        
    '''Gets called when "submit" is pressed'''
    # Read the inputs
    N = app.entry("Nos")    
    u = app.entry("Csp")
    mu = app.entry("Sp")
    delay = app.entry("Del")
    r = app.entry("NoriA")
    s = app.entry("NociA")
    p = app.entry("Nob")

    # Reset the outputs
    app.setLabel("lq", [])
    app.setLabel("lk", [])
    app.setLabel("ln", [])
    app.setLabel("lT", [])

    # Initialize progress meter
    app.setMeter("Progress",0)

    # Catch invalid inputs
    if N < 1 or u < 0 or mu <= 0 or delay <=0 or r < 1 or s < 1 or p < 1 or (N % 1) != 0 or (u % 1) != 0 or (r % 1) != 0 or (s % 1) != 0 or (p % 1) != 0:
    	
        app.infoBox("Invalid Input","Note that the number of servers, the number of rows and columns in A and the number of bits per number must be positive integers, the number of colluding services must be a non negative integer and the straggling paramter and delay must be a positive number")
    
    else:   # Input is valid
        n, k, q, T = find_grouping(N,u,mu,delay,r,s,p,app)	# Compute optimal grouping

        # Write output
        app.setLabel("lq", "(" + str(int(N/n)) + "," + str(q) + ")")
        app.setLabel("lk", str(k))
        app.setLabel("ln", str(n))
        app.setLabel("lT", str(T))

        
    


app = gui("Code Parameter Optimization", "1400x1400", bg='green', font={'size':18}) # Open a new gui called app

# Inputs
app.startLabelFrame("Input Arguments")                  # Frame the inputs
app.addLabel("l1","Number of servers",1,0)              # Label for N
app.addNumericEntry("Nos",1,1)                          # Input box for N
app.setEntry("Nos", N)                                  # Set default value of N
app.addLabel("l2","Colluding service providers",2,0)    # Label for u
app.addNumericEntry("Csp",2,1)                          # Input box for u
app.setEntry("Csp", str(u))                             # Set default value of u
app.addLabel("l3","Straggling Parameter",3,0)           # Label for mu
app.addNumericEntry("Sp",3,1)                           # Input box for mu
app.setEntry("Sp", mu)                                  # Set default value of mu
app.addLabel("l4","Delay",4,0)                          # Label for delay
app.addNumericEntry("Del",4,1)                          # Input box for delay
app.setEntry("Del", delay)                              # Set default value of delay
app.addLabel("l5","Number of rows in A",5,0)         	# Label for r
app.addNumericEntry("NoriA",5,1)                        # Input box for r
app.setEntry("NoriA", r)                               	# Set default value of r
app.addLabel("l6","Number of columns in A",6,0)         # Label for s
app.addNumericEntry("NociA",6,1)                        # Input box for s
app.setEntry("NociA", s)                               	# Set default value of s
app.addLabel("l7","Number of bits per number",7,0)      # Label for p
app.addNumericEntry("Nob",7,1)                        	# Input box for p
app.setEntry("Nob", str(p))                             # Set default value of p
app.stopLabelFrame()

# Buttons
app.addButtons(["Submit", "Cancel"], [press, app.stop],1)   # Add two buttons. Call "Press" when "Submit" is pressed and stop the app when "Cancel" is pressed

# Progress meter
app.addMeter("Progress",2)								# Add a progress meter
app.setMeterFill("Progress", "blue")

# Output 
app.startLabelFrame("Output")                           # Frame the outputs
app.addLabel("l8","Number of service providers:",0,0)   # Label for n
app.addLabel("ln","",0,1)                               # Textbox for n
app.addLabel("l9","Service providers to wait for:",1,0) # Label for k
app.addLabel("lk","",1,1)                               # Textbox for k
app.addLabel("l10","Code dimension at the service providers:",2,0)	# Label for q
app.addLabel("lq","",2,1)                               # Textbox for q
app.addLabel("l11","Expected waiting time:",3,0)        # Label for T
app.addLabel("lT","",3,1)                               # Textbox for T
app.stopLabelFrame()


# Start the gui
app.go()