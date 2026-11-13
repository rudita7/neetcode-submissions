class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set()
        for num in nums:
            distinct.add(num)
        
        if len(nums) > len(distinct):
            return True
        else:
            return False