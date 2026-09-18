from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        x = defaultdict(list)
        for i in strs:
            key =  "".join(sorted(i))
            x[key].append(i)
        return list(x.values())
         
        
        