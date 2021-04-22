# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return 
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                node.left,node.right = node.right,node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

        
