
def groupAnagrams(strs):
    result=[]
    temp=[]
    i=0
    while len(strs)>0:
        if len(result)==0:
            temp.append(strs[i])
            result.append(temp)
            strs.remove(strs[i])
            temp=[]
        else:    
            for j in range(len(result)):
                if len(strs)>0:
                    if isAnagram(result[j][0],strs[i]):
                        result[j].append(strs[i])
                        strs.remove(strs[i])
                        break
                    elif j==(len(result)-1):
                        temp.append(strs[i])
                        result.append(temp)
                        strs.remove(strs[i])
                          
            temp=[]     
    print(result)       
            
def isAnagram(str1,str2):
    test=set(str1)
    if len(str1)==len(str2):
        for i in test:
            if str1.count(i)!=str2.count(i):
                return False
        return True
    return False            
                
groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"])        