class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Time Complexity: O(n), where n is length of heystack
        # n is bigger than the length of needle.
        # It iterates through the array of heystack.
        #Therefore, it is O(n)

        #Space Complexity: O(1), since it checks for the substrings,
        #not allocating the memory
        length = len(needle)

        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i 
        return -1


haystack = "abcode"
needle = "e"
sol = Solution()
print(sol.strStr(haystack, needle))