'''
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        if x%10==0 and x!= 0: return False  # 10, 100, 1000...etc.

        '''
        解題思路:如果x=121，則從個位數開始往上加，
        因此最後得出來的121的百位數的1，其實是x的個位數。
        '''
        res=0
        x_ori = x
        while x != 0:
            digit = x % 10          # 求出個位數
            res = res*10 + digit    # 將palindrome數字*10後，加上個位數。Ex: res=1, digit=1, newRes=res*10+digit=11 
            x //= 10                # 將原本數字除以10
        
        # print(f"res:{res}, x:{x}, x_ori:{x_ori}")
        return res==x_ori