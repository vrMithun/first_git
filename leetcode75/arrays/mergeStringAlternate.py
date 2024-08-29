
def mergeAlternately (word1, word2):
    result=""
    if len(word1)<len(word2):
        for i in range(len(word1)):
            result+=word1[i]
            result+=word2[i]
        i+=1    
        while i<len(word2):
            result+=word2[i]  
            i+=1 
    else:
        for i in range(len(word2)):
            result+=word1[i]
            result+=word2[i]
        i+=1    
        while i<len(word1):
            result+=word1[i]  
            i+=1 
    print(result)    
mergeAlternately("abcd","efgh")           