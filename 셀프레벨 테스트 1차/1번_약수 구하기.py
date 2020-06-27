n = int(input())
ans = []
for i in range(1,n+1):
    if n % i == 0:
    	ans.append(i)
for i in ans:
    print(i,end=' ')
#알고리즘 : 약수구하기
