class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            if ch in "+-*/" or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    top = stack.pop()
                    stack.append(int(float(top) / num))
                op = ch
                num = 0
        return sum(stack)

                



        