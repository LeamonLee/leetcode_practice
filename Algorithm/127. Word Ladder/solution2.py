from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        print(f"nei: {nei}")    # nei = {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot', 'hit'] }

        visit = set([beginWord])
        q = deque([beginWord])
        level = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            
            level+=1
        
        return 0

beginWord="hit"
endWord="cog"
wordList=["hot","dot","dog","lot","log","cog"]
Expected = 5

a = Solution()
res = a.ladderLength(beginWord, endWord, wordList)
print(f"res:{res}")