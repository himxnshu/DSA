import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            ans[key].append(s)
        return list(ans.values())
            
        