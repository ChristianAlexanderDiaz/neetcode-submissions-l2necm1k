class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def backtrack(state, i):
            if i == len(digits):
                result.append("".join(state))
                return

            for letter in mapping[digits[i]]:
                state.append(letter)
                backtrack(state, i + 1)
                state.pop()
    
        
        backtrack([], 0)
        return result