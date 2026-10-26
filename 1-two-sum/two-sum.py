class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in seen:
                return [seen[n] , i]
            
            seen[num] = i
        return []
            
        


        
        