class Solution(object):
    def isPalindrome(self, x):
     
     liste=[rakam for rakam in str(x)]
     
     ters_liste=liste[::-1]   #listeyi ters çevirdik

     if ters_liste==liste:
       return True
     else:
        return False


solution=Solution()
print(solution.isPalindrome(121))