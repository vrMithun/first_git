def sumlist(l,length):
      if length==0:
          return 0
      else:
          return l[length-1]+sumlist(l,length-1)
l=[]
l=list(map(int,input().split()))
print(sumlist(l,len(l)))    
