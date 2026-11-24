class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempLen = len(nums)
        if tempLen > len(set(nums)):
            return True 
        return False
        