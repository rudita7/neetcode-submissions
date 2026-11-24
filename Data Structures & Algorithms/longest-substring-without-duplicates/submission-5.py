class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        res = 0
        streak = 0
        for i in range(len(s)):
            if s[i] in seen:
                if s[i-1] == s[i]:
                    seen.clear()
                    seen.append(s[i])
                elif s[i-1] != s[i]:
                    del seen[:seen.index(s[i])+1]
                    seen.append(s[i])
            else:
                seen.append(s[i])
            res = max(len(seen), res)

        return res




