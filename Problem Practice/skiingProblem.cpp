#include "bits/stdc++.h"
using namespace std;

int moves[] = {1, 0, 0, 1, -1, 0, 0, -1};

bool compare(pair<int, int> a, pair<int, int> b)
{
    return (a.first > b.first) || (a.first == b.first && a.second < b.second);
}

bool validMove(int i, int j, int n, int m)
{
    return i >= 0 && i < n && j >= 0 && j < m;
}

pair<int, int> calculateSkiingDrop(vector<vector<int>> &graph, vector<vector<pair<int, int>>> &dp, int i, int j)
{
    int x, y;

    pair<int, int> mx;
    mx.first = 1;
    mx.second = graph[i][j];

    int rotate = 0;
    while (rotate < 4)
    {
        x = i + moves[2 * rotate];
        y = j + moves[2 * rotate + 1];

        if (validMove(x, y, graph.size(), graph[0].size()) && graph[i][j] > graph[x][y])
        {
            pair<int, int> tmp;
            if (dp[x][y].first == -1)
                tmp = calculateSkiingDrop(graph, dp, x, y);
            else
            {
                tmp.first = dp[x][y].first;
                tmp.second = dp[x][y].second;
            }
            tmp.first++;
            if (compare(tmp, mx))
            {
                mx.first = tmp.first;
                mx.second = tmp.second;
            }
        }
        rotate++;
    }

    dp[i][j].first = mx.first;
    dp[i][j].second = mx.second;

    return mx;
}

int main()
{
    FILE *fp;
    fp = fopen("input.txt", "r");

    int n, m;

    fscanf(fp, "%d %d", &n, &m);

    pair<int, int> pp;
    pp.first = -1;
    pp.second = -1;
    vector<pair<int, int>> vp(m, pp);
    vector<vector<pair<int, int>>> dp(n, vp);

    vector<vector<int>> graph(n);

    int x;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            fscanf(fp, "%d", &x);
            graph[i].push_back(x);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (dp[i][j].first == -1)
            {
                calculateSkiingDrop(graph, dp, i, j);
            }
        }
    }

    pair<int, int> ans;
    ans.first = 0;
    ans.second = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (compare(dp[i][j], ans))
            {
                ans.first = dp[i][j].first;
                ans.second = graph[i][j] - dp[i][j].second;
            }
        }
    }

    cout << ans.first << " " << ans.second << endl;

    return 0;
}