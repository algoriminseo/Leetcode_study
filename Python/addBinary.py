class Solution(object):
    def addBinary(self, a, b):
      
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bin_sum = str(bin(int(a,2) + int(b, 2)))
        
        return bin_sum[2:]    




    




a = "11"
b = "1"
sol = Solution()
print(sol.addBinary(a, b))