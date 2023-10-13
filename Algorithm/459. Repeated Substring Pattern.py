class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sLength = len(s)
        startIndex = (sLength//2)-1
        # print(f"startIndex:{startIndex}")
        for i in range(startIndex, -1, -1):
            numString = i+1
            # print(f"numString:{numString}, sLength / numString: {sLength / numString}")
            if sLength % numString == 0:
                numGroup = int(sLength / numString)
                subString = s[:numString]
                # print(f"numString:{numString}, numGroup:{numGroup}, subString:{subString}")

                targetString = ""
                for _ in range(numGroup):
                    targetString +=subString

                if targetString == s:
                    return True

        return False 
