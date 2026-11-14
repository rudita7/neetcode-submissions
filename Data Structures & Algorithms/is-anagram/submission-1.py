class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        hashmap2 = {}
        for c in t:
            if c in hashmap2:
                hashmap2[c] += 1
            else:
                hashmap2[c] = 1
        for key, value in hashmap.items():
            if key not in hashmap2:
                return False
            elif key in hashmap2:
                if hashmap[key] != hashmap2[key]:
                    return False
        for key, value in hashmap2.items():
            if key not in hashmap:
                return False
        return True
                
            


