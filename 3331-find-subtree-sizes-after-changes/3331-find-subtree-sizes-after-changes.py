class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = {}
        new_parent = [-1] * n

        def dfs(node):
            c = s[node]
            p = last.get(c, -1)
            new_parent[node] = p if p != -1 else parent[node]

            last[c] = node

            for child in children[node]:
                dfs(child)

            if p == -1:
                last.pop(c, None)
            else:
                last[c] = p

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in new_children[node]:
                ans[node] += calculate(child)
            return ans[node]

        calculate(0)
        return ans