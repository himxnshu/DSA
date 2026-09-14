class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i,num in enumerate(nums):
            n ^= i ^ num
        return n

        
        
        
        