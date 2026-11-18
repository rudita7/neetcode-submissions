class Solution:
    def longestConsecutive(self, nums):
        seen = set()
        for num in nums:
            seen.add(num)
        longest = 0
        for n in seen:
            count = 1
            if n-1 in seen:
                continue
            current = n + 1
            while current in seen:
                count += 1
                current = current + 1
            if count > longest:
                longest = count

        return longest