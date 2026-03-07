import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    p = input().strip()

    ans = 0
    j = 0

    for i in range(n):
        if j < m and s[i] == p[j]:
            j += 1
            if j == m:
                ans += 1
                j = 0

    print(ans)