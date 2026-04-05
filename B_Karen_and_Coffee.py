import sys
input = sys.stdin.readline

n, k, q = map(int, input().split())
recipes = [0] * 200001
for _ in range(n):
    l, r = map(int, input().split())
    recipes[l] += 1
    if r + 1 <= 200000:
        recipes[r + 1] -= 1
for i in range(1, 200001):
    recipes[i] += recipes[i - 1]
admissible = [0] * 200001

for i in range(1, 200001):
    admissible[i] = admissible[i - 1] + (1 if recipes[i] >= k else 0)
    
for _ in range(q):
    l, r = map(int, input().split())
    print(admissible[r] - admissible[l - 1])
