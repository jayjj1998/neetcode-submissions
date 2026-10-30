class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = ''.join(sorted(s))
        top = ''.join(sorted(t))
        
        if sa != top:
            return False 
        return True 