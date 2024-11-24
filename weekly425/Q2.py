class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t) or len(s) % k != 0:
            return False
        
        if sorted(s) != sorted(t):
            return False
            
        n = len(s)
        chunkSize = n // k
        
        if k == 1:
            return s == t
            
        sChunks = [s[i:i+chunkSize] for i in range(0, n, chunkSize)]
        tChunks = [t[i:i+chunkSize] for i in range(0, n, chunkSize)]
        
        sFreq = {}
        for chunk in sChunks:
            sFreq[chunk] = sFreq.get(chunk, 0) + 1
            
        tFreq = {}
        for chunk in tChunks:
            tFreq[chunk] = tFreq.get(chunk, 0) + 1
            
        return sFreq == tFreq