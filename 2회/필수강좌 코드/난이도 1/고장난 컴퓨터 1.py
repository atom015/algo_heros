N,c = map(int,input().split())
arr = list(map(int,input().split()))
ans = 1
for i in range(N-1):
    if arr[i+1]-arr[i] <= c:
        ans += 1
    else:
        ans = 1
print(ans)

# 구현하란 데로 하면 된다.
