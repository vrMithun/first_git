class Node:
    def __init__(self,Name=None,event_ID=None):
        self.Name=Name
        self.event_ID=event_ID
class LL:
    def __init__(self,event_ID):
        self.head=Node() 
        self.event_ID=event_ID
        self.mydict={}
        self.count=0
    def register(self,Name,ID):
        self.mydict[Name]=ID
    def return_event(self,ID):
         lst=self.mydict.keys()
         for i in lst:
             if ID==self.mydict[i]:
                 print("Name of the participant:f{i} Event participated:f{mydict[i]}")
                 self.count+=1   
    def total(self):
        return self.count                       