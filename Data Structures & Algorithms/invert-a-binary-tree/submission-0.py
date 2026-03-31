# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Writing a simple BFS for practice 
        q = []
        q_rev = []
        if root is not None:
            q.append(root)
        while len(q) > 0:
            cur_node = q.pop(0)
            # Mark visited
            print(f"Visited Node: {cur_node.val}")
            # Add neighbors to q
            if cur_node.left is not None:
                q.append(cur_node.left)
            if cur_node.right is not None:
                q.append(cur_node.right)
            
            # Re-orient the children 
            temp_l = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = temp_l
            q_rev.append(cur_node)
        return q_rev.pop(0) if len(q_rev) > 0 else None