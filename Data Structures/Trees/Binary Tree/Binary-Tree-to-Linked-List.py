# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        if root is None:
            return None
        dummy = LLNode(0)
        tail = dummy
        vals = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for i in sorted(vals):
            tail.next = LLNode(i)
            tail = tail.next
        return dummy.next                
