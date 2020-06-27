N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
point = arr[-1][-1]
arr.sort()
for i in range(N-1):
    if arr[i][0] != arr[i+1][0]:
        point += arr[i][1]
print(point)
