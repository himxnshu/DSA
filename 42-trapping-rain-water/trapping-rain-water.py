class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        i = 0
        j = len(height) - 1

        left = 0
        right = 0
        water = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] >= left:
                    left = height[i]
                else:
                    water += left - height[i]
                i += 1 
            else:
                if height[j] >= right:
                    right = height[j]
                else:
                    water += right - height[j]
                j -= 1 
        return water         

        
        