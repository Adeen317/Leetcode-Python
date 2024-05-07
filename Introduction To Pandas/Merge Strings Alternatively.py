#Leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=''
        i=0
        for i in range(i < len(word1) and i < len(word2)):
            merge += word1[i] + word2[i]
            i+=1

            if i < len(word1):
                merge += word1[i:]
            elif i < len(word2):
                merge += word2[i:]
        
            return merge

        
        
