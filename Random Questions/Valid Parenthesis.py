class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Hash map to keep track of mappings
        mapping = {')': '(', '}': '{', ']': '['}
        
        # For every character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack if it is not empty
                # Otherwise, assign a dummy value of '#' to the top_element
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket in the mapping does not match the top element of the stack
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, it means all the opening brackets were properly matched
        return not stack
