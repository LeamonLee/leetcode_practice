'''
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        # 建立一個array，紀錄小於n以下有哪些數不是質數。True: 不是質數, False: 是質數 
        # 預設一開始都是質數
        lstNoPrimes = [False]*n         
        res = 0

        for i in range(2, n):
            if not lstNoPrimes[i]:
                # print(f"i:{i}")
                res+=1
                
                ''' 以質數為因數去乘2,3,4...的數就不是質數。
                Ex:
                2*2, 2*3, 2*4... 
                3*2, 3*3, 3*4... 
                '''
                for j in range(2, n):
                    index = i*j
                    if index >= n:
                        break
                    
                    lstNoPrimes[index] = True
                    

        return res
