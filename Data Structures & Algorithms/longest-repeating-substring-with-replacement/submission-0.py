class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return None
        l = 0
        res = 0
        frequency = defaultdict(int)
        for r in range(len(s)):
            frequency[s[r]] += 1
            replacements = ((r-l)+1) - max(frequency.values())

            while replacements > k:
                frequency[s[l]] -= 1
                l += 1
                replacements = ((r-l)+1) - max(frequency.values())
            res = max(res, (r-l)+1)
        
        return res


