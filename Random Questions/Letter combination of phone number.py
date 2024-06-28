class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        queue = deque([''])

        for digit in digits:
            letters = phone_map[digit]
            for _ in range(len(queue)):
                combination = queue.popleft()
                for letter in letters:
                    queue.append(combination + letter)

        return list(queue)
            
