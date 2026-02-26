#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    string line;
    getline(cin, line);

    for (int tc = 1; tc <= t; tc++) {
        getline(cin, line);
        stringstream ss(line);
        vector<string> v;
        string w;
        while (ss >> w) v.push_back(w);

        cout << "Case #" << tc << ": ";
        for (int i = (int)v.size() - 1; i >= 0; i--) {
            cout << v[i] << (i ? ' ' : '\n');
        }
    }
    return 0;
}