import sys
from collections import Counter
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        l = int(data[idx + 1])
        r = int(data[idx + 2])
        idx += 3
        
        c = list(map(int, data[idx:idx + n]))
        idx += n
        
        left_socks = Counter(c[:l])
        right_socks = Counter(c[l:])
        for color in left_socks:
            if color in right_socks:
                common = min(left_socks[color], right_socks[color])
                left_socks[color] -= common
                right_socks[color] -= common
                l -= common
                r -= common
        
        if l < r:
            left_socks, right_socks = right_socks, left_socks
            l, r = r, l
            
        ans = 0
        diff = (l - r) // 2
        
        for color in left_socks:
            can_take = left_socks[color] // 2
            take = min(can_take, diff)
            ans += take  
            diff -= take
            l -= 2 * take
     
        results.append(str(ans + l))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()