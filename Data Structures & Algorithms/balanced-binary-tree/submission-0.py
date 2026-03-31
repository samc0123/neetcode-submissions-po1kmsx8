# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced_flag = True
        # Height
        def dfs(node):
            # Base case 
            if node == None:
                return 0
            
            # Get the left height 
            l_height = dfs(node.left)
            # Get the right height 
            r_height = dfs(node.right)
            
            # Check the abs 
            if abs(l_height-r_height) > 1:
                self.balanced_flag = False
            return 1 + max(l_height,r_height)
            
        dfs(root)
        return self.balanced_flag
        