char* minWindow(char* s, char* t) {
    int need[128] = {0};
    int required = 0;

    for (int i = 0; t[i]; i++) {
        if (need[(unsigned char)t[i]] == 0)
            required++;
        need[(unsigned char)t[i]]++;
    }

    int window[128] = {0};
    int formed = 0;
    int left = 0, right = 0;
    int minLen = INT_MAX, start = 0;

    while (s[right]) {
        unsigned char c = s[right];
        window[c]++;
        if (need[c] > 0 && window[c] == need[c])
            formed++;

        while (formed == required) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                start = left;
            }

            unsigned char d = s[left];
            window[d]--;
            if (need[d] > 0 && window[d] < need[d])
                formed--;
            left++;
        }

        right++;
    }

    if (minLen == INT_MAX) {
        char* res = (char*)malloc(1);
        res[0] = '\0';
        return res;
    }

    char* res = (char*)malloc(minLen + 1);
    strncpy(res, s + start, minLen);
    res[minLen] = '\0';
    return res;
}