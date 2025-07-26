class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n= len(haystack)
        m= len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return(-1)
        


#Alternative
"""
class Solution(object):
    def strStr(self, haystack, needle):
  
        if needle in haystack:
            return haystack.index(needle)
        else:
            return(-1)
"""
