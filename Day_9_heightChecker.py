class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h1 = sorted(heights)
        i,j,ct=0,0,0
        while(i<len(heights)):

            if(heights[i]!=h1[j]):
                ct+=1
            i+=1
            j+=1
        return ct
