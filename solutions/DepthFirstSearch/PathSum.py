#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            return (dfs(node.left,currSum) or
                    dfs(node.right,currSum)) 
            
        return dfs(root, 0)    
    
    
    # solution2
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum==0
        else:
            return self.hasPathSum(root.left,targetSum) or  self.hasPathSum(root.right,targetSum)
