class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only letters and numbers, and convert to lowercase
        cleaned = "".join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
        return cleaned == cleaned[::-1]