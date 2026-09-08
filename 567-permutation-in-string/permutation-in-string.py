from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        #s1_count = {}
        #s2_count = {}

        k = len(s1)
        s1_count = Counter(s1)
        s2_count = Counter(s2[:k])

        #result = []

        if s1_count == s2_count:
            return True

        for right in range(k , len(s2)):
            char_in = s2[right]
            s2_count[char_in] = s2_count.get(char_in , 0) + 1

            char_out = s2[right - k]
            s2_count[char_out] -= 1
            if s2_count[char_out] == 0:
                del s2_count[char_out]

            if s1_count == s2_count:
                return True
        return False         

        
        