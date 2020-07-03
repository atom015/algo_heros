x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
ans = abs((x1*y2+x2*y3+x3*y1)-(x1*y3+x3*y2+x2*y1))/2
print(str(ans)+"0")
#알고리즘:수학
