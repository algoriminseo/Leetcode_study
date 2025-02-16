#Time complexity : O(n), where n is length of the list
#Space complexity : O(1) Does not require extra space, just return the key

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        thisdict = {}
     
        for i in nums:
            thisdict[i] = 0
        
        for j in nums:
            thisdict[j] += 1
        
        for x in thisdict.keys():
            if thisdict[x] == 1:
                return x
        
    