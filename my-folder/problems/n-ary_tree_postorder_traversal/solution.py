"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answerList = []
        def check(root):
            if root:
                for child in root.children:
                    # print(child)
                    check(child)
                answerList.append(root.val)
                print(root.val)
        check(root)
        return answerList
        