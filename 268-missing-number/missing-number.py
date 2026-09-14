class Solution(object):
    def missingNumber(self, nums):
        i = 0
        n = len(nums)
        while i < n: 
            index = nums[i]
            if nums[i] < n and nums[index] != nums[i]:
                nums[i],nums[index] = nums[index],nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n


        
        