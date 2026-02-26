#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, T;
    cin >> N >> T;

    deque<long long> dq;
    dq.resize(2 * N);
    for (int i = 0; i < 2 * N; i++) cin >> dq[i];

    for (int i = 0; i < T; i++) {
        int b;
        cin >> b;

        for (int k = 0; k < b - 1; k++) {
            dq.push_back(dq.front());
            dq.pop_front();
        }

        cout << dq.front() << (i + 1 == T ? '\n' : ' ');
    }
    return 0;
}