class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in nums:
            li.append(i*i)

        li.sort()
        return li
