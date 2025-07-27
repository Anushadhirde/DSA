class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Floyd's Tortoise and Hare    
        slow = nums[0]
        fast = nums[0]
        
        # Step 1: Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find cycle entry (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


            
            

        