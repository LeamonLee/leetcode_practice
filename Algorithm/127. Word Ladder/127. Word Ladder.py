from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        wordSet = set(wordList)
        q = deque()
        q.append(beginWord)
        level = 1
        # if beginWord in wordSet:
        #     wordSet.remove(beginWord)
        while q:
            q_size = len(q)
            for _ in range(q_size):
                word = q.popleft()
                isFound = False
                
                for i in range(len(word)):
                    for c in range(ord('a'), ord('z')+1):
                        c = chr(c)
                        newWord = word[:i] + c + word[i+1:]
                        # newWord = list(word)
                        # newWord[i] = c
                        # newWord = "".join(newWord)
                        
                        # print(f"newWord: {newWord}")
                        if newWord in wordSet:
                            print(f"Found word: {newWord}, level:{level}")
                            if newWord == endWord: return level + 1
                            
                            q.append(newWord)
                            wordSet.remove(newWord)
                            isFound = True
                            # level+=1
                    
                    # if isFound:
                    #     break
                # if isFound:
                #     level+=1
            level+=1
        
        return 0

'''
    beginWord="a"
    endWord="c"
    wordList=["a","b","c"]

    Expected = 2 # "a" -> "c"

    beginWord="hot"
    endWord="dog"
    wordList=["hot","dog","dot"]
    Expected = 3    # "hot" -> "dot" -> "dog"
'''

beginWord="hit"
endWord="cog"
wordList=["hot","dot","dog","lot","log","cog"]
Expected = 5

a = Solution()
res = a.ladderLength(beginWord, endWord, wordList)
print(f"res:{res}")