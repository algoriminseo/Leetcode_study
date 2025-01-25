

class Solution:
    #Memoization
    #Time complexity : O(n) where n is the input n 
    #Since the method iterates until n is 1 or 2, it will take linear time
    #Space complexity : O(1), no extra space needed

    # def __init__(self):
    #     self.dict = {1:1, 2:2}
    # def climbStairs(self, n: int) -> int:
    #     if n in self.dict:
    #         return self.dict[n]
    #     self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    #     return self.dict[n]
    
    
    #Iterative sol
    def climbStairs(self, n: int) -> int:
        result = 0
        temp1 = 1
        temp2 = 2
        if n == temp1 or n == temp2:
            return n
        else:
            for i in range(3, n+1):
                result = temp1 + temp2
                temp1 = temp2
                temp2 = result
        return result
    



n = 5
sol = Solution()
print(sol.climbStairs(n))
