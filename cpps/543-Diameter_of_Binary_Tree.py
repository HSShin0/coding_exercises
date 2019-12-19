'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:    
        # 각 node를 정점으로, 그 left-subtree와 right-subtree를 통과하는 가장 긴 path의 길이를 저장할 list.
        self.diameters = [0]  # leaf node를 위해 0을 미리 추가해놓는다.
        self.maxDepth(root)
        return max(self.diameters)
        
    def maxDepth(self, root: TreeNode) -> int:
        '''
        root로부터 가장 깊게 내려갈 수 있는 깊이를 반환한다.
        계산 과정에서 root를 정점으로 left-subtree와 right-subtree를 통과하는 가장 긴 path 길이를 self.diameters 에 추가한다.
        '''
        if not root:
            return 0
        
        subtree_length = []
        if root.left:
            left_max = self.maxDepth(root.left)
            subtree_length.append(left_max)
        if root.right:
            right_max = self.maxDepth(root.right)
            subtree_length.append(right_max)
        if len(subtree_length) > 0:
            self.diameters.append(sum(subtree_length))
            return max(subtree_length) + 1
        else:
            return 1
