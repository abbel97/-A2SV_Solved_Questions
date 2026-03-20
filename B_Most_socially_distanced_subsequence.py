import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    rel = [a[0]]
    for i in range(1, n - 1):
        if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
            rel.append(a[i])
    rel.append(a[-1])
    
    print(len(rel))
    print(*rel)