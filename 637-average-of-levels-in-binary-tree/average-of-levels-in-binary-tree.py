from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        averageList = deque()
        fifo = deque([root])
        while fifo:
            _sum = 0
            lenFifo = len(fifo)
            for _ in range(lenFifo):
                curNode = fifo.popleft()
                _sum += curNode.val
                if curNode.left != None:
                    fifo.append(curNode.left)

                if curNode.right != None:
                    fifo.append(curNode.right)
            averageList.append(_sum / lenFifo)
        return averageList        


        