from appJar import gui
from grouping import find_grouping

# Default values
N = 100             # Number of workers
u = 3               # Number of compromised service provieders
mu = 0.1          # Straggling parameter of one worker performing the whole task
delay = 10          # Delay of one worker performing the whole task
rs = 200000*100     # Number of entries in A



def press():        
    '''Gets called when "submit" is pressed'''
    # Read the inputs
    N = app.entry("Nos")    
    u = app.entry("Csp")
    mu = app.entry("Sp")
    delay = app.entry("Del")
    rs = app.entry("NoeiA")

    # Catch invalid inputs
    if N < 1 or u < 0 or mu <= 0 or delay <=0 or rs < 1 or (N % 1) != 0 or (u % 1) != 0 or (rs % 1) != 0:
    	
        app.infoBox("Invalid Input","Note that the number of servers and the number of entires in A must be a positive integer, the \
	number of colluding services must be a non negative integer and the straggling paramter and delay must be a positive number")
    
    else:   # Input is valid
        n, k, q, T = find_grouping(N,u,mu,delay,rs)     # Compute optimal grouping

        # Write output
        app.setLabel("lq", "(" + str(int(N/n)) + "," + str(q) + ")")
        app.setLabel("lk", str(k))
        app.setLabel("ln", str(n))
        app.setLabel("lT", str(T))

        
    


app = gui("Code Parameter Optimization", "1400x1000", bg='green', font={'size':18}) # Open a new gui called app

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
app.addLabel("l5","Number of entries in A",5,0)         # Label for rs
app.addNumericEntry("NoeiA",5,1)                        # Input box for rs
app.setEntry("NoeiA", rs)                               # Set default value of rs
app.stopLabelFrame()

# Buttons
app.addButtons(["Submit", "Cancel"], [press, app.stop],1)   # Add two buttons. Call "Press" when "Submit" is pressed and stop the app when "Cancel" is pressed

# Output 
app.startLabelFrame("Output")                           # Frame the outputs
app.addLabel("l6","Number of service providers:",0,0)   # Label for n
app.addLabel("ln","",0,1)                               # Textbox for n
app.addLabel("l7","Service providers to wait for:",1,0) # Label for k
app.addLabel("lk","",1,1)                               # Textbox for k
app.addLabel("l8","Code dimension at the service providers:",2,0)   # Label for q
app.addLabel("lq","",2,1)                               # Textbox for q
app.addLabel("l9","Expected waiting time:",3,0)         # Label for T
app.addLabel("lT","",3,1)                               # Textbox for T
app.stopLabelFrame()


# Start the gui
app.go()