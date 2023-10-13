class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return False

        def getNext(index):
            fast = (index + nums[index]) % len(nums)
            if fast >= 0:
                return fast
            else:
                return fast+len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:return False

            slow = i
            fast = getNext(i)
            print(f"slow:{slow}, fast:{fast}, nums[slow]*nums[fast]:{nums[slow]*nums[fast]}")
            while nums[slow] * nums[fast] > 0:
                if slow == fast:
                    if slow == getNext(slow): break
                    return True
                if nums[fast] * nums[getNext(fast)] < 0: break

                slow = getNext(slow)
                fast = getNext(getNext(fast))
            
        return False
                