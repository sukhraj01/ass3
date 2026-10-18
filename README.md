const long long MOD = 1000000007LL;
    int n = a.size();

    vector<long long> v(n + 2);
    v[0] = l;
    v[n + 1] = r;
    for (int i = 1; i <= n; i++) v[i] = a[i - 1];

    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));
    vector<vector<long long>> ways(n + 2, vector<long long>(n + 2, 1));

    long long comb[351][351] = {};
    comb[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        comb[i][0] = comb[i][i] = 1;
        for (int j = 1; j < i; j++)
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
    }

    for (int len = 1; len <= n; len++) {
        for (int i = 1; i + len - 1 <= n; i++) {
            int j = i + len - 1;
            dp[i][j] = LLONG_MIN;
            ways[i][j] = 0;

            for (int k = i; k <= j; k++) {
                long long left = (k == i) ? 0 : dp[i][k - 1];
                long long right = (k == j) ? 0 : dp[k + 1][j];

                long long score = left + right + v[i - 1] * v[k] * v[j + 1];

                long long leftWays = (k == i) ? 1 : ways[i][k - 1];
                long long rightWays = (k == j) ? 1 : ways[k + 1][j];

                long long count = leftWays * rightWays % MOD;
                count = count * comb[len - 1][k - i] % MOD;

                if (score > dp[i][j]) {
                    dp[i][j] = score;
                    ways[i][j] = count;
                } else if (score == dp[i][j]) {
                    ways[i][j] = (ways[i][j] + count) % MOD;
                }
            }
        }
    }

    return {dp[1][n], ways[1][n]};
