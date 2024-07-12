class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        rc=0
        lc=0
        ans=0

        for i in range(len(s)):
            if s[i] == 'R':
                rc+=1
            else: lc+=1
            if(rc==lc):ans+=1
        return ans
