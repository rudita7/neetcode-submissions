class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        current = 0
        for num in nums:
            if num != 1:
                current = 0
            else:
                current += 1
            if current > best:
                best = current
        return best
        