class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use 2 pointers 
        #copare the value of two pointer to make sure they match
        # the moment they dont, we brak the loop and return False 
        #we need to skip non alphanumeric chars 

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True 