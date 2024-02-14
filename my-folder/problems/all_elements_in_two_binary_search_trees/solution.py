# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def check(root):
            if root is None:
                return []
            else:
                return check(root.left) + [root.val] + check(root.right)
        return sorted(check(root1)+check(root2))
        