# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root, answerList):
        # 尋找最後的子節點(沒有左右節點) 儲存  
        # 指針到上一層父節點 尋找右邊的子節點
        if root == None : 
            return answerList
        else :
            self.postorder(root.left, answerList)
            self.postorder(root.right, answerList)
            answerList.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.postorder(root, answerList)
        return answerList