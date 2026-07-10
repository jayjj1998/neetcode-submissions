class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        count = 0
        total = sum(arr[0:k])
        print(total)
        if (total / k) >= threshold:
            count += 1

        for r in range(k, len(arr)):
            print(f"adding {arr[r]} sub {arr[r - k]}")
            total -= arr[r - k]
            total += arr[r]
            if (total / k) >= threshold:
                count += 1
        
        return count
