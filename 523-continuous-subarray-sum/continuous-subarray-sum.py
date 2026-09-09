class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefixSum = { 0 : -1 }
        currentSum = 0
        for i,num in enumerate(nums):
            currentSum += num
            rem = currentSum % k
            if rem in prefixSum:
                if i - prefixSum[rem] >= 2:
                    return True
            else:
                prefixSum[rem] = i
        return False 

            

        
        