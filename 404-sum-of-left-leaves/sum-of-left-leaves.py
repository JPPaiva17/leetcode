from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        
        if root.left == None and root.right == None:
            return 0
    
        totalSum = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            left_son = node.left
            
            if left_son and left_son.right == None and left_son.left == None:
                totalSum += left_son.val
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        return totalSum           