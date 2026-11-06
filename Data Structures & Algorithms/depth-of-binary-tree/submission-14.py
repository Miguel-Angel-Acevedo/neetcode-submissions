# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        q = deque([root])
        res = 0

        while q:

            for i in range (len(q)):
                curr_node = q.popleft()

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res += 1

        return res
                