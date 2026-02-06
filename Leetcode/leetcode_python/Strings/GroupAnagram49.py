class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict={}
        for i in strs:
            currstr="".join(sorted(list(i)))
            if currstr not in mydict:
                mydict[currstr]=[i]
            else:
                mydict[currstr].append(i)

        return mydict.values()