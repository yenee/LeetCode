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
            self.check(root.right, answerList)
            answerList.append(root.val)
        return answerList

    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return count
        answerList = self.check(root, [])
        if sum(answerList) // len(answerList) == root.val:
            count += 1
        count += self.averageOfSubtree(root.left)
        count += self.averageOfSubtree(root.right)
        return count
