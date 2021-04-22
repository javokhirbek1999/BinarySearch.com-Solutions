# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.c = 0
    def solve(self, root):
        self.preOrder(root)
        return self.c

    def preOrder(self,root):
        if root is None:
            return self.c
        self.c+=1
        self.preOrder(root.left)
        self.preOrder(root.right)                 
