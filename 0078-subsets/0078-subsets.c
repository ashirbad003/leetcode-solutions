void dfs(int* nums, int numsSize, int index, int* path, int pathSize,
         int** ans, int* returnSize, int* returnColumnSizes) {
    ans[*returnSize] = (int*)malloc(pathSize * sizeof(int));
    memcpy(ans[*returnSize], path, pathSize * sizeof(int));
    returnColumnSizes[*returnSize] = pathSize;
    (*returnSize)++;

    for (int i = index; i < numsSize; i++) {
        path[pathSize] = nums[i];
        dfs(nums, numsSize, i + 1, path, pathSize + 1,
            ans, returnSize, returnColumnSizes);
    }
}

int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int total = 1 << numsSize;

    int** ans = (int**)malloc(total * sizeof(int*));
    *returnColumnSizes = (int*)malloc(total * sizeof(int));

    *returnSize = 0;
    int* path = (int*)malloc(numsSize * sizeof(int));

    dfs(nums, numsSize, 0, path, 0, ans, returnSize, *returnColumnSizes);

    free(path);
    return ans;
}