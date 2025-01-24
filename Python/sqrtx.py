class Solution:
    # Time complexity: O(log n), where n is integer x. Since the method implements binary search and
    # decreases the extent of integers, it take logrithmic time
    # Space complexity : O(1), does not need extra space
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) //2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid -1
        return right


x = 8
sol = Solution()
print(sol.mySqrt(x))