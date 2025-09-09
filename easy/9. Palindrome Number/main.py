class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        reversed_value = value[::-1]
        if value == reversed_value:
            return True
        else:
            return False


        
