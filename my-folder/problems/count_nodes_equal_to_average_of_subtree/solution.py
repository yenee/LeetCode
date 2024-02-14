# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def check(self, root):
        if root == None : 
            return 0, 0
        else :
            total_l, num_l = self.check(root.left)
            total_r, num_r = self.check(root.right)
            total = total_l + total_r + root.val
            num = num_l + num_r + 1
            if total // num == root.val:
                self.count += 1
        return total, num
    
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.check(root)
        return self.count