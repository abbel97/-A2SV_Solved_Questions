import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    white_count = s[:k].count('W')
    min_recolor = white_count
    
    for i in range(k, n):
        if s[i] == 'W':
            white_count += 1
        if s[i - k] == 'W':
            white_count -= 1
        min_recolor = min(min_recolor, white_count)
    
    print(min_recolor)