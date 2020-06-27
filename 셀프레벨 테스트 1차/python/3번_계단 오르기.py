N = int(input())
dp = [1,1]+[0 for i in range(N+1)]
for i in range(2,N+1):
    dp[i] = dp[i-2]+1
print(dp)
