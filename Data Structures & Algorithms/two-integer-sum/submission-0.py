class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = { }
        for i, num in enumerate(nums):
            dif = target - num
            if dif in dict1:
                return [dict1[dif], i]
            else:
                dict1[num] = i
        
        return []
