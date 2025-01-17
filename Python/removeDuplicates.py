class Solution:
    #Time complexity : O(n),where n is length of nums array
    #Space complexity : O(1), since it replaces duplicates with other elements
    # in the given size of the array
    def removeDuplicates(self, nums):

        
        k = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k = k + 1
                nums[k] = nums[i]
             

        
        return k+1
        



nums = [1,1,2]
sol = Solution()
print(sol.removeDuplicates(nums))