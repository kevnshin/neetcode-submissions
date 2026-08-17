from collections import defaultdict
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)
        for s in s1:
            s1Map[s] += 1
        foundLetterInS1 = False
        print('s1Map', s1Map)
        
        left, right = 0, 0
        s1MapCopy = None
        while right < len(s2):
            if s2[right] in s1Map:
                print('right', right)
                print('s2[right]', s2[right])
                print('left', left)
                print('s2[left]', s2[left])
                if not foundLetterInS1:
                    foundLetterInS1 = True
                    s1MapCopy = copy.deepcopy(s1Map)
                else:
                    if s1MapCopy[s2[right]] == 0:
                        s1MapCopy[s2[left]] += 1
                        left += 1
                        continue
                    
                s1MapCopy[s2[right]] -= 1
            else:
                foundLetterInS1 = False
            if s1MapCopy:
                print('s1MapCopy', s1MapCopy)
            
            if foundLetterInS1 and all(value == 0 for value in s1MapCopy.values()):
                return True

            right += 1
            if not foundLetterInS1:
                left +=1

        # for s in s2:
        #     if s in s1Map:
        #         if not foundLetterInS1:
        #             foundLetterInS1 = True
        #             s1MapCopy = copy.deepcopy(s1Map)

        #         s1MapCopy[s] -= 1
        #         if s1MapCopy[s] == 0:
        #             del s1MapCopy[s]
        #     else:
        #         foundLetterInS1 = False
        #     if foundLetterInS1 and len(s1MapCopy) == 0:
        #         return True
        return False
