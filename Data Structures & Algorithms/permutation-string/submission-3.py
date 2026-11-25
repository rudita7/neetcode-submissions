class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        for c in s1:
            count_s1[c] += 1
        
        l = 0
        counts = defaultdict(int)
        for r in range(len(s2)):
            counts[s2[r]] += 1
            if (r-l)+1 == len(s1):

                if counts == count_s1:
                    return True
                else:
                    counts[s2[l]] -= 1
                    if counts[s2[l]] == 0:
                        counts.pop(s2[l])
                    l += 1
        return False
            
        