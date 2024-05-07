class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.rstrip().split(' ')
    
    # Find the length of the last word
        if words:
            return len(words[-1])
        else:
            return 0