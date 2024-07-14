class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        while(len(nums)>0):
            a1=min(nums)
            a = nums.remove(a1)
            b1=min(nums)
            b = nums.remove(b1)
            li.append(b1)
            li.append(a1)
        return li
        
