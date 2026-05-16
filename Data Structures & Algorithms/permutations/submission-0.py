class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def backtrack(state, used):
            if len(state) == len(nums):
                result.append(state.copy())
                return

            for num in nums:
                if num in used:
                    continue
                else:
                    state.append(num)
                    used.add(num)

                    backtrack(state,used)

                    state.pop()
                    used.remove(num)

        backtrack([], used)
        return result
