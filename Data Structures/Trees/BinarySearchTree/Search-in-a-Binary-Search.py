# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        if root is None:
            return False
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False                    
