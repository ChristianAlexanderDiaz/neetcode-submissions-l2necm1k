# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.list = []

        # def dfs(root):
        #     if root is None:
        #         return None

        #     dfs(root.left)
        #     self.list.append(root.val)
        #     dfs(root.right)

        # dfs(root)
        # return self.list[k-1]
        self.count = 0
        self.result = None

        def dfs(node):
            if node is None or self.result is not None:
                return
            
            dfs(node.left)

            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.result