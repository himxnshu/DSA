from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        count = Counter(s)
        for ch,i in count.items():
            if i < k:
                return max(self.longestSubstring(sub,k) for sub in s.split(ch))
        return len(s)
      
        
        

        