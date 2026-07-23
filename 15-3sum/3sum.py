class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        a = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while(j < k):
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum == 0:
                        a.append([nums[i],nums[j],nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                elif currentSum < 0:
                    j += 1
                else:
                    k -= 1                
                          
        return a
        
        