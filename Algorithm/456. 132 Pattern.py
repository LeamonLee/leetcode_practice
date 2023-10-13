class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        numK=float("-inf")
        numJ=float("-inf")

        # nums=[-1,3,2,0]
        for i in range(len(nums)-1,-1,-1):
            # if nums[i] < numK < numJ: return True
            if nums[i] < numK: return True

            while stack and nums[i] > stack[-1]:
                # numJ = nums[i]
                numK=stack.pop()
            
            stack.append(nums[i])
        
        return False