class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                temp = []
                # Pop characters until '(' is found
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis '('
                stack.pop()
                # Reverse the characters and push them back to the stack
                stack.extend(temp)
            else:
                stack.append(char)
        
        # Join all characters to form the final result
        return ''.join(stack)


        
