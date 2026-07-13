class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_feq = 0
        L = 0
        freq_count = {}
        longest = 0

        for R in range(len(s)):
            if s[R] in freq_count:
                freq_count[s[R]] += 1
            else:
                freq_count[s[R]] = 1
            
            if freq_count[s[R]] > max_feq:
                max_feq += 1
            
            while (R - L + 1) - max_feq > k:
                freq_count[s[L]] -= 1
                L += 1

            longest = max(longest, R - L + 1)
        
        return longest