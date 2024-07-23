class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {} 
        for i in nums:
            d[i] = d.get(i,0)+1
        #print (d)

        sorted_d = sorted(d.items(), key=lambda x: (x[1], -x[0]))

        #print(sorted_d)

        num1=[]
        for key,ct in sorted_d:
            num1.extend([key]*ct)
        
        #print(nums)
        return num1
