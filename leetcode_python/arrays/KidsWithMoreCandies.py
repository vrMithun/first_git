class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest=candies[0]
        lst=[]
        for i in range(1,len(candies)):
            if greatest<candies[i]:
                greatest=candies[i]
        for j in range(len(candies)):
            test=candies[j]+extraCandies
            if test>=greatest:
                lst.append(True)
            else:
                lst.append(False)    
        return lst    
        