class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #Time complexity : O(log n) where n is length of array nums
        # Since the method tries to divide low and mid value comparing with the target, it is logrithmic 
        # Space complexity: O(1) s
        # Since it searches element in the array, it takes constant space
        index = 0
        if len(nums) == 1:
            if nums[0] < target:
                index += 1
                return index
            elif nums[0] >= target:
                return index
        else:
            low = 0
            high = len(nums)-1
            if target < nums[0]:
                return 0
            elif target > nums[high]:
                return len(nums)
            while low <= high:
                mid = low + (int)((high - low)/2) 
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    if nums[mid-1] < target:
                        return mid    
                    high = mid - 1
                else:
                    if nums[mid+1] > target:
                        return mid + 1
                    low = mid + 1

nums = [1, 3, 5, 6, 10]
target = 7
sol = Solution()
print(sol.searchInsert(nums, target))
