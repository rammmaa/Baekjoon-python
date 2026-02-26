#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    deque<int> q;
    for (int i = 1; i <= n; i++) q.push_back(i);

    int ans = 0;
    while (m--) {
        int x;
        cin >> x;

        int pos = 0;
        for (int i = 0; i < (int)q.size(); i++) {
            if (q[i] == x) { pos = i; break; }
        }

        int left = pos;
        int right = (int)q.size() - pos;

        ans += min(left, right);

        if (left <= right) {
            while (pos--) {
                q.push_back(q.front());
                q.pop_front();
            }
        } else {
            int k = (int)q.size() - pos;
            while (k--) {
                q.push_front(q.back());
                q.pop_back();
            }
        }
        q.pop_front();
    }

    cout << ans << "\n";
    return 0;
}