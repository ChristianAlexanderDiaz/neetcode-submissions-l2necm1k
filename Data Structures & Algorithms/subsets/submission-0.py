class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                result.append(path[:])
                return
            
            backtrack(i+1)

            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        
        backtrack(0)
        return result