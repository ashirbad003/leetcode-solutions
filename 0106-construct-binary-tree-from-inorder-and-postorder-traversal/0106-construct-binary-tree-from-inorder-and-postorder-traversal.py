# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> "TreeNode":

        idx = {v: i for i, v in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx

            if left > right:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)

            mid = idx[root_val]

            # Build right subtree first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)