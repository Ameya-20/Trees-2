# Definition for a binary tree node.
# TC / SC - O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if node is None:
                return 0
            
            current_sum = current_sum * 10 + node.val
            
            if node.left is None and node.right is None:
                return current_sum
            
            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)
            
            return left_sum + right_sum
        
        return dfs(root, 0)
