from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val =val 
        self.left=left
        self.right=right
class Solution:
    def delNodes(self,root: Optional[TreeNode],to_delete: list[int])->list[TreeNode]:
        print(root)
        pass
solution=Solution()
root= [1,2,3,4,5,6,7]
to_delete=[3,5]
solution.delNodes(root,to_delete)