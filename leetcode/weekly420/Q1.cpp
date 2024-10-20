class Solution {
public:
   vector<string> stringSequence(string target) {
       vector<string> result;
       string curr = ""; 
       
       curr += 'a';
       result.push_back(curr);
       
       for(int i = 0; i < target.length(); i++) {
           if(i == 0 && target[i] == 'a') continue;
           
           if(i >= curr.length()) {
               curr += 'a';
               result.push_back(curr);
           }
           
           char lastChar = curr.back();
           while(lastChar != target[i]) {
               lastChar = (lastChar - 'a' + 1) % 26 + 'a';
               curr.back() = lastChar;
               result.push_back(curr);
           }
       }
       
       return result;
   }
};