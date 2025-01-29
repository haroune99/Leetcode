# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], counter = 1) -> int:
        if root is None:
            return 0 
        
        
        if root.left is None and root.right is None:
            return counter
        
        
        left_depth = self.maxDepth(root.left, counter + 1) if root.left else counter
        right_depth = self.maxDepth(root.right, counter + 1) if root.right else counter
        
        return max(left_depth, right_depth)


