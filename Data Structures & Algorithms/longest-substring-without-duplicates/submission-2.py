class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0
        chars = set()

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            longest = max(len(chars), longest)
        
        return longest