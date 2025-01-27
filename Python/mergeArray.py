class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Thinking backwards was the key
        
        i = m - 1
        j = n - 1
        k = m + n -1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -=1
            else:
                nums1[k] = nums2[j]
                j -=1
            k-=1
        print(nums1)



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
sol = Solution()
sol.merge(nums1, m, nums2, 3)