'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"

-
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f, nums = [1], [0]      # 0的階層是1，把結果放入f。nums代表目前跑到階層幾了
        for i in range(1,n+1):
            f.append(i*f[i-1])  # Ex:3!=3*2!
            nums.append(i)
        
        res=[]
        # 假設n=5總共有120種(5!)，第一個數字分別為1~5，1xxxx,2xxxx,3xxxx,4xxxx,5xxxx，
        # 因此要從4!有幾種開始算
        # 假設k=49，49/24=2.xxx，等於在第三堆，也就是3xxxx這一團，因此需使用math.ceil無條件進位
        for i in range(n-1, -1, -1):
            nth = math.ceil(k / f[i])
            res.append(nums.pop(nth))
            k = k - (nth-1)*f[i]        # 假設k=49，k=49-2*24=1
        
        return "".join(map(str, res))