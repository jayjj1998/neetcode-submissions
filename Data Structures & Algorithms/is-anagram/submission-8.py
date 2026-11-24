class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if lenght is the same 

        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

