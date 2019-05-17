#include <bits/stdc++.h>
using namespace std;

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)

int findPar(vector<int> &par, int r)
{
    if (r == -1)
        return r;

    if (r == par[r])
        return r;

    par[r] = findPar(par, par[r]);

    return par[r];
}

/// Disjoint Set
/// Given Small group of forests
/// Find Size of every forest
int main()
{
    int n, m;

    sdii(n, m);

    vector<int> par(n + 1, -1);

    int arr[500001];
    int nx;
    bool f;

    int p, tmpp;
    for (int g = 0; g < m; g++)
    {
        sdi(nx);

        if (nx == 0)
            continue;

        f = false;
        p = -1;
        for (int i = 0; i < nx; i++)
        {
            sdi(arr[i]);

            if (!f && par[arr[i]] != -1)
            {
                p = arr[i];
                f = true;
            }
        }

        if (p != -1)
        {
            p = findPar(par, p);

            for (int i = 0; i < nx; i++)
            {
                if (arr[i] == p)
                    continue;

                tmpp = findPar(par, arr[i]);

                if (tmpp == -1)
                    par[arr[i]] = p;
                else
                    par[tmpp] = p;
            }
        }
        else
        {
            p = arr[0];
            for (int i = 0; i < nx; i++)
            {
                par[arr[i]] = p;
            }
        }
    }

    unordered_map<int, int> mp;

    for (int i = 1; i <= n; i++)
    {
        if (par[i] != -1)
        {
            mp[findPar(par, i)]++;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        if (par[i] != -1)
            printf("%d ", mp[findPar(par, i)]);
        else
            printf("1 ");
    }
    cout << endl;
}