class Solution:
    def productExceptSelf(self, nums):
        results = []
        product = [1] * (len(nums))
        for i in range(1, len(nums)):
            product[i] = product[i-1]*nums[i-1]
            after = 1
        for i in range((len(nums)-1), -1, -1):
            product[i] = product[i] * after
            after = after * nums[i]

        return product