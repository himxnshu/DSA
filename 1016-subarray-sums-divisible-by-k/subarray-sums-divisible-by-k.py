class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefixRem = {0 : 1}

        count = 0
        currentSum = 0

        for num in nums:
            currentSum += num

            rem = currentSum % k

            if rem in prefixRem:
                count += prefixRem[rem]

            prefixRem[rem] = prefixRem.get(rem , 0) + 1

        return count



        