void dfs(int n, int k, int start, int *path, int pathSize,
         int **ans, int *returnSize) {
    if (pathSize == k) {
        ans[*returnSize] = (int *)malloc(k * sizeof(int));
        memcpy(ans[*returnSize], path, k * sizeof(int));
        (*returnSize)++;
        return;
    }

    for (int i = start; i <= n - (k - pathSize) + 1; i++) {
        path[pathSize] = i;
        dfs(n, k, i + 1, path, pathSize + 1, ans, returnSize);
    }
}

int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {
    int cap = 1;
    for (int i = 1; i <= k; i++)
        cap = cap * (n - i + 1) / i;

    int **ans = (int **)malloc(cap * sizeof(int *));
    *returnColumnSizes = (int *)malloc(cap * sizeof(int));

    for (int i = 0; i < cap; i++)
        (*returnColumnSizes)[i] = k;

    *returnSize = 0;
    int *path = (int *)malloc(k * sizeof(int));

    dfs(n, k, 1, path, 0, ans, returnSize);

    free(path);
    return ans;
}