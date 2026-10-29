class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevValue = {}

        for i, val in enumerate(nums):
           #get the difference between target and value
            diff = target - val
           #check if the diff is in hash
            if diff in prevValue.keys():
                return list([prevValue.get(diff), i])
            else:
                prevValue[val] = i