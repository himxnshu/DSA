class Solution(object):
    def simplifyPath(self, path):
        stack = []
        tokens = path.split('/')
        for token in tokens:
            if token == "" or token == ".":
                continue
            if token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)




        