class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)  # Convert string to a list to allow mutation

        while True:
            digit_found = False
            for i in range(len(s)):
                if s[i].isdigit():
                    digit_found = True
                    left_index = i - 1
                    while left_index >= 0 and s[left_index].isdigit():
                        left_index -= 1
                    if left_index >= 0:
                        s.pop(i)  
                        s.pop(left_index)
                    else:
                        s.pop(i)
                    break 

            if not digit_found:
                break

        return ''.join(s)  

        
