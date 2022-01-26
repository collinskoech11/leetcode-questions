# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isIdentical(self, T,S):
        if T is None and S is None:
            return True
        if T is None or S is None:
            return False
        #check if val of both roots is the same and value of left anf right subtrees are the same
        return T.val==S.val and self.isIdentical(T.left,S.left) and self.isIdentical(T.right,S.right)
    def isSubtree(self, T: Optional[TreeNode], S: Optional[TreeNode]) -> bool:
        if T is None:
            return False
        if S is None:
            return True
        #check the tree with root as current node
        if (self.isIdentical(T,S)):
            return True
        #if the tree with root as current node does not match, check left and right subtree one by one
        return self.isSubtree(T.left,S) or self.isSubtree(T.right,S)
