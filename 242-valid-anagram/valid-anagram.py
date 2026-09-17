from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for charS , charT in zip(s,t):
            counts[ord(charS) - ord('a')] += 1
            counts[ord(charT) - ord('a')] -= 1
        return all(count == 0 for count in counts)
        
        