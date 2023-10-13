class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lstPrerequisites = [0] * numCourses
        queue = deque()

        for pair in prerequisites:
            lstPrerequisites[pair[0]] += 1
        
        for idx, preCourse in enumerate(lstPrerequisites):
            if preCourse == 0:
                queue.append(idx)
        
        while len(queue) > 0:
            curr = queue.popleft()
            for pair in prerequisites:
                if lstPrerequisites[pair[0]] == 0:
                    continue
                if pair[1] == curr:
                    lstPrerequisites[pair[0]] -= 1
                
                if lstPrerequisites[pair[0]] == 0:
                    queue.append(pair[0])
        
        for preCourse in lstPrerequisites:
            if preCourse != 0:
                return False
        
        return True

