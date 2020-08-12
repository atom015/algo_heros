N,M = map(int,input().split())
arr = [["." for i in range(M)] for i in range(N)]
chk = 1
for i in range(N):
    if i % 2 == 0:
        arr[i] = ["#"]*M
    else:
        if chk == 1:
            arr[i][-1] = "#"
        else:
            arr[i][0] = "#"
        chk *= -1
for i in arr:
    print(*i,sep='')
