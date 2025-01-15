class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        
        # time complexity : let n = length of given string Time complexity: O(n) Space complexity: O(n)
        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] == "[" or s[i] == "(" or s[i] == "{":
                    stack.append(s[i])
                else:
                    return False
            elif s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            elif stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif stack[-1] == "(" and s[i] == ")":
                stack.pop()
            elif stack[-1] == "{" and s[i] == "}":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False


s = "([])"
sol = Solution()
print(sol.isValid(s))

