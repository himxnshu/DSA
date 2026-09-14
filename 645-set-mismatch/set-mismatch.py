class Solution(object):
    def findErrorNums(self, nums):
       n = len(nums)
       expectedSum = n * (n + 1) // 2
       uniqueSum = sum(set(nums))
       actualSum = sum(nums)
       missing = expectedSum - uniqueSum
       duplicate = actualSum - uniqueSum
       return [duplicate,missing]
        
        