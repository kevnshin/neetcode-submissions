class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict: dict[int, int] = {}
        for str in s:
            if str in sDict:
                sDict[str] += 1
            else:
                sDict[str] = 1
        
        for str in t:
            if str in sDict:
                sDict[str] -= 1
                if sDict[str] == 0:
                    del sDict[str]
            else:
                return False

        for key, value in sDict.items():
            if value > 0:
                return False
        return True
        