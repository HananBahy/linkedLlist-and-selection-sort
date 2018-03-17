class Node :
    def __init__(self,initdata): #initialize self.data
        self.data = initdata  
        self.next=None        
        
    def getData(self):         #return data
        return self.data       
    
    def getNext(self):         #return next
        return self.next
    
    def setData(self,newdata): # put anew value to data in node
        self.data =newdata
        
    def setNext(self,newnext): # put anew value to next in node 
        self.next =newnext
