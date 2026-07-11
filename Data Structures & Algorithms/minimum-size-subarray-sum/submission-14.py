class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_length = float('inf')
        window_sum = 0

        for R in range(len(nums)):
            window_sum += nums[R]
            while window_sum >= target:
                min_length = min(R - L + 1, min_length)
                window_sum -= nums[L]
                L += 1

        if min_length == float('inf'):
            return 0
        
        return int(min_length)