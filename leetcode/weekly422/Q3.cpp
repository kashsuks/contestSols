#include <vector>
#include <tuple>
#include <queue>
#include <limits>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int height = moveTime.size();
        int width = moveTime[0].size();
        
        vector<vector<long long>> bestOddPath(height, vector<long long>(width, LLONG_MAX));
        vector<vector<long long>> bestEvenPath(height, vector<long long>(width, LLONG_MAX));
        
        priority_queue<pair<long long, tuple<int, int, int>>, 
                      vector<pair<long long, tuple<int, int, int>>>, 
                      greater<>> paths;
                      
        paths.push({0, {0, 0, 0}});
        bestEvenPath[0][0] = 0;
        
        int row[] = {-1, 0, 1, 0};
        int col[] = {0, 1, 0, -1};
        
        while (!paths.empty()) {
            auto [time, current] = paths.top();
            auto [x, y, steps] = current;
            paths.pop();
            
            if ((steps % 2 == 0 && time > bestEvenPath[x][y]) || 
                (steps % 2 == 1 && time > bestOddPath[x][y])) {
                continue;
            }
            
            if (x == height - 1 && y == width - 1) {
                return time;
            }
            
            for (int i = 0; i < 4; i++) {
                int nextX = x + row[i];
                int nextY = y + col[i];
                
                if (nextX < 0 || nextY < 0 || nextX >= height || nextY >= width) continue;
                
                long long nextTime = max(time, (long long)moveTime[nextX][nextY]) + (steps % 2 == 0 ? 1 : 2);
                bool isNextOdd = !bool(steps % 2);
                auto& bestPath = isNextOdd ? bestOddPath : bestEvenPath;
                
                if (nextTime < bestPath[nextX][nextY]) {
                    bestPath[nextX][nextY] = nextTime;
                    paths.push({nextTime, {nextX, nextY, steps + 1}});
                }
            }
        }
        
        return -1;
    }
};
