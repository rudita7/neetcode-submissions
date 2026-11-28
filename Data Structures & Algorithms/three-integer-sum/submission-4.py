class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        answer = []
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr > 0:
                    k -= 1
                elif curr < 0:
                    j += 1
                elif curr == 0:
                    output.append(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1

        if output == []:
            return []            
        store = set(output)
        store1 = list(store)
        for s in store1:
            s = list(s)
            answer.append(s)
        return answer