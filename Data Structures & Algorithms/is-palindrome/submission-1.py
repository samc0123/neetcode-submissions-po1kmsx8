class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        # Lower all of s 
        s = s.lower()
        while l < r:
            # Check that chars are alpha numeric 
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
        
            if s[l] != s[r]:
                print(s[l])
                print(s[r])
                return False
            r -= 1
            l += 1
            print(l)
            print(r)
        return True