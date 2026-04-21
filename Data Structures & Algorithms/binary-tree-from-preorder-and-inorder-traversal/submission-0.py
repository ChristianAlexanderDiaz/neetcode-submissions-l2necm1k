# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder_slice, inorder_slice):
            if not preorder_slice:
                return None

            root = TreeNode(preorder_slice[0])
            index = inorder_slice.index(preorder_slice[0])

            left_in = inorder_slice[:index]
            right_in = inorder_slice[index+1:]

            left_pre = preorder_slice[1:1 + len(left_in)]
            right_pre = preorder_slice[1 + len(left_in):]

            root.left = dfs(left_pre, left_in)
            root.right = dfs(right_pre, right_in)

            return root

        return dfs(preorder, inorder)