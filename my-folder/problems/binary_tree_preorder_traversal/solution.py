# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, answerList):
        # 儲存val -> left -> right
        # 走到底時回傳answerList
        if root == None : 
            return answerList
        else :
            answerList.append(root.val)
            self.preorder(root.left, answerList)
            self.preorder(root.right, answerList)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.preorder(root, answerList)
        return answerList