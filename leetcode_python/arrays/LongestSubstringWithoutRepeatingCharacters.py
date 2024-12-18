'''def lengthOfLongestSubstring(s):
        if not s:
            return 0
        if len(s)==1:
            return 1    
        mylist=[]
        result=0
        i=0
        test=0
        while i<len(s):
            if s[i] not in mylist:
                mylist.append(s[i])
                i+=1
            else:
                if result<len(mylist):
                    result=len(mylist)
                mylist=[]
                test+=1
                i=test
        if result<len(mylist):
            result=len(mylist)
        return result        
print(lengthOfLongestSubstring("au"))'''
#optimised using sliding window
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(lengthOfLongestSubstring("pwwkew"))
