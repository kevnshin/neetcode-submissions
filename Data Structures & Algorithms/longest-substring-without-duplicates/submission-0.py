class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left:int = 0
        right:int = 0
        largest:int = 0
        currentChars:set = set()
        while (right < len(s)):
            if s[right] not in currentChars:
                currentChars.add(s[right])
                right += 1
            else:
                currentChars.remove(s[left])
                left += 1
            if len(currentChars) > largest:
                largest = len(currentChars)
        return largest