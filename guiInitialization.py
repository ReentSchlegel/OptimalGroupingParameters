from appJar import gui

N = 100 
u = 3
mu = 1.0
rs = 200000*100


def press():
    global N, u, mu
    N = app.entry("Nos")  
    u = app.entry("Csp")
    mu = app.entry("Sp")
    rs = app.entry("NoeiA")
    if N < 1 or u < 0 or mu <= 0 or rs < 1 or (N % 1) != 0 or (u % 1) != 0 or (rs % 1) != 0:
    	app.infoBox("Invalid Input","Note that the number of servers and the number of entires in A must be a positive integer, the \
	number of colluding services must be a non negative integer and the straggling paramter must be a positive number")
    else:
    	print(N,u,mu)
    


app = gui("Code Parameter Optimization", "600x300", bg='orange', font={'size':18})
app.startLabelFrame("Input Arguments")
app.addLabel("l1","Number of servers",1,0)
app.addNumericEntry("Nos",1,1)
app.setEntry("Nos", N)
app.addLabel("l2","Colluding service providers",2,0)
app.addNumericEntry("Csp",2,1)
app.setEntry("Csp", str(u))
app.addLabel("l3","Straggling Parameter",3,0)
app.addNumericEntry("Sp",3,1)
app.setEntry("Sp", mu)
app.addLabel("l4","Number of entries in A",4,0)
app.addNumericEntry("NoeiA",4,1)
app.setEntry("NoeiA", rs)
app.stopLabelFrame()
app.addButtons(["Submit", "Cancel"], [press, app.stop],1)


app.go()