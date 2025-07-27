class Solution:
    def removeDuplicates(self, nums):
        unique = 0  # pointer to track position for unique elements

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1

        return unique
