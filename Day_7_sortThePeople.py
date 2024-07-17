class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i]<heights[j]:
                    temp = heights[i]
                    heights[i]=heights[j]
                    heights[j]=temp
                    temp1=names[i]
                    names[i]=names[j]
                    names[j]=temp1

        return names
