class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cl_s = ''.join(c for c in s if c.isalnum())
        print(cl_s)
        for i in range(len(cl_s)):
            if i == ((len(cl_s)-1)/2):
                break
            j = ((len(cl_s)-1)-i)
            if cl_s[i] != cl_s[j]:
                return False
        
        return True
