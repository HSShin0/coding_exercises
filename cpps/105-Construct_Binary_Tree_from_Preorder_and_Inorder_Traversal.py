# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        val = preorder[0]
        root = TreeNode(val)
        
        sep = inorder.index(val) # the index seperating left-subtree and right-subtree
        left_inorder = inorder[ :sep]
        right_inorder = inorder[sep+1: ]
        
        left_preorder = preorder[1: 1+sep] # the first element is root
        right_preorder = preorder[1+sep: ]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root
