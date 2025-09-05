class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If needle is empty, return 0
        if not needle:
            return 0

        n, m = len(haystack), len(needle)

        # Loop through haystack up to a point where needle can still fit
        for i in range(n - m + 1):
            # Assume match, then check character by character
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i  # Found first occurrence

        return -1  # Not found
