from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Frequency = self.tranformToListStr(s1)
        left, right = 0, len(s1)
        s2Frequency = self.tranformToListStr(s2[left:right])
        while right <= len(s2):
            if s1Frequency == s2Frequency:
                return True
            s2Frequency[self.transformToIndex(s2[left])] -= 1
            left += 1
            right += 1
            if right <= len(s2):
                s2Frequency[self.transformToIndex(s2[right - 1])] += 1
        return False

    def tranformToListStr(self, word:str) -> List[int]:
        result = [0] * 26
        for char in word:
            result[self.transformToIndex(char)] += 1
        return result


    def transformToIndex(self, s:str) -> int:
        return ord(s) - ord('a')
