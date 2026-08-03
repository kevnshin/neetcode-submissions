from collections import defaultdict
class Solution:
    map
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:dict[List[int]:List[str]] = {}

        for word in strs:
            key = self.tranformToListStr(word)
            if key in groups:
                groups[key].append(word)
            else:

                groups[key] = [word]
        
        return list(groups.values())

    def tranformToListStr(self, word:str) -> Tuple[int]:
        result = [0] * 26
        for char in word:
            result[self.transformToIndex(char)] += 1
        return tuple(result)


    def transformToIndex(self, s:str) -> int:
        return ord(s) - ord('a')

    

        
        