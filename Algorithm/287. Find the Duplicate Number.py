class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast: break
        
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast: break

        return slow