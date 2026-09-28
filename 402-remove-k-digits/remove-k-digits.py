class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
        if k > 0:
            stack = stack[:-k]
            
        res = "".join(stack).lstrip('0')
        return res if res else "0"

        
        
        