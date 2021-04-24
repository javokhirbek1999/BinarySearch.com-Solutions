# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        ind = 0
        current_ind = -1
        current = node
        while current:
            if current.val == target:
                current_ind = ind
            current = current.next
            ind += 1
        if current_ind == -1:
            return node
        if current_ind == 0:
            return node.next
        if ind == 1 and current_ind != -1:
            return None
        current = node
        t = 0
        while current:
            if t == current_ind-1:
                break
            current = current.next
            t += 1
        next_node = current.next
        current.next = next_node.next
        return node
