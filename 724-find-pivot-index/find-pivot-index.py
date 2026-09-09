class Solution(object):
    def pivotIndex(self, nums):
        leftSum = 0
        totalSum = sum(nums)

        for i,num in enumerate(nums):
            if leftSum == totalSum - leftSum - num:
                return i
            leftSum += num
        return -1


        

        