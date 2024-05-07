class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(substring, string):
            n = len(string) // len(substring)
            return substring * n == string

        # Ensure str1 is shorter or equal in length
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        # Iterate through possible lengths of substrings
        for length in range(len(str1), 0, -1):
            if len(str1) % length == 0 and len(str2) % length == 0:
                substring = str1[:length]
                if is_divisor(substring, str1) and is_divisor(substring, str2):
                    return substring
        return ""
        
