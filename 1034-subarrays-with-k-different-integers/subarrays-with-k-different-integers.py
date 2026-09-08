class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(dl):
            if dl <= 0:
                return 0

            result = {}
            left = 0
            total_subarray = 0
        
            for right in range(len(nums)):
                r = nums[right]
                result[r] = result.get(r, 0 ) + 1

                while len(result) > dl:
                    l = nums[left]
                    result[l] -= 1
                    if result[l] == 0:
                        del result[l]
                    left += 1

                total_subarray += right - left + 1

            return total_subarray

        return atMost(k) - atMost(k-1)

        
        