class Solution(object):
    def mostWordsFound(self, sentences):
        max=0
        for i in range(len(sentences)):
            lst=sentences[i].split(" ")
            count=len(lst)
            if max<count:
                max=count
        return max        
        