class Solution(object):
    def __init__(self):
        self.result=[]
    def topKFrequent(self, nums, k):
        mydict={}
        for i in nums:
            if i not in mydict:
                mydict[i]=0
            mydict[i]+=1
        for _ in range(k):
            self.maxi(mydict)
        print(self.result) 
    def maxi(self,mydict): 
        temp=0
        mymax=0  
        for i in mydict.keys():
            if mymax<mydict[i]:
                mymax=mydict[i]
                temp=i        
        self.result.append(temp)
        mydict.pop(temp)
myobj=Solution()
arr=[1,1,1,2,2,3]
myobj.topKFrequent(arr,2)

                
        