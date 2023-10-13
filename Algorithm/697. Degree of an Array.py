class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mapNumberCount = {}
        res = 0
        currMaxCount = 0

        for i in range(len(nums)):
            if nums[i] not in mapNumberCount:
                mapNumberCount[nums[i]] = {
                    "count": 1,
                    "index": i
                }
            else:
                mapNumberCount[nums[i]]["count"]+=1
            
            if mapNumberCount[nums[i]]["count"] > currMaxCount:
                res = i - mapNumberCount[nums[i]]["index"] + 1
                currMaxCount = mapNumberCount[nums[i]]["count"]
            elif mapNumberCount[nums[i]]["count"] == currMaxCount:
                res = min(res, i - mapNumberCount[nums[i]]["index"] + 1)
            
        return res
