class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum = {0:-1}
        max_length = 0
        current_sum = 0

        for i,num in enumerate(nums):
            current_sum += 1 if num == 1 else -1 
            if current_sum in prefix_sum:
                max_length = max(max_length , i - prefix_sum[current_sum])
            else:
                prefix_sum[current_sum] = i
        return max_length

        

        
        