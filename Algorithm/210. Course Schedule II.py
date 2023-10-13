class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        lstNumberPreCourses = [0] * numCourses
        queue = deque()
        res = []

        for pair in prerequisites:
            lstNumberPreCourses[pair[0]] += 1
        
        for idx, preCourse in enumerate(lstNumberPreCourses):
            if preCourse == 0:
                queue.append(idx)
                res.append(idx)
        
        while queue:
            curr = queue.pop()
            for pair in prerequisites:
                if lstNumberPreCourses[pair[0]] == 0:
                    continue

                if pair[1] == curr:
                    lstNumberPreCourses[pair[0]] -= 1
                
                if lstNumberPreCourses[pair[0]] == 0:
                    queue.append(pair[0])
                    res.append(pair[0])
        
        return res if len(res) == numCourses else []