class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_weight = 0
        apple_number = 0
        while apple_number < len(weight):
            total_weight += weight[apple_number]
            if total_weight <= 5000:
                apple_number += 1
            else:
                break
        
        return apple_number

