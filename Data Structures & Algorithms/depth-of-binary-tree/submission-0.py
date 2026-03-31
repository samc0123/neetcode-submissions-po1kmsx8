# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if root == None:
            return 0 
        
        # Recursive step 
        return max(1+self.maxDepth(root=root.left),1+self.maxDepth(root=root.right))