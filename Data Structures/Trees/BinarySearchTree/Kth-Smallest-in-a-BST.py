# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        vals = []
        current = root
        if current is None:
            return vals
        queue = [root]    
        while queue:
            node = queue.pop(0)
            vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sorted(vals)[k]                 
