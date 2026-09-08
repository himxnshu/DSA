class Solution(object):
    def totalFruit(self, fruits):
        count = {}
        left = 0
        max_fruit = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit ,0 ) + 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1
            max_fruit = max(max_fruit, right - left + 1)
        return max_fruit


        
        