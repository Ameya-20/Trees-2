# Definition for a binary tree node.
# # TC / SC - O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        
        def build(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            index = inorder_index_map[root_val]
            
            root.right = build(index + 1, in_right)
            root.left = build(in_left, index - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
