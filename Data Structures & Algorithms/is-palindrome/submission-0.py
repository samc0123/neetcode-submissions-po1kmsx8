class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_al_num = ""
        

        for char in s:
            if char.isalnum():
                s_al_num = s_al_num + char.lower()
        return s_al_num == s_al_num[::-1]