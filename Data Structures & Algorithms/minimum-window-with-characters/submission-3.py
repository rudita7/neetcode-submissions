class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        l = 0
        output = []
        for i in range(len(t)):
            count_t[t[i]] += 1
        
        for r in range(len(s)):

            count_s[s[r]] += 1
            valid = True 
            for key in count_t:
                if count_t[key] > count_s[key]:
                    valid = False
                    break
            if valid:
                output.append((len(s[l:r+1]), s[l:r+1]))
                while count_s[s[l]] > count_t[s[l]] and l < r:

                    count_s[s[l]] -= 1
                    l += 1 
                output.append((len(s[l:r+1]), s[l:r+1]))

    
        output = sorted(output)
        if output == []:
            return ""
        return output[0][1]
