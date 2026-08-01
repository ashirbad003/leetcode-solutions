# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []

        def dfs(node, target, path):
            if not node:
                return

            path.append(node.val)
            target -= node.val

            if not node.left and not node.right and target == 0:
                ans.append(path[:])
            else:
                dfs(node.left, target, path)
                dfs(node.right, target, path)

            path.pop()

        dfs(root, targetSum, [])

        return ans