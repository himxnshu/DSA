from collections import Counter
class Solution(object):
    def strStr(self, haystack, needle):
        n = len(needle)
        m = len(haystack)

        for i in range(m - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1



        
        