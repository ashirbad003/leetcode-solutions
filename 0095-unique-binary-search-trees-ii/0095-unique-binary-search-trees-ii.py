class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        from functools import lru_cache

        @lru_cache(None)
        def build(lo, hi):
            if lo > hi:
                return [None]

            ans = []
            for i in range(lo, hi + 1):
                for left in build(lo, i - 1):
                    for right in build(i + 1, hi):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        return build(1, n)