class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for ch in tokens:
            if ch == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)    
            elif ch == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(ch))
        return stack[0]
               

