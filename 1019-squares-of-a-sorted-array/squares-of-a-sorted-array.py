class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        arr = []
        for i in nums:
            arr.append(i**2)
        arr.sort()
        return arr    

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        