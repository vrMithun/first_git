class Solution:
    def intToRoman(self,num):
        self.roman={1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        self.keys=list(self.roman.keys())
        part=self.partition(num)
        print(self.keys)
        result=""
        for i in range(len(part)-1,-1,-1):
            result+=self.helper(part[i],i)
        return result
                        
    def helper(self,num,index):
        i=len(self.keys)-1
        result=""
        actual_num=num*(10**index)
        while i>=0:
            if num!=4 and num!=9:
                if actual_num-self.keys[i]>=0:
                    actual_num-=self.keys[i]
                    result+=self.roman[self.keys[i]]
                else:
                    i-=1
            else:
                if self.keys[i]-actual_num in self.keys:
                    actual_num=self.keys[i]-actual_num
                    result+=self.roman[actual_num]+self.roman[self.keys[i]]
                    return result
                else:
                    i-=1
        return result


    def partition(self,nums):
        result=[]
        dup=nums
        digit=0
        while dup>0:
            result.append((dup%10))
            dup=dup//10
            digit+=1
        return result

myobj=Solution()
print(myobj.intToRoman(1994))

# More efficient way
'''
class Solution:
    def intToRoman(self, num):
        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10]
        )

# Test
s = Solution()
print(s.intToRoman(1994))  # Output: MCMXCIV

'''