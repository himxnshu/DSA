class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        i = 0
        j = 0
        k = n-1

        while (j <= k):
            if nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[k],nums[j] = nums[j],nums[k]
                k -= 1

        return nums                            