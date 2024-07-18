class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l1=[]

        for i in range(len(nums)):
            if (nums[i]%2 == 0):
                l1.append(nums[i])
        #print(nums)
        for j in range(len(nums)):
            if(nums[j]%2!=0):
                l1.append(nums[j])
        #print(nums)
        return l1
        
