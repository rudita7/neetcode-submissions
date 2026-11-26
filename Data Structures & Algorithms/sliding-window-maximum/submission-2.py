class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        res = []
        answer = []
        for i in range(len(nums)):
            answer.append((i, nums[i]))
        for r in range(len(nums)):
            if r-l >=  k:
                res.append(nums[dq[0]])
                l += 1
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] <= r-k:
                dq.popleft()
        
        
        res.append(nums[dq[0]])
        return res


        