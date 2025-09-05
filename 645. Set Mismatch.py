class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = [0] * (n + 1)  # index from 1..n
        dup = miss = -1

        # Count frequencies
        for num in nums:
            count[num] += 1

        # Find duplicate and missing
        for i in range(1, n + 1):
            if count[i] == 2:
                dup = i
            elif count[i] == 0:
                miss = i

        return [dup, miss]
