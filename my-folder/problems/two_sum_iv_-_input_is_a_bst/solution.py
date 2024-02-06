# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def check(root, rootList):
            if root is None:
                return False
            if (k - root.val) in rootList:
                return True
            rootList.add(root.val)  # 使用集合（set）以提高查找效率
            return check(root.left, rootList) or check(root.right, rootList)
        return check(root, set())  # 初始化一個空的集合