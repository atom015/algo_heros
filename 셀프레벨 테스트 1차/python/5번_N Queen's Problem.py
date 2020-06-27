col = [0 for i in range(15+1)]
def promising(i):
    k = 1
    flag = True
    while k < i and flag == True:
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k:
            flag = False
        k += 1
    return flag
def queens(i):
    global cnt
    if promising(i) == True:
        if i == N:
            cnt += 1
        else:
            for j in range(1,N+1):
                col[i+1] = j
                queens(i+1)
cnt = 0
N = int(input())
queens(0)
print(cnt)
#알고리즘 : N queen,백트래킹
