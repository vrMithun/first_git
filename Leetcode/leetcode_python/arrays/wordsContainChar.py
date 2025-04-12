class Solution(object):
    def findWordsContaining(self, words, x):
        t=-1
        result=[]
        for i in words:
            if x in i:
                t+=1
                result.append(t)
            else:
                t+=1    
        return result    

        