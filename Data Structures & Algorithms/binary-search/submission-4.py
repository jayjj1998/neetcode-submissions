class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        return self.search_deeper(nums, target, l, r)

    def search_deeper(self, nums: List[int], target: int, l: int, r: int) -> int:
        m = (l + r) // 2
        if l > r:
            return -1
        
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.search_deeper(nums, target, l, m - 1)
        else:
            return self.search_deeper(nums, target, m + 1, r)