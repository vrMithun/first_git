class node:
    def __init__(self,data): 
        '''What it does::creating the constructor that acts as a node
                         each time we create a object new node is created.
           what is node::node act as a place holder for the data to be stored.
                         node contains its own memory address
           what is ref::reference is like a thead that links to or points to the next node.                            
        '''
        self.data=data #assigning the data
        self.ref=None  #setting defauld reference as None means it points to nothing.
class LinkedList:
    '''creating the linked list class to store all the functions'''
    head=node(None)
    '''head:here head is created by assingning None to the data'''
    def traversal(self):
        '''traversal():this method traverse through the linked list 
                    which helps in printing the data from the linked list'''
        if self.head==None:
            print("Linked List is empty")
        else:
            a=self.head
            while a!=None:
                print(a.data,end=" ")
                a=a.ref
            print()    
    def add_begin(self,data):
        if self.head.data==None:
            self.head.data=data 
        else:
            new_node=node(data)          
            new_node.ref=self.head
            self.head=new_node    
    def add_end(self,data):
        if self.head.data==None:
            self.head.data=data 
        else:    
            new_node=node(data)
            n=self.head
            if self.head==None:
                print("give input to the head first")
            else:
                while n.ref!=None:
                    n=n.ref                 
                n.ref=new_node
    def add(self,data,position):
        new_node=node(data)
        n=self.head
        if position==0:
            self.add_begin(data)
        if position==1:
            n.ref=new_node    
        for _ in range(position):
            if n.ref!=None: 
                n=n.ref
            else:
                self.add_end(data)  
                break  
        n.ref=new_node                
    def del_first(self):
        if self.head.ref==None:
            del self.head
        else:
            temp=self.head
            self.head=self.head.ref
            del temp            
                   

