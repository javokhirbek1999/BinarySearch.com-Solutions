# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        if head is None:
            return False
        if head.next is None:
            return True
        current = head
        while current.next:
            if current.val >= current.next.val:
                return False
            current = current.next
        return True
        

        
