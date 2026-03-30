import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    balance = [0] * n
    cnts = 0

    for i in range(n):
        if a[i] == '1':
            cnts += 1
        else:
            cnts -= 1
        balance[i] = cnts

    flipped = False
    possible = True

    for i in range(n - 1, -1, -1):
        current = a[i]
        
        if flipped:
            current = '1' if current == '0' else '0'

        if current != b[i]:
            if balance[i] != 0:
                possible = False
                break
            flipped = not flipped

    print("YES" if possible else "NO")