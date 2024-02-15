# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_list = defaultdict(list)
        def check(root, L):
            if root:
                level_list[L].append(root.val)
                check(root.left, L+1)
                check(root.right, L+1)
        check(root, 0)
        return [level_list[i] for i in range(len(level_list))]
        