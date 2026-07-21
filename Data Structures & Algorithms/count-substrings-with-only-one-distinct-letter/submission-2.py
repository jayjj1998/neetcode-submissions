class Solution:
    def countLetters(self, s: str) -> int:
        sub_strings_count, L = 0, 0

        for R in range(len(s)):
            if s[L] != s[R]:
                L = R
            
            sub_strings_count += (R - L + 1)

        return sub_strings_count