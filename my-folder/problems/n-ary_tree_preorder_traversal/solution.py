"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answerList = []
        def check(root):
            if root:
                answerList.append(root.val)
                for child in root.children:
                    check(child)
        check(root)
        return answerList