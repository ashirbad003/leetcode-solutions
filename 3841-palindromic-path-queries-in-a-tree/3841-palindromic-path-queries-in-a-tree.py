class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Iterative DFS: preorder, parent, depth
        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]
        while stack:
            x = stack.pop()
            order.append(x)
            for y in adj[x]:
                if y != parent[x]:
                    parent[y] = x
                    depth[y] = depth[x] + 1
                    stack.append(y)

        # Euler tour: subtree of x is [tin[x], tout[x]]
        tin = [0] * n
        for i, x in enumerate(order):
            tin[x] = i
        size = [1] * n
        for x in reversed(order):
            if parent[x] >= 0:
                size[parent[x]] += size[x]
        tout = [tin[x] + size[x] - 1 for x in range(n)]

        # Binary lifting for LCA
        LOG = max(1, n.bit_length())
        up = [[p if p >= 0 else 0 for p in parent]]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[x]] for x in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return up[0][a]

        # Q[x] = parity mask of root..x (inclusive)
        Q = [0] * n
        for x in order:
            bit = 1 << (ord(s[x]) - 97)
            Q[x] = (Q[parent[x]] if parent[x] >= 0 else 0) ^ bit

        # Fenwick tree supporting range-XOR update and point query
        tree = [0] * (n + 1)

        def add(i, m):
            i += 1
            while i <= n:
                tree[i] ^= m
                i += i & -i

        def point(i):
            res = 0
            i += 1
            while i > 0:
                res ^= tree[i]
                i -= i & -i
            return res

        def range_xor(l, r, m):
            add(l, m)
            if r + 1 < n:
                add(r + 1, m)

        # Build difference array so point(i) == Q[order[i]]
        A = [Q[order[i]] for i in range(n)]
        for i in range(n):
            add(i, A[i] ^ (A[i - 1] if i else 0))

        chars = list(s)
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x = int(parts[1])
                c = parts[2]
                delta = (1 << (ord(chars[x]) - 97)) ^ (1 << (ord(c) - 97))
                if delta:
                    range_xor(tin[x], tout[x], delta)
                chars[x] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = point(tin[u]) ^ point(tin[v]) ^ (1 << (ord(chars[l]) - 97))
                answer.append(mask & (mask - 1) == 0)
        return answer