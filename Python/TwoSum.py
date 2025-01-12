class Solution(object):
    def twoSum(self, nums, target):
        i = 0
     
        indices = []
        while i < (len(nums)-1):
            k = i + 1
            while k < len(nums):
                if((nums[i] + nums[k])== target):
                    indices.append(i)
                    indices.append(k)
                    k = k + 1  
                k = k + 1
            i = i + 1
        return indices
      




num = [3, 4, 7, 8]
target = 12
sol = Solution()
print(sol.twoSum(num, target))
