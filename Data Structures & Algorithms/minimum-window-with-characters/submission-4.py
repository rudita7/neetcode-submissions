class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if (r-l) +1 < resLen:
                    res = [l, r]
                    resLen = (r-l)+1

                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -=1
                l +=1 
        l , r = res
        if resLen != "infinity":
            return s[l:r+1]
        else:
            return ""
