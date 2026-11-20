class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap and prevMap[diff] != i:
                return sorted([i, prevMap[diff]])
            else:
                prevMap[num] = i