from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        frequency = defaultdict(int)
        max_frequency = 0
        result = 0

        while right < len(s):
            frequency[s[right]] += 1
            max_frequency = max(max_frequency, frequency[s[right]])

            while (right - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right +=1 

        return result




        # currentCount = 0
        # longestCount = 0
        # currentChar = s[0]
        # currentK = k

        # left = 0
        # nextLeft = 0
        # right = 0

        # while right < len(s):
        #     if currentChar == s[right]:
        #         currentCount += 1
        #         right += 1
        #     else:
        #         if nextLeft == left:
        #             nextLeft = right

        #         if currentK > 0:
        #             currentCount += 1
        #             right += 1
        #             currentK -= 1
        #         else:
        #             left = nextLeft
        #             right = left
        #             currentCount = 0
        #             currentChar = s[left]
        #             currentK = k    
    
        #     longestCount = max(currentCount, longestCount)
        
        # return longestCount

            # check current char
            # if same:
                # add current count
            # else:
                # if next left == left:
                    # set next left

                # if currentK left:
                    # add currentCount
                # else:
                    # reset left to next left 
                    # reset right
                    # reset currentCount
                    # reset currentChar
                    # reset currentK
            
            # longestCount = max(currentCount, longestCount)
        