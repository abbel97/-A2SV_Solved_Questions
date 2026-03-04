import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
        
    casinos.sort(key=lambda x: x[0])
    max_heap = [] 
    idx = 0
    current = k
    
    while True:
        while idx < n and casinos[idx][0] <= current:
            l, r, real = casinos[idx]
            if current <= r:
                heapq.heappush(max_heap, (-real, real))
            idx += 1
        
        if not max_heap:
            break
        
        best_real = heapq.heappop(max_heap)[1]
        
        if best_real <= current:
            break
        
        current = best_real
    
    print(current)