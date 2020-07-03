from sys import *
ip = stdin.readline
def Sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans

def update(i,dif):
    while i < len(tree):
        tree[i] += dif
        i += (i & -i)

n,m = map(int,input().split())
tree = [0 for i in range(n+1)]
arr = [0 for i in range(n+1)]
tmp = [0]+list(map(int,ip().split()))
for i in range(1,n+1):
    arr[i] = tmp[i]
    update(i,arr[i])

for i in range(m):
    a,b = map(int,ip().split())
    s = Sum(b)-Sum(a-1)
    print("+"+str(s) if s > 0 else s)
#알고리즘:펜윅트리
