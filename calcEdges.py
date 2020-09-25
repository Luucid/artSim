import numpy as np

class Draw():
    def __init__(self, n, d, tpType): #d is dimention, x y.
        self.ss = [-1, 0, 1]
        self.edgeX = []
        self.edgeY = []
        self.lastX = int(d/2)
        self.lastY = int(d/2)
        
        self.tpTypes = ["standard", "corners", "chaos", "growing", "fractal"]
        self.tpc = 0
        self.crns = [[1, 1],[1, d/2],[d/2, d/2],[d/2, 1]]
        self.ci = 0
        self.tp = self.tpTypes[(tpType-1)%5] #line navigation types.
        
        self.usedPoints = [[]]*d # [x][y]
        self.d = d
        self.infloop = 0
        
        self.chk = 1 #loop når denne er 1
        if(self.tp == "fractal"):
            self.curPos = (1,1)
            self.nextPos = (1,1)
        else: 
            self.curPos = (d/2,d/2)
            self.nextPos = (d/2,d/2)
        print("tp type set to %s" % self.tp)
    
    def __next__(self):
        
        self.chk = 1 
        self.tpc = 1
       
        a = np.random.choice(self.ss, 2)     
        self.nextPos = self.curPos + a 
        
        while((a[0] == 0 and a[1] == 0) 
              or (self.nextPos[0] >= self.d) 
              or (self.nextPos[0] <= 0) 
              or (self.lastX == int(a[0]) and self.lastY == int(a[1])) 
              or self.isStuck(int(self.nextPos[0]),int(self.nextPos[1]))
              ):
            
            if(self.tp == "standard"):
                if(self.tpc > 5):
                    self.ss = [-self.tpc, 0, self.tpc]
                a = np.random.choice(self.ss, 2)   
                self.nextPos = self.curPos + a 
                self.tpc += 1
                
        
            elif(self.tp == "corners"):
                if(self.tpc > 5):
                    self.nextPos = self.crns[self.ci]
                    self.ci +=1
                    if(self.ci > 3):
                        self.tp = "standard"
                    
                else:
                    a = np.random.choice(self.ss, 2)   
                    self.nextPos = self.curPos + a 
                self.tpc += 1
                
            
            elif(self.tp == "chaos"):
                
                rnga = np.random.randint(1, 10)
                rngb = np.random.randint(1, 10)
                self.ss = [-rnga, 0, rngb]
                a = np.random.choice(self.ss, 2)   
                self.nextPos = self.curPos + a 
            
            elif(self.tp == "growing"):
                
                a = np.random.choice(self.ss, 2)   
                self.nextPos = self.curPos + a 
                
                self.ss[0] -= np.random.randint(1, 3)
                self.ss[2] += np.random.randint(1, 3)
            
            elif(self.tp == "fractal"):
                self.ss = [0, 1, 2]
                a = np.random.choice(self.ss, 2)   
                self.nextPos = self.curPos + a
                
                
                
                
                
             
            
            
            
        self.chk = self.checkEdges(tuple(self.nextPos), self.curPos)
        
        if(self.tp != "growing"):
            self.ss = [-1, 0, 1]
        if(self.chk == 0):
      
            self.edgeX = np.append(self.edgeX, int(self.curPos[0]))   
            self.edgeY = np.append(self.edgeY, int(self.curPos[1]))  
                
            self.lastX = int(a[0])
            self.lastY = int(a[1])
            self.curPos = self.nextPos
            return 1
        return 0
        
     

 
        
        
        
        
    
    def getEdgeX(self):   
        return self.edgeX
    
    def getEdgeY(self):
        return self.edgeY
    
    def diagCheck(self, a, ay, b, by, pp, np):
        if(ay in self.usedPoints[a] and by in self.usedPoints[b]):
            
            if((pp == (np[0] - 1, np[1]-1))  #c4
               or (pp == (np[0]+1, np[1]+1)) #c2
               or (pp == (np[0]-1, np[1]+1)) #c3
               or (pp == (np[0]+1, np[1]-1)) #c1
               ):
                #print("stopped cross")
                return 1         
        return 0
    
    def isStuck(self, x, y):
        
        ################################################### middle    
        
        if(x > 1 and x < self.d-1 and y > 1 and y < self.d-1):
            if(y+1 in self.usedPoints[x-1] and y+1 in self.usedPoints[x] and y+1 in self.usedPoints[x+1]): #top
                if(y in self.usedPoints[x-1] and y in self.usedPoints[x+1]): #mid
                    if(y-1 in self.usedPoints[x-1] and y-1 in self.usedPoints[x] and y-1 in self.usedPoints[x+1]): #bot
                       # print("stuck in middle")
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
    
        if(y in self.usedPoints[x]): #is spot empty
            return 1

        ###########################################
                   #  diagChecks  # 
        ###########################################
        if(x > 0):
            if(y > 0):
                if(self.diagCheck(x-1, y, x, y-1, pp, (x, y))): #c4
                    return 1
            
            if(y < self.d):
                if(self.diagCheck(x-1, y, x, y+1, pp, (x, y))): #c3
                    return 1
        
        if(x < self.d):
            if(y > 0):
                if(self.diagCheck(x, y-1, x+1, y, pp, (x, y))): #c1
                    return 1
            
            if(y < self.d):
                if(self.diagCheck(x+1, y, x, y+1, pp, (x, y))): #c2
                    return 1
        #############################################  
            
        self.usedPoints[x] = np.append(self.usedPoints[x], y)
        return 0
       
        
        
    
    def checkEdges(self, newP, curP):       
        return self.addPoint(int(newP[0]-1), int(newP[1]), tuple(curP))
    
        
            

#######################################