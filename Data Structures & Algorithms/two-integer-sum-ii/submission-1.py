class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = defaultdict(int)

        for i, num in enumerate(numbers):
            complement = target - num
            if prevMap[complement] != 0:
                return sorted([i+1, prevMap[complement]])
            else:
                prevMap[num] = i + 1
