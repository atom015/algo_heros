from sys import *
from math import sqrt
ip = stdin.readline
N = int(ip())
arr = []
ans = []
for i in range(N):
    arr.append(list(map(int,ip().split()))+[i+1])
for i in range(N):
    for j in range(i+1,N):
        x1,x2 = arr[i][0],arr[j][0]
        y1,y2 = arr[i][1],arr[j][1]
        n1,n2 = arr[i][2],arr[j][2]
        ans.append([int(sqrt(((x2-x1)**2)+ ((y2-y1)**2))),n1,n2])
ans.sort()
print(*ans[-1][1:])
