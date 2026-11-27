class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        isalnum = str.isalnum
        lower = str.lower
        while left < right:

            while left < right and not isalnum(s[right]):
                right -= 1
            while left < right and not isalnum(s[left]):
                left += 1
            
            if lower(s[left]) != lower(s[right]):
                return False
            right -= 1
            left += 1
        return True