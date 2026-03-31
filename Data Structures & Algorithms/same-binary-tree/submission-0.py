# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Pseudocode 
        # need to find 2 equal trees 
        # How? Bc trees have the same value nodes at the same places 
        # 

        # End Pseudocode

        def dfs(p_tree,q_tree):
            if p_tree is None and q_tree is None:
                return True
            elif p_tree is None or q_tree is None:
                return False
            elif p_tree.val != q_tree.val:
                return False
            
            if dfs(p_tree.left,q_tree.left) == True and dfs(p_tree.right,q_tree.right) == True:
                return True
            else:
                return False 
        return dfs(p,q)
            

            
        