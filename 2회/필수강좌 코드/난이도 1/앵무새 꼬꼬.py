for i in range(int(input())):
    s = input()
    ans = ""
    for i in s:
        if i.lower() in ("a","e","i","o","u"):
            ans += i
    print("???" if len(ans) == 0 else ans)
# 문자열 탐색문제
