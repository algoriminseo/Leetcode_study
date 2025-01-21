class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # time complexity : O(n + m) , where n is length of array words, m is length of last word. In the first loop, 
        #it finds for the last word, so it would be expected constant time. However, in the worst case, length of s could be 1.
        #In the second loop, we need to count each character in the last word. Therefore, it is O(n + m)
        # space complexity : O(n), where n is size of array words. We do not need extra space for searching.
    
        l_length = 0
        l_words = "" 
        words = s.split(" ")
        i = len(words) - 1
        while i >= 0:
            if len(words[i]) >= 1:
                l_words = words[i]
                break
            i -= 1
        for k in l_words:
            l_length += 1
        return l_length

    

s = "   fly me   to   the moon  "
sol = Solution()
print(sol.lengthOfLastWord(s))