MOD = 1000000007

def powerModFunc(a, b):
    res = 1
    a %= MOD
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

def initFact(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invFact = [1] * (n + 1)
    invFact[n] = powerModFunc(fact[n], MOD - 2)
    for i in range(n - 1, -1, -1):
        invFact[i] = invFact[i + 1] * (i + 1) % MOD
    return fact, invFact

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        freq = [0] * 10
        totalSum = 0
        
        for c in num:
            d = int(c)
            freq[d] += 1
            totalSum += d
        
        if totalSum % 2 != 0:
            return 0
        
        sumHalf = totalSum // 2
        k = (n + 1) // 2
        
        fact, invFact = initFact(n)
        
        dp = [[0] * (sumHalf + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        
        for d in range(10):
            if freq[d] == 0:
                continue
            for c in range(k, -1, -1):
                for s in range(sumHalf, -1, -1):
                    if dp[c][s] == 0:
                        continue
                    for t in range(1, min(freq[d], k - c) + 1):
                        if s + d * t > sumHalf:
                            break
                        comb = (fact[freq[d]] * invFact[t] % MOD) * invFact[freq[d] - t] % MOD
                        dp[c + t][s + d * t] = (dp[c + t][s + d * t] + dp[c][s] * comb) % MOD
        
        validAssignments = dp[k][sumHalf]
        if validAssignments == 0:
            return 0
        
        prodFactFd = 1
        for d in range(10):
            prodFactFd = prodFactFd * fact[freq[d]] % MOD
        
        fkFnk = (fact[k] * fact[n - k]) % MOD
        invProdFactFd = powerModFunc(prodFactFd, MOD - 2)
        answer = (fkFnk * validAssignments) % MOD
        answer = (answer * invProdFactFd) % MOD
        
        return answer
