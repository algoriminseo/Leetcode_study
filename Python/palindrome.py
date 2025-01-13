class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
       
sol = Solution()
x = 13231
print(sol.isPalindrome(x))