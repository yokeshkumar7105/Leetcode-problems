class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s1=""
        for i in digits:
            s1=s1+str(i)
        print(s1)
        s2 = str(int(s1)+1)
        li=[]
        for i in s2:
            li.append(int(i))
        return li
