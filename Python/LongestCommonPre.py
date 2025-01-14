class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        first_len = len(first)

        last = strs[-1]
  

        for i in range(first_len):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return ans
    

        
        



strs = ["fanower","fanlow","fanlight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))