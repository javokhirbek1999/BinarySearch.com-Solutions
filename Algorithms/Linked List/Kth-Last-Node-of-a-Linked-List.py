# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        
        f,s = node,node
        
        for i in range(k):
            s = s.next
        
        while s.next:
            f = f.next
            s = s.next
        
        return f.val
