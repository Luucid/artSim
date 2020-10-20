import numpy as np
import matplotlib.pyplot as plt
import time as ti
import calcEdges as ce

 
   
def prnt(x, y, cols, lt, cntr):
   # r = np.random.randint(0,6)
    plt.plot(x, y, "%s" % (cols),label = lt, linewidth=lt)
    counter = cntr + 1
    return counter
    
    
    
def frctRec(l, mp, mpmp, n, x, y, cols): # mp = multiplier, mpmp = multiplier multiplier.
    print("-------------------------")
    counter = 0
    for i in range(1,l):
        r = np.random.randint(1, 10)
        counter = frct(mp,n, x, y, cols[i%r], counter)
        mp *= mpmp
        print(counter)
       
        
    return counter
        
  


def frct(mp, n, x, y, cols, cntr):
    tck = np.random.uniform(0.1, 0.2)
    counter = cntr
    for i in range(1,n):
        
        if(i%2 == 0):
            xt = np.array(x)
            yt = np.array(y)
            xt *= mp
            yt *= mp
        else:
            xt = np.array(y)
            yt = np.array(x)
            xt *= mp
            yt *= mp
          
        counter = prnt(xt, yt, cols, tck, counter)

        xt = np.negative(xt)
        yt = np.negative(yt)  
        counter = prnt(xt, yt, cols, tck, counter)
            
   
        xt = np.negative(xt)  
        counter = prnt(xt, yt, cols, tck, counter)
           
      
        yt = np.negative(yt) 
        xt = np.negative(xt)
        counter = prnt(xt, yt, cols, tck, counter)
        
        return counter

  

def getCol():
    r = np.random.randint(0,4)
    c1 = ["b-", "c-", "g-", "y-", "r-", "b--", "c--", "g--", "y--", "r--"]  
    c2 = ["b-", "g-", "b-", "g-", "b-", "g--", "b--", "g--", "b--", "g--"] 
    c3 = ["r-", "r-", "b-", "b-", "r-", "r--", "g--", "g--", "y--", "r--"] 
    c4 = ["b-", "c-", "b-", "c-", "b-", "b--", "c--", "g--", "y--", "r--"] 

    if(r == 0):
        return c1
    if(r == 1):
        return c2
    if (r == 3):
        return c3
    if (r == 4):
        return c4
    return c1
        
        

def drawing(n, d, nShifts, mmp, mode, p):
    
    art = ce.Draw(n, d, mode)
    
    cols = getCol()
    
    qlt = 1200
    plt.figure(dpi=qlt) 
    plt.axis("equal")
    plt.subplot().spines["left"].set_visible(0)
    plt.subplot().spines["right"].set_visible(0)
    plt.subplot().spines["top"].set_visible(0)
    plt.subplot().spines["bottom"].set_visible(0)
 
   
    i = 0
    print("init base-line calculations.")
    while(i < n):       
        i+=next(art)
 
    print("done! \n")
    
    x = art.getEdgeX()
    y = art.getEdgeY()
    print(x, "XXXX")
    print(y, "YYYY")
    
    lines = len(x) - 1
    
 
    print("init drawing, please wait..")
    
    cntr = frctRec(nShifts, 1, mmp, n, x, y, cols)
    linesDrawn = cntr * lines
    plt.xlabel("n lines = "+str(linesDrawn))
    
    print("number of lines = %d" % linesDrawn)
    print("done! \n")  
    

    print("init render, please wait..")
    
    start = ti.time_ns()
    plt.xticks([])
    plt.yticks([])
    plt.show()
    end = ti.time_ns()
    rendTime = (end-start) * (10**-9)
   
    print("done! time used: %.3f" % rendTime)
    print("-------------------------\n")
    
    plt.plot(x, y, "r-")
    plt.show()

 

    
    

def startUp():
  
      
    mode = 10
    rep = 1
    
    
    for i in range(1):
        # n = np.random.randint(4, 6)
        n = 10
        d = n*2
        nShifts = np.random.randint(10, 50)
        mmp = np.random.uniform(0.92, 1.08)
        print("---------------------------")
        print("n = %d | nShifts = %d | multiplier = %.5f \n" % (n, nShifts, mmp))
        drawing(n, d, nShifts, mmp, mode, rep)   
        
    
           
    

    
startUp()






