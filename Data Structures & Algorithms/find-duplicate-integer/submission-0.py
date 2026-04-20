class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # meeting point
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        # finding entrance
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

        