n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(a[-1] - a[0])
else:
    differences = []
    for i in range(1, n):
        differences.append(a[i] - a[i-1])
    differences.sort(reverse=True)
    print(a[-1] - a[0] - sum(differences[:k-1]))