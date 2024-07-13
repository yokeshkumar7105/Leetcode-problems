class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        li = s.split(" ")
        s1= li[0]+""
        for i in range(1,k):
            s1 = s1+" "+li[i]
        return s1
        
