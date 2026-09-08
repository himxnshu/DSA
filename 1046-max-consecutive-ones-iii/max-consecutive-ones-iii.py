class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        max_zero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                max_zero += 1

            while max_zero > k:
                if nums[left] == 0:
                    max_zero -= 1
                left += 1
            max_len = max(max_len , right - left + 1)
        return max_len     

        
        