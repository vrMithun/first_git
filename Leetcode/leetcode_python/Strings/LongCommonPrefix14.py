class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=strs[0]
        for i in range(len(strs)):
            j=0
            if len(result)>len(strs[i]):
                result=result[:len(strs[i])]
            while j<len(result):
                if strs[i][j]!=result[j]:
                    result=result[:j]
                    break
                j+=1
        return result
        