class Solution(object):
    def findDisappearedNumbers(self, nums):
        numSet = set(nums)
        n = len(nums)
        return [i for i in range(1 , n + 1) if i not in numSet]
        
        
        