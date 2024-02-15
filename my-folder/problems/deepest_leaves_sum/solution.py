# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxlevel = 0
        maxlevel_list = defaultdict(int)
        def check(root, level):
            nonlocal maxlevel
            if root:
                check(root.left, level+1)
                check(root.right, level+1)
                maxlevel = max(maxlevel, level)
                if maxlevel == level:
                    maxlevel_list[maxlevel] += root.val
        check(root, 0)
        return maxlevel_list[maxlevel]