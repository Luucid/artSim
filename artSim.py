import numpy as np
import matplotlib.pyplot as plt
import time as ti
import calcEdges as ce







def prnt2(x, y, cols, lt, n):
    for i in range(1, n-1):
            
        if(x[i] < x[i-1]):
            if(x[i-1] - x[i] > 1):
                plt.plot([x[i-1], x[i]], [y[i-1], y[i]], "c:", linewidth=lt, markersize= 0.5)
            else:
                plt.plot([x[i-1], x[i]], [y[i-1], y[i]], "%s" %(cols[i%3]), linewidth=lt)
                
        else:
            if(x[i] - x[i-1] > 1):
                plt.plot([x[i-1], x[i]], [y[i-1], y[i]], "c:", linewidth=lt, markersize = 1)
            else:
                plt.plot([x[i-1], x[i]], [y[i-1], y[i]], "%s" %(cols[i%3]), linewidth=lt)
 
   
def prnt(x, y, cols, lt):
    r = np.random.randint(0,6)
    plt.plot(x, y, "%s" % (cols[r]),label = lt, linewidth=lt)
    
    
    
def frctRec(l, mp, mpmp, n, x, y, cols): # mp = multiplier, mpmp = multiplier multiplier.
    print("-------------------------")
    for i in range(1,l):
        frct(mp,n, x, y, cols)
        mp *= mpmp
  


def frct(mp, n, x, y, cols):
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
          
        prnt(xt, yt, cols, 0.1)
              
        xt = np.negative(xt)
        yt = np.negative(yt)  
        prnt(xt, yt, cols, 0.1)
            
        xt = np.negative(xt)  
        prnt(xt, yt, cols, 0.1)
                 
        yt = np.negative(yt) 
        xt = np.negative(xt)
        prnt(xt, yt, cols, 0.1)
        

  

        
        
        

def drawing(n, d, nShifts, mmp, prct, mode, p):
    start = ti.time_ns()
    art = ce.Draw(n, d, mode)
    cols = ["r-", "g-", "b-", "y-", "c-", "m-"]  
    
    i = 0
    while(i < n):
        
        i+=next(art)
        if(i%prct == 0):
            print("%d of %d"%(i, n))
             
        
    end = ti.time_ns()
    dif = (end-start)*(10**-9)
    print("time used for n = %d was %.3f sec" % (n, dif))
    
    x = art.getEdgeX()
    y = art.getEdgeY()
            

    qlt = int(input("please enter print quality(200-1200, higher is better): "))
    plt.figure(dpi=qlt) 
    plt.axis("equal")
    plt.axis("off")
    plt.plot(x, y, "b-")
    plt.show()
    
    plt.figure(dpi=qlt) 
    plt.axis("equal")
    plt.axis("off")

    if(p):
        print("init drawing, please wait..")
        frctRec(nShifts, 1, mmp, n, x, y, cols)
        print("done! \n\n\n")  
    
    else:
        print("init drawing, please wait")
        prnt2(x, y, cols, 0.2, n)
      
    print("init render, please wait..\n"+"-------------------------")
    plt.show()
    print("done!")

 


def startUp():
    n = int(input("enter number of lines in one layer: "))
    #d = int(input("enter canvas multiplier: "))
    d = 2
    d = n*d
    nShifts = 0
    mmp = 1
    prct = n / 100
    #print("\n\n"+"modes:\n" + "1. standard \n"+"2. corners \n"+"3. chaos \n"+"4. growing \n"+"5. bestPat \n")
    #mode = int(input("choose mode between 1-5: "))
    mode = 5
    rep = int(input("enable patternization? (0/1): "))

    if(rep):
        nShifts = int(input("choose number of repetitions for pattern: "))
        mmp = float(input("choose scew multiplier(x<1 == shrinking): "))
    

    drawing(n, d, nShifts, mmp, prct, mode, rep)   

    
startUp()






