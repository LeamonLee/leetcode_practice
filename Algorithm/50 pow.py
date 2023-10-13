'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        這題關鍵在n可能是負的，所以一律都先把n用正數處理，最後再判斷如果是負數的話取倒數。
        '''
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            # 如果n是奇數的話，只有這樣寫會少乘一次
            # 因此return前要先判斷如果n是奇數的話還要再多乘一次x
            # Ex: 
            # 偶數: x^2 * x^2 = x^4
            # 奇數: x * x^2 * x^2 = x^5
            res = helper(x*x, n//2)
            return res*x if n%2==1 else res
        
        # if n=3, res = x*x*x
        res=helper(x, abs(n))
        return res if n>=0 else 1/res   # 是n>=0