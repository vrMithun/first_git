from Stack import *
class operation:
    stack_string=Stack()
    stack_int=Stack()
    stack_float=Stack()
    def __init__(self,n):
        self.n=n
        for _ in range(self.n):
            data=input("enter the type:")
            
            if data=="int":
                value=input("enter value:")
                self.stack_int.push(value)
            if data=="string":
                value=input("enter value:")
                self.stack_string.push(value)
            if data=="float":
                value=input("enter value:")
                self.stack_float.push(value)
    def remove(self,total,type):
        for _ in range(total):
            if type=="int":
                self.stack_int.pop()
            if type=="string":
                self.stack_string.pop()
            if type=="float":
                self.stack_float.pop()
    def get_top(self,type):
            if type=="int":
                self.stack_int.top()
            if type=="string":
                self.stack_string.top()
            if type=="float":
                self.stack_float.top()   
                 
myobj=operation(5)
myobj.stack_int.traverse()  
myobj.remove(3,"int") 
myobj.stack_int.traverse()    
                          