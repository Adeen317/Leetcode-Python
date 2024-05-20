class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Define the Roman numeral values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        length = len(s)
        
        for i in range(length):
            # Get the value of the current Roman numeral
            current_value = roman_values[s[i]]
            
            # If not the last character and the next character is larger, apply the subtraction rule
            if i + 1 < length and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= current_value
            else:
                total += current_value
        
        return total
        
