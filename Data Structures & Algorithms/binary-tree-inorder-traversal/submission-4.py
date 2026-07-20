# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.appendNode(root, ret)
        return ret

    def appendNode(self, root: Optional[TreeNode], inorder_list: List[int]) -> None:
        if not root:
            return
        
        self.appendNode(root.left, inorder_list)
        inorder_list.append(root.val)
        self.appendNode(root.right, inorder_list)
        return
