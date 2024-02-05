# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answerList = []
        def check(root, answer):
            if root is None: 
                return []
            if (root.left is None and root.right is None):
                answer.append(root.val)
                if sum(answer) == targetSum: 
                    answerList.append(answer)
            else :
                check(root.left, answer+[root.val])
                check(root.right, answer+[root.val])
        check(root, [])
        return answerList