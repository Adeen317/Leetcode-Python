class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Iterate over the other strings in the array
        for string in strs[1:]:
            # Find the minimum length between the current prefix and the current string
            min_length = min(len(prefix), len(string))
            # Initialize an index to track the length of the common prefix
            i = 0
            # Compare characters until they differ or we reach the end of one of the strings
            while i < min_length and prefix[i] == string[i]:
                i += 1
            # Update the prefix to the common part found
            prefix = prefix[:i]
            # If the prefix becomes empty, return immediately
            if not prefix:
                return ""
    
        return prefix
