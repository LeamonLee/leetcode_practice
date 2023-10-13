'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        解題思路:把Array中每個字串做排序，然後放到dictionary裡面，key是排序過的字串，value是array
        接著把同樣排序的字串放到一個array裡面。
        '''
        # dctGroupAnagrams = {}
        dctGroupAnagrams = defaultdict(list)

        for _str in strs:
            sortedStr = ''.join(sorted(_str))
            print(f"sortedStr:{sortedStr}")
            # if sortedStr not in dctGroupAnagrams:
            #     dctGroupAnagrams[sortedStr] = [_str]
            # else:
            #     dctGroupAnagrams[sortedStr].append(_str)
            
            dctGroupAnagrams[sortedStr].append(_str)    # 如果使用defaultdict的話
        
        print(f"dctGroupAnagrams:{dctGroupAnagrams}")
        res=[]
        for anagramStr in dctGroupAnagrams.values():
            print(f"anagramStr:{anagramStr}")
            res.append(anagramStr)
        
        print(f"res:{res}")
        return res