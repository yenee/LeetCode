"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: 
            return 0
        else:
            max_depth_child = 0
            for child in root.children:
                max_depth_child = max(max_depth_child, self.maxDepth(child))
        return max_depth_child + 1