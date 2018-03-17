from Node import Node
class linkedlistuno:
    def __init__(self):                         #constructor of class
        self.head=None

    def isEmpty(self):                          #check is empty or not 
        return self.head==None

    def add(self,item):                         #insert anew node to linked list from beginning of list
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def length(self):                           #counts nodes in linked list 
        current=self.head
        count =0
        while current != None:
            count =count+1
            current = current.getNext()

        return count

    def search(self,item):                      #search for item in linked list
        current=self.head
        while current != None:
            if current.getData()==item:
                return True
            else :
                current =current.getNext()
        return False

    def remove(self,item):                      #remove item from linked list
        current=self.head
        previous=None  
        found=False
        while not found:                        #search for item in linked list
            if current.getData()==item:   
                found=True
                previous.setNext(current.getNext())
            else:
                previous=current
                current=current.getNext()

        if previous==None:                          # item which needed  to remove is head
                self.head =current.getNext()
        else:                                       # item which needed  to remove is current 
            previous.setnext(current.getnext())
        
#--------------------------------
    def selectionsort(self):                #selection sort
        current=self.head
        while current.getNext()!=None:      #do this loop while current isn't the last node
            minimum=current 
            minival=current.getData()       #put data of current in minival 
            item=current.getNext()          #item= next node of current
            while item !=None:              #do this loop while item is found
                if minival>item.getData():  #compare data of item with minival
                    minival=item.getData()  #put data of item in minival
                    minimum=item 
                
                item=item.getNext()         #item= next node

            minimum.setData(current.getData())      #put data of current in data of minimum
            current.setData(minival)                #put minival in data of current
        
            current=current.getNext()               #current= next node
#-------------------------------------------            
    def print_linked(self):                 #prints the first 3 elements in linked list
            print(self.head.getData())      #it is used with the large list
            m=self.head.getNext()           #we can make it with for loop(another way)
            print(m.getData())
            print(m.getNext().getData())

#------------------------------------
    def print_linked2(self):                #prints the all elements in linked list
        current=self.head                   #it is used with the small list
        while current !=None:
            print(current.getData())
            current=current.getNext()

            
