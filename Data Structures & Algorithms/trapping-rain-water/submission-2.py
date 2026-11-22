class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        waters = []
        rightMaxes = defaultdict(int)
        rightMax = height[(len(height)-1)]
        for j in range(len(height)-1, -1, -1):
            rightMax = max(height[j], rightMax)
            rightMaxes[j] = rightMax
        for i in range(1, len(height)-1):
            leftMax = max(height[i], leftMax)
            water = min(leftMax, rightMaxes[i]) - height[i]
            if water >= 0:
                waters.append(water)
        
        totals = 0
        for water in waters:
            totals = totals + int(water)
        
        return totals
            