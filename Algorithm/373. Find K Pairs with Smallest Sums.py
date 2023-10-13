'''
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k: return []

        '''
        使用priority queue
        '''

        res=[]
        heap=[]

        # 先把nums1的每一個element和nums2的第一個element index加進去priority queue
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))    # (總和, nums1 index, nums2 index)
        
        # print(f"heap:{heap}")
        while heap and k > 0:
            curr = heapq.heappop(heap)
            # print(f"curr:{curr}, k:{k}")
            res.append([nums1[curr[1]], nums2[curr[2]]])
            k-=1

            if curr[2] >= len(nums2) - 1: continue
            heapq.heappush(heap, (nums1[curr[1]] + nums2[curr[2]+1], curr[1], curr[2]+1))   # 從priority queue拿出來總和最小的值後，接著使用nums2的下一個值，因為最一開始的for迴圈 已經把nums1的三個row的值加進去
        
        return res