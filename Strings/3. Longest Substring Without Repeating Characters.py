class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        maxlen = 0
        seen = set()   # keep track of current substring chars

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                maxlen = max(maxlen, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return maxlen
