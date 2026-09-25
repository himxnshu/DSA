class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"

        res = "1"
        
        for _ in range(n-1):
            i = 0
            next_seq = []

            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                next_seq.append(str(count))
                next_seq.append(res[i])
                i += 1
            res = "".join(next_seq)
        return res


        
        
        