class Solution(object):
    def __init__(self):
        self.result=[]
    
    def topKFrequent(self, nums, k):
        mydict = {}
        for i in nums:
            if i not in mydict:
                mydict[i] = 0
            mydict[i] += 1
        
        for _ in range(k):
            self.maxi(mydict)
        
        print(self.result)
    
    def maxi(self, mydict): 
        temp = 0
        mymax = 0
        for i in mydict.keys():
            if mymax < mydict[i]:
                mymax = mydict[i]
                temp = i
        self.result.append(temp)
        mydict.pop(temp)

# Instantiate the solution
solution = Solution()

# Test cases
print("Test case 1 (Basic case with multiple elements):", end=" ")
arr1 = [1, 1, 1, 2, 2, 3]
solution.topKFrequent(arr1, 2)
# Expected: [1, 2]

print("Test case 2 (Single frequent number):", end=" ")
arr2 = [1, 2, 2, 2, 3, 3, 4]
solution.topKFrequent(arr2, 1)
# Expected: [2]

print("Test case 3 (All numbers same frequency):", end=" ")
arr3 = [1, 2, 3, 4, 5]
solution.topKFrequent(arr3, 3)
# Expected: [1, 2, 3] (Any 3 of them, since they all have the same frequency)

print("Test case 4 (Empty list):", end=" ")
arr4 = []
solution.topKFrequent(arr4, 2)
# Expected: [] (No frequent elements)

print("Test case 5 (Only one number repeated):", end=" ")
arr5 = [7, 7, 7, 7]
solution.topKFrequent(arr5, 1)
# Expected: [7] (Only one number, so it should be the most frequent)

print("Test case 6 (Negative numbers):", end=" ")
arr6 = [-1, -1, -2, -3, -2, -3, -3]
solution.topKFrequent(arr6, 2)
# Expected: [-3, -2] (Most frequent negative numbers)

print("Test case 7 (Large k):", end=" ")
arr7 = [1, 2, 3, 4, 5, 6]
solution.topKFrequent(arr7, 10)
# Expected: [1, 2, 3, 4, 5, 6] (All are equally frequent, returns all)

print("Test case 8 (All numbers are the same):", end=" ")
arr8 = [9, 9, 9, 9, 9, 9]
solution.topKFrequent(arr8, 1)
# Expected: [9] (Only one unique number)

print("Test case 9 (Mixed frequency):", end=" ")
arr9 = [1, 2, 2, 3, 3, 3, 4]
solution.topKFrequent(arr9, 3)
# Expected: [3, 2, 1] (Frequency 3 > Frequency 2 > Frequency 1)

print("Test case 10 (Same number twice):", end=" ")
arr10 = [5, 5, 6, 6, 7, 7]
solution.topKFrequent(arr10, 1)
# Expected: [5] or [6] or [7] (Any of these numbers, all have the same frequency)
