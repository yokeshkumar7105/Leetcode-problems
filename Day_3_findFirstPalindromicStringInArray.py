class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if (i[::-1] == i):
                return i
            else:continue
        return ""
