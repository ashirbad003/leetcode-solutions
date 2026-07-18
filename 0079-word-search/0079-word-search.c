bool dfs(char** board, int boardSize, int* boardColSize,
         int i, int j, char* word, int idx) {
    if (word[idx] == '\0')
        return true;

    if (i < 0 || i >= boardSize || j < 0 || j >= boardColSize[0] ||
        board[i][j] != word[idx])
        return false;

    char temp = board[i][j];
    board[i][j] = '#';

    bool found = dfs(board, boardSize, boardColSize, i + 1, j, word, idx + 1) ||
                 dfs(board, boardSize, boardColSize, i - 1, j, word, idx + 1) ||
                 dfs(board, boardSize, boardColSize, i, j + 1, word, idx + 1) ||
                 dfs(board, boardSize, boardColSize, i, j - 1, word, idx + 1);

    board[i][j] = temp;
    return found;
}

bool exist(char** board, int boardSize, int* boardColSize, char* word) {
    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardColSize[0]; j++) {
            if (dfs(board, boardSize, boardColSize, i, j, word, 0))
                return true;
        }
    }
    return false;
}