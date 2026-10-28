class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                currentNum = num
                count = 1
            
                while (currentNum + 1) in numSet:
                    currentNum += 1
                    count += 1
                longest = max(longest, count)
        return longest

        
        