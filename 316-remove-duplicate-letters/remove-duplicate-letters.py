class Solution(object):
    def removeDuplicateLetters(self, s):
        lastOcurr = {ch:i for i ,ch in enumerate(s)}
        stack = []
        seen = set()
        for i,ch in enumerate(s):
            if ch in seen:
                continue
            while stack and stack[-1] > ch and lastOcurr[stack[-1]] > i:
                popp = stack.pop()
                seen.remove(popp)
            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)
        
        