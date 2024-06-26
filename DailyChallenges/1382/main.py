
# Definition for a binary tree node.
'''In a binary search tree,
 the left node_left<root and node_right> root.
 Therefore, traversing a binary tree in an inorder '''

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Step 2: Use the sorted node values to construct a balanced BST
        def sorted_array_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root
        
        sorted_vals = inorder_traversal(root)
        return sorted_array_to_bst(sorted_vals)

#needs a makeTree method so that it could be tested without test template


