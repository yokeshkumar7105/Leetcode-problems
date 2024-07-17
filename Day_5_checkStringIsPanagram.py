class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        string = "abcdefghijklmnopqrstuvwxyz"
        s1="".join(sorted(sentence))
        s2 = "".join(sorted(set(s1)))
        #print(s2)
        if (string == s2.lower()): return True
        else: return False
