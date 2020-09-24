import numpy as np
import matplotlib.pyplot as plt
import time as ti

class Draw():
    def __init__(self, n, d): #d is dimention, x y.
        self.ss = [-1, 0, 1]
     
        self.edgeX = []
        self.edgeY = []
        self.lastX = int(d/2)
        self.lastY = int(d/2)
        
        self.usedPoints = [[]]*d # [x][y]
        self.d = d
        self.infloop = 0
        
        self.chk = 1 #loop når denne er 1
        self.curPos = (d/2,d/2)
        self.nextPos = (4,4)
     
    
    def __next__(self):
        
        self.chk = 1 
       
        #while(self.chk): 
        a = np.random.choice(self.ss, 2)     
        self.nextPos = self.curPos + a 
        
        while((a[0] == 0 and a[1] == 0) 
              or (self.nextPos[0] >= d or self.nextPos[1] >= d) 
              or (self.nextPos[0] <= 0 or self.nextPos[1] <= 0) 
              or (self.lastX == int(a[0]) and self.lastY == int(a[1])) 
              or self.isStuck(int(self.nextPos[0]-1),self.nextPos[1])
              ):
           
            a = np.random.choice(self.ss, 2)   
            self.nextPos = self.curPos + a 
            
        self.chk = self.checkEdges(tuple(self.nextPos), self.curPos)
        
        
        # if (self.isStuck(int(self.nextPos[0]-1),self.nextPos[1])):
        #     return 1
        
       
        if(self.chk == 0):
            self.edgeX = np.append(self.edgeX, int(self.curPos[0]))   
            self.edgeY = np.append(self.edgeY, int(self.curPos[1]))  
            self.lastX = int(a[0])
            self.lastY = int(a[1])
            self.curPos = self.nextPos
        
        return 0
       
        
            

    
    
    def getEdgeX(self):   
        return self.edgeX
    
    def getEdgeY(self):
        return self.edgeY
    
    def isStuck(self, x, y):
        
        ################################################### middle    
        
        if(x > 1 and x < self.d-1 and y > 1 and y < self.d-1):
            if(y+1 in self.usedPoints[x-1] and y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x+1]): #top
                if(y in self.usedPoints[x-1] and y in self.usedPoints[x+1]): #mid
                    if(y-1 in self.usedPoints[x-1] and y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x+1]): #bot
                        print("stuck in middle")
                        return 1
                    
        ###################################################
            
        ################################################### endlim    
        
        if(x == self.d-1 and y == self.d-1): #one
            if(y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x-1]): #bot
                if(y in self.usedPoints[x-1]): #mid
                    print("stuck in endlim one")
                    return 1
                
        if(x == self.d-1 and y < self.d-1 and y > 1): #two
            if(y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x-1]): #top
                if(y in self.usedPoints[x-1]): #mid
                    if(y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x-1]): #bot
                        print("stuck in endlim two")
                        return 1
                
        if(x == self.d - 1 and y == 1): #three
            if(y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x-1]): #top
                if(y in self.usedPoints[x-1]): #mid    
                    print("stuck in endlim three")
                    return 1       
                
         ###################################################
         
         ################################################### startlim 
               
        if(x == 1 and y == 1): #one
            if(y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x+1]): #top
                if(y in self.usedPoints[x+1]): #mid
                    print("stuck in startlim one")
                    return 1
        
        if(x == 1 and y > 1 and y < self.d-1): #two
            if(y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x+1]): #top
                if(y in self.usedPoints[x+1]): #mid
                    if(y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x+1]): #bot
                        print("stuck in startlim two")
                        return 1
                
        if(x == 1 and y == self.d - 1): #three
            if(y in self.usedPoints[x+1]): #mid
                if(y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x+1]): #bot
                    print("stuck in startlim three")
                    return 1
                
        
            
        ######################################################
        
        ###################################################### ylim
        
        if((x > 1 and x < self.d-1) and y == self.d-1): #max
            if(y in self.usedPoints[x-1] and y in self.usedPoints[x+1]): #mid
                if(y-1 in self.usedPoints[x-1] and y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x+1]): #bot
                    print("stuck in ylim max")
                    return 1
                
        if((x > 1 and x < self.d-1) and y == 1): #min
            if(y in self.usedPoints[x-1] and y in self.usedPoints[x+1]): #mid
                if(y+1 in self.usedPoints[x-1] and y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x+1]): #top
                    print("stuck in ylim min")
                    return 1
                
        ######################################################     
        
            
        # print("returnning 0")
        return 0
                        
    
    def getSizeX(self):
        return(len(self.edgeX))
    
    def addPoint(self, x, y, pp): #pp = prev point
        l = 0 #left
        r = 0 #right
        t = 0 #top
        b = 0 #bot
    
        pp1 = ((x+1), (y-1))
        pp2 = (x+1, y+1)
        pp3 = ((x-1), (y+1))
        pp4 = ((x-1), (y-1))
        
        
        if(y in self.usedPoints[x]): #is spot empty
            return 1

        
        if(x>0):
            if(y > 0):
                if(y in self.usedPoints[x-1] 
                   and y-1 in self.usedPoints[x] 
                   and y-1 in self.usedPoints[x-1] 
                   and pp == pp4
                   ): return 1 # c4
              
            if(y < self.d):
                if(y in self.usedPoints[x-1] 
                   and y+1 in self.usedPoints[x] 
                   and y+1 in self.usedPoints[x-1] 
                   and pp == pp3
                   ): return 1 # c3
                
            
            if(y in self.usedPoints[x-1]):
                l = 1
        
                
        if(x<self.d):
            
            if(y < self.d):
                if(y in self.usedPoints[x+1] 
                   and y+1 in self.usedPoints[x] 
                   and y+1 in self.usedPoints[x+1] 
                   and pp == pp2
                   ): return 1 # c2
                
            if(y > 0):
                if(y in self.usedPoints[x+1] 
                   and y-1 in self.usedPoints[x] 
                   and y-1 in self.usedPoints[x+1] 
                   and pp == pp1
                   ): return 1 # c1
                
                
       
        if(x < self.d):
            if(y in self.usedPoints[x+1]):
                r = 1      
                
        if(y < self.d):
            if(y+1 in self.usedPoints[x]):
                t = 1
        
        if(y > 0):
            if(y-1 in self.usedPoints[x]):
                b = 1
        
            
        
        
        if(l and r and t and b):
            return 1
            
        self.usedPoints[x] = np.append(self.usedPoints[x], y)
        return 0
       
        
        
    
    def checkEdges(self, newP, curP):       
        return self.addPoint(int(newP[0]-1), int(newP[1]), tuple(curP))
    
        
            

