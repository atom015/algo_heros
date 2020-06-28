n = int(input())
dp = [1,1]+[0 for i in range(n)]
for i in range(1,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])
#알고리즘 : dp
