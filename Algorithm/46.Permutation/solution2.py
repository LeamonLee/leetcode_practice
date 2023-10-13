class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res=[]

        # '''
        # [1] -> [1,2], [2,1] -> [3,1,2], [1,3,2], [1,2,3]
        # '''

        # def dfs(perms, i):
        #     print(f"perms:{perms}, i:{i}")
        #     if len(perms) == len(nums):
        #         print(f"Found perms:{perms}")
        #         res.append(perms)
        #         return

            
        #     for j in range(i+1):
        #         print(f"j:{j}")
        #         tmp = perms.copy()
        #         tmp.insert(j, nums[i])
        #         dfs(tmp, i+1)         
 
        
        # dfs([], 0)
        # return res

        res = []
        nTotalLength = len(nums)
        '''
        perms:[] -> [1] -> [1,2]
        remains:[1,2,3] -> [2,3] -> [3]
        '''

        def dfs(perms, remains):
            print(f"perms:{perms}, remains:{remains}")
            if len(perms) == nTotalLength:
                print(f"Found perms:{perms}")
                res.append(list(perms))
                print(f"res:{res}")
                return

            for i in range(len(remains)):
                ''' Solution1 '''
                # num = remains.pop(0)
                # perms.append(num))
                # dfs(perms, remains)
                # perms.pop()
                # remains.append(num)

                ''' Solution2 '''
                perms.append(remains[i])
                dfs(perms, remains[:i] + remains[i+1:])
                perms.pop()

            return
        
        dfs([], nums)
        print("Finish")
        print(f"res:{res}")
        return res

        

