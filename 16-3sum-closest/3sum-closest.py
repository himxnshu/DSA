class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        # 1. Initialize with real numbers to avoid infinity bugs
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # 2. Correct duplicate check for anchor 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j = i + 1
            k = n - 1
            
            # 3. Two-pointer traversal
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                # Perfect match! Exit immediately
                if current_sum == target:
                    return current_sum
                
                # 4. Check if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 5. Move pointers based on sum
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
                    
        return closest_sum
        