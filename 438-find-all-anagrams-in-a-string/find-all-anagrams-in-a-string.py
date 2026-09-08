class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []

        p_count = {}
        s_count = {}    

        p_count = Counter(p)   #anangram ki length nikal li 
        k = len(p)
        s_count = Counter(s[:k])  #isme first k length tk alphabtes select hogye

        result = []
        
        if s_count == p_count:
            result.append(0)

        for right in range(k ,len(s)):
            char_in = s[right]
            s_count[char_in] = s_count.get(char_in,0) + 1  # toh basically isme agr char_in milta hai s_count mai toh ye {'char_in':1} aise krdega

            char_out = s[right - k]
            s_count[char_out] -= 1
            if s_count[char_out] == 0:
                del s_count[char_out]

            if s_count == p_count:
                result.append(right - k + 1)    #The formula right - k + 1 converts the end index into the start index:{Start Index} = {End Index} - {Window Length} + 1

        return result               




        
            



        