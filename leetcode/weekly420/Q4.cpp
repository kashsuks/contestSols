#include <vector>
#include <deque>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    long long modMultiply(long long a, long long b, long long mod) {
        long long result = 0;
        a %= mod;
        while (b > 0) {
            if (b % 2 == 1) {
                result = (result + a) % mod;
            }
            a = (a * 2) % mod;
            b /= 2;
        }
        return result;
    }

    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);

        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }

        const long long basePrimary = 911382628;
        const long long modPrimary = 1000000000000000007LL;
        const long long baseSecondary = 3571;
        const long long modSecondary = 1000000000000000009LL;

        int maxLen = n + 1;
        vector<long long> basePowerPrimary(maxLen, 1);
        vector<long long> basePowerSecondary(maxLen, 1);

        for (int i = 1; i < maxLen; ++i) {
            basePowerPrimary[i] = modMultiply(basePowerPrimary[i - 1], basePrimary, modPrimary);
            basePowerSecondary[i] = modMultiply(basePowerSecondary[i - 1], baseSecondary, modSecondary);
        }

        // Initialize hash arrays for forward and reverse hashes
        vector<long long> forwardHashPrimary(n, 0), reverseHashPrimary(n, 0);
        vector<long long> forwardHashSecondary(n, 0), reverseHashSecondary(n, 0);
        vector<int> subtreeLen(n, 1);
        vector<int> inDegree(n, 0);

        for (int i = 0; i < n; ++i) {
            inDegree[i] = children[i].size();
        }

        deque<int> bfsQueue;
        for (int i = 0; i < n; ++i) {
            if (inDegree[i] == 0) {
                bfsQueue.push_back(i);
            }
        }

        unordered_map<long long, int> subtreeHashPrimary;
        unordered_map<long long, int> subtreeHashSecondary;

        while (!bfsQueue.empty()) {
            int current = bfsQueue.front();
            bfsQueue.pop_front();

            long long combinedPrimaryHash = 0;
            for (int child : children[current]) {
                combinedPrimaryHash = (modMultiply(combinedPrimaryHash, basePowerPrimary[subtreeLen[child]], modPrimary) + forwardHashPrimary[child]) % modPrimary;
            }
            combinedPrimaryHash = (modMultiply(combinedPrimaryHash, basePrimary, modPrimary) + s[current]) % modPrimary;
            forwardHashPrimary[current] = combinedPrimaryHash;

            long long reversePrimaryHash = s[current];
            for (int i = children[current].size() - 1; i >= 0; --i) {
                int child = children[current][i];
                reversePrimaryHash = (modMultiply(reversePrimaryHash, basePowerPrimary[subtreeLen[child]], modPrimary) + reverseHashPrimary[child]) % modPrimary;
            }
            reverseHashPrimary[current] = reversePrimaryHash;

            long long combinedSecondaryHash = 0;
            for (int child : children[current]) {
                combinedSecondaryHash = (modMultiply(combinedSecondaryHash, basePowerSecondary[subtreeLen[child]], modSecondary) + forwardHashSecondary[child]) % modSecondary;
            }
            combinedSecondaryHash = (modMultiply(combinedSecondaryHash, baseSecondary, modSecondary) + s[current]) % modSecondary;
            forwardHashSecondary[current] = combinedSecondaryHash;

            long long reverseSecondaryHash = s[current];
            for (int i = children[current].size() - 1; i >= 0; --i) {
                int child = children[current][i];
                reverseSecondaryHash = (modMultiply(reverseSecondaryHash, basePowerSecondary[subtreeLen[child]], modSecondary) + reverseHashSecondary[child]) % modSecondary;
            }
            reverseHashSecondary[current] = reverseSecondaryHash;

            int totalSubtreeLength = 1;
            for (int child : children[current]) {
                totalSubtreeLength += subtreeLen[child];
            }
            subtreeLen[current] = totalSubtreeLength;

            if (current != 0) {
                int parentIdx = parent[current];
                inDegree[parentIdx]--;
                if (inDegree[parentIdx] == 0) {
                    bfsQueue.push_back(parentIdx);
                }
            }
        }

        vector<bool> result(n, false);
        for (int i = 0; i < n; ++i) {
            if (forwardHashPrimary[i] == reverseHashPrimary[i] && forwardHashSecondary[i] == reverseHashSecondary[i]) {
                result[i] = true;
            }
        }

        return result;
    }
};
