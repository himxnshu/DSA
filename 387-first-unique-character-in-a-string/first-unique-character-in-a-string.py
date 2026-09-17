from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        for i,ch in enumerate(s):
            if count[ord(ch) - ord('a')] == 1:
                return i
        return -1


        
        