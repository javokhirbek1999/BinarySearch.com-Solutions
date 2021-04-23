# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll0, ll1):
        if not ll0 and not ll1:
            return None
        l = set()
        if not ll0 and ll1:
            return ll1
        if ll0 and not ll1:
            return ll0
        
        while ll0:
            l.add(ll0.val)
            ll0 = ll0.next
        while ll1:
            l.add(ll1.val)
            ll1 = ll1.next
        
        dummy = LLNode(0)
        tail = dummy
        for i in sorted(l):
            tail.next = LLNode(i)
            tail = tail.next
        return dummy.next
