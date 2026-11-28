class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        outputs = []
        nums = sorted(nums)
        for i in range(len(nums)):
            tmp = 0 - nums[i]
            j = i + 1
            k = len(nums)-1
            while j < k:

                if nums[j] + nums[k] == tmp:
                    outputs.append(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                elif nums[j] + nums[k] < tmp:
                    j += 1
                else:
                    k -= 1
        if outputs == []:
            return []
        store = set(outputs)
        store1 = list(store)

        for s in store1:
            answer.append(list(s))
        
        return answer

