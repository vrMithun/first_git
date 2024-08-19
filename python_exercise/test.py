class Node:
    def __init__(self,title=None,author=None):
        self.title=title
        self.author=author
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=Node()        
    def add_book(self,title,author):
        if self.head.title==None and self.head.author==None:
            self.head.title=title
            self.head.author=author
        else:
            New_book=Node(title,author)
            n=self.head
            while n:
                if n.ref==None:
                    n.ref=New_book
                    break
                n=n.ref
    def remove_book(self,title,author):
        n=self.head
        prev=None
        while n:
            if n.title==title and n.author==author:
                if n==self.head:
                    self.head=n.ref
                else:       
                    prev.ref=n.ref  
                del n
                n=prev.ref
            else:
                prev=n           
                n=n.ref     
    def search_book(self,title,author):
        n=self.head
        test=1
        while n:
            if n.title==title and n.author==author:
                print(f"book is at position {test}") 
                return 
            test+=1       
            n=n.ref 
        print("book doesnt exist")
    def traverse(self):
        n=self.head
        while n:
            print(f"title:{n.title}",f"author:{n.author}")
            n=n.ref        
lib1=LinkedList()
lib1.add_book('a','b') 
lib1.add_book('d','h') 
lib1.add_book('g','c') 
lib1.add_book('f','b') 
lib1.remove_book('f','b')
lib1.traverse()                          
   