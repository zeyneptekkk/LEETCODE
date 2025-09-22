class Solution(object):
    def lengthOfLastWord(self, s):
       
       kelimeler=s.split()
       return len(kelimeler[-1])