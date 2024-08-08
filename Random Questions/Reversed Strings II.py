class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        
        for i in range(0, n, 2 * k):
            chunk = s[i:i + 2 * k]
            
            # Split into the first k characters and the remaining
            first_k = chunk[:k]
            rest = chunk[k:]
            
            result.append(first_k[::-1] + rest)
        
        return ''.join(result)
        
