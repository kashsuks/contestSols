class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        int n = s.length(), result = 0;
        
        for(int len = 1; len <= n; len++) {
            vector<int> freq(26, 0);
            
            for(int i = 0; i < len; i++) {
                freq[s[i] - 'a']++;
            }
            
            if(hasCharWithFreqK(freq, k)) result++;
            
            for(int i = len; i < n; i++) {
                freq[s[i] - 'a']++;
                freq[s[i-len] - 'a']--;
                if(hasCharWithFreqK(freq, k)) result++;
            }
        }
        return result;
    }
    
private:
    bool hasCharWithFreqK(vector<int>& freq, int k) {
        for(int f : freq) {
            if(f >= k) return true;
        }
        return false;
    }
};