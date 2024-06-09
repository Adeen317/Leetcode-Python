class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        x=0
        length=0
        for i in range(len(s)):
            if s[i] in a and a[s[i]]>=x:
                x=a[s[i]]+1
            else:
                length = max(length,i-x+1)
            
            a[s[i]] = i

        return length
        
