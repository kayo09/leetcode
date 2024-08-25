# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def __init__(self):
        self.nums=[]
    def postorderTraversal(self, root):
        
        if root==None:
            return self.nums
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.nums.append(root.val)
        return self.nums
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
solution=Solution()
root=TreeNode(0)
solution.postorderTraversal(root)
