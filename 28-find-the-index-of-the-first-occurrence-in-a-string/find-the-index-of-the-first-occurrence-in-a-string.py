class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)  

        if needle=="":
            return 0

        for i in range(len(haystack)-len(needle)+1):
              if haystack[i:i+len(needle)]==needle:
                return 0
              else:
                return -1
        