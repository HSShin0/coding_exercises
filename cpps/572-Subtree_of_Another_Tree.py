# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        q = queue.Queue()
        q.put(s)
        
        while q.qsize() > 0:
            s = q.get()
            if s.left:
                q.put(s.left)
            if s.right:
                q.put(s.right)
            if (s.val == t.val):
                if self.isEqual(s,t):
                    return True
        return False
        
        
    def isEqual(self, s: TreeNode, t: TreeNode) -> bool:
        #################################################
        ## Any other idea?
        #################################################
        q_s = queue.Queue()
        q_s.put(s)
        
        q_t = queue.Queue()
        q_t.put(t)
        
        while q_s.qsize() > 0:
            s = q_s.get()
            t = q_t.get()
            # 각 val가 일치하지 않는 것이 나올 경우, False를 반환한다.
            if not s.val == t.val:
                return False
            
            
            if s.left:
                q_s.put(s.left)
            if t.left:
                q_t.put(t.left)
            if not q_s.qsize() == q_t.qsize():
                return False
            
            if s.right:
                q_s.put(s.right)
            if t.right:
                q_t.put(t.right)
            if not q_s.qsize() == q_t.qsize():
                return False
            
        return True
