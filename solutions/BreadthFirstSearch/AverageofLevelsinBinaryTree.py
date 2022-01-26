# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[]
        curr=[root]
        while curr:
            q.append(curr)
            curr=[]
            for node in q[-1]:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
        val = [[node.val for node in curr] for curr in q]
        return [sum(level)/len(level)for level in vals]
