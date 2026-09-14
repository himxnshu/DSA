class Solution(object):
    def findDuplicates(self, nums):
        duplicates = set()
        for num in nums:
            n = abs(num) - 1
            if nums[n] < 0:
                duplicates.add(abs(num))
            else:
                nums[n] = -nums[n]
        return sorted(list(duplicates))

        