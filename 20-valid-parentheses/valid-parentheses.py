class Solution(object):
    def isValid(self, s):
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for ch in s:
            if ch in matching:
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0

        