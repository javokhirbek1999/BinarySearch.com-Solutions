# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node is None:
            return None
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        node = prev
        return node
