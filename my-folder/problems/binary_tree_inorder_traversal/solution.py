# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, answerList):
        if root == None : 
            return answerList
        else :
            self.check(root.left, answerList)
            answerList.append(root.val)
            self.check(root.right, answerList)
        return answerList
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.check(root, [])
        