#######################################


n = 10000
d = n*2
max_i = n*10
i = 0
start = ti.time_ns()

art = Draw(n, d)
# for i in range(n):
#     print(i)
    
while(art.getSizeX() < n and i < max_i):
    next(art)
    i+=1
    
    
    
end = ti.time_ns()
dif = (end-start)*(10**-9)
print("time used for n = %d was %.3f sec" % (n, dif))



x = art.getEdgeX()
y = art.getEdgeY()

print("size of x = %d, size of y = %d" % (len(x), len(y)))


    

plt.figure(dpi=1200) 
plt.axis("equal")
plt.plot(x, y, "b-",linewidth=0.5)
plt.show()

############################################
        

# def getCol():
#     colors = ["r-", "b-", "g-"]
#     r = np.random.randint(0,3)
#     return str(colors[r])




     # if(y in self.usedPoints[x]):
     #        return 1
     #    if(x > 0):
     #        if(y in self.usedPoints[x-1]):         
     #            return 1
     #    if(x < self.d):
     #        if(y in self.usedPoints[x+1]):
     #            return 1
            
     #    if(y > 0):
     #        if((y-1) in self.usedPoints[x]):
     #            return 1
     #        # if(x > 0):
     #        #     if((y-1) in self.usedPoints[x-1]):
     #        #         return 1
     #        if(x < self.d):
     #            if((y-1) in self.usedPoints[x+1]):
     #                return 1
                
     #    if(y < self.d):
     #        if((y+1) in self.usedPoints[x]):
     #            return 1
     #        # if(x > 0):
     #        #     if((y+1) in self.usedPoints[x-1]):
     #        #         return 1
     #        if(x < self.d):
     #            if((y+1) in self.usedPoints[x+1]):
     #                return 1