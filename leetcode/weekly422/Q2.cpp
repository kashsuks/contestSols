#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int dungeonHeight = moveTime.size();
        int dungeonWidth = moveTime[0].size();
        
        int finalRoomX = dungeonHeight - 1;
        int finalRoomY = dungeonWidth - 1;
        
        vector<vector<int>> quickestPath(dungeonHeight, vector<int>(dungeonWidth, INT_MAX));
        
        queue<pair<int, pair<int, int>>> roomQueue;
        roomQueue.push({0, {0, 0}});
        quickestPath[0][0] = 0;
        
        vector<pair<int, int>> possibleMoves = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        
        while (!roomQueue.empty()) {
            int timeSpent = roomQueue.front().first;
            int myX = roomQueue.front().second.first;
            int myY = roomQueue.front().second.second;
            roomQueue.pop();
            
            if (timeSpent > quickestPath[myX][myY]) continue;
            
            for (auto& nextMove : possibleMoves) {
                int nextX = myX + nextMove.first;
                int nextY = myY + nextMove.second;
                
                if (nextX >= 0 && nextX < dungeonHeight && nextY >= 0 && nextY < dungeonWidth) {
                    int timeToNext = max(timeSpent, moveTime[nextX][nextY]) + 1;
                    
                    if (timeToNext < quickestPath[nextX][nextY]) {
                        quickestPath[nextX][nextY] = timeToNext;
                        roomQueue.push({timeToNext, {nextX, nextY}});
                    }
                }
            }
        }
        
        return quickestPath[finalRoomX][finalRoomY];
    }
};
