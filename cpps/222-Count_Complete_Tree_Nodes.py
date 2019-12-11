# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        dir_q = queue.Queue()
        
        while root.left:
            direction = self.directionLastNode(root)
            dir_q.put(direction)
            if direction == 0:
                root = root.left
            else:
                root = root.right
                
        depth = dir_q.qsize()
        
        count = 0
        while dir_q.qsize() > 0:
            x = dir_q.get()
            count = 2*count + x
        
        return count + 2**depth
        
        
    def directionLastNode(self, root: TreeNode) -> int:
        """
        Gives the "direction" to the last node.
        0 means left-subtree, 1 means right-subtree of the node root
        """
        if not root.left:   # root가 leaf일 때. (complete binary tree)
            return None
        else:
            left_node = root.left
        
        if root.right:
            right_node = root.right
        else:    # right-subtree 없는 경우, root.left가 leaf 가 된다. (complete binary tree)
            return 0
        
        
        # root.left, root.right 둘 다 존재하는 경우, 아래 코드가 실행된다.
        depth_l = 0    # root에서 left-subtree를 따라가며 측정하는 depth
        while root.left:
            depth_l += 1
            root = root.left
        
        depth_r = 1    # right_root에서부터 left-subtree를 이용해서 측정하는 depth
        root = right_node
        while root.left:
            depth_r += 1
            root = root.left
            
        if depth_l == depth_r: 
            return 1
        else:
            return 0
        
