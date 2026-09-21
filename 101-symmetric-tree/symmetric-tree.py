from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return False
        
        left_row = deque([root.left])
        right_row = deque([root.right])
        
        while left_row and right_row:
            left_node = left_row.popleft()
            right_node = right_row.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node or left_node.val != right_node.val:
                return False
                
            left_row.append(left_node.left)
            left_row.append(left_node.right)
                    
            right_row.append(right_node.right)
            right_row.append(right_node.left)

        return True