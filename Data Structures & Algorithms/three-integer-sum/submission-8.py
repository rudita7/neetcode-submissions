class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, a in enumerate(nums):
            if a >0:
                break
            j = i+1
            k = len(nums) -1 
            if i >0 and a == nums[i-1]:
                continue
            while j < k:

                threeSum = a + nums[j] + nums[k]
                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k  -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res 