# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, nums):
        if not nums:
            return None
        rootIndex = len(nums)//2
        root = Tree(nums[rootIndex])
        root.left = self.solve(nums[:rootIndex])
        root.right = self.solve(nums[rootIndex+1:])
        return root
      
