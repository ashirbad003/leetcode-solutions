class Solution {
public:
    long long sumAndMultiply(int n) {
        long long x = 0;
        int sum = 0;

        if (n == 0)
            return 0;

        string s = to_string(n);

        for (char c : s) {
            if (c != '0') {
                x = x * 10 + (c - '0');
                sum += (c - '0');
            }
        }

        return x * sum;
    }
};