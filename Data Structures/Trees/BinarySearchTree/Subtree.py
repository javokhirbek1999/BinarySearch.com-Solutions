# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        def similar(r,t):
            if not r and not t:
                return r == t
            if r and t:
                return r.val == t.val and similar(r.left,t.left) and similar(r.right,t.right)

        queue = [root]
        while queue:
            node = queue.pop(0)
            if similar(node,target):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

        
