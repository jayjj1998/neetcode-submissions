class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while (r - l) > 1:
            m = (l + r) // 2
            if nums[l] > nums[r]:
                if nums[m] > nums[l]:
                    l = m
                elif nums[m] < nums[r]:
                    r = m
            else:
                return nums[0]

        
        return min(nums[l], nums[r])
        