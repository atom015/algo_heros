N1,N2 = map(int,input().split())
D = int(input())
ch = 1
for i in range(D+1):
    if ch == 1:
        if N1 % 2 == 0:
            N2 += N1//2
            N1 = N1//2
        else:
            N2 += (N1//2)+1
            N1 = N1//2
    else:
        if N2 % 2 == 0:
            N1 += N2//2
            N2 = N2//2
        else:
            N1 += (N2//2)+1
            N2 = N2//2
    ch *= -1

print(N1,N2)